import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Title
st.title("⚽ Football Team Dashboard 2022-2023")

# Load data
data_path = Path(__file__).resolve().parent.parent / "data" / "matches_2022_2023.csv"
df = pd.read_csv(data_path)

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Team selection
teams = sorted(set(df["home_team"]).union(set(df["away_team"])))
team_choice = st.selectbox("Select a team:", teams)

# Filter data
team_df = df[(df["home_team"] == team_choice) | (df["away_team"] == team_choice)]

# Summary stats
st.subheader(f"📊 Performance Summary for {team_choice}")

total_matches = team_df.shape[0]
total_goals_for = team_df.loc[team_df["home_team"] == team_choice, "home_goals"].sum() + \
                  team_df.loc[team_df["away_team"] == team_choice, "away_goals"].sum()

total_goals_against = team_df.loc[team_df["home_team"] == team_choice, "away_goals"].sum() + \
                      team_df.loc[team_df["away_team"] == team_choice, "home_goals"].sum()

st.write(f"Total matches: {total_matches}")
st.write(f"Goals scored: {total_goals_for}")
st.write(f"Goals conceded: {total_goals_against}")

# Bar chart goals
fig1, ax1 = plt.subplots()
sns.barplot(x=["Goals Scored", "Goals Conceded"], y=[total_goals_for, total_goals_against], ax=ax1)
st.pyplot(fig1)

# Match points
def calculate_points(row, team):
    if row["home_team"] == team:
        if row["home_goals"] > row["away_goals"]:
            return 3
        elif row["home_goals"] == row["away_goals"]:
            return 1
        else:
            return 0
    else:
        if row["away_goals"] > row["home_goals"]:
            return 3
        elif row["away_goals"] == row["home_goals"]:
            return 1
        else:
            return 0

team_df.loc[:, "points"] = team_df.apply(lambda row: calculate_points(row, team_choice), axis=1)
team_df.loc[:, "cumulative_points"] = team_df["points"].cumsum()

# Line chart cumulative points
fig2, ax2 = plt.subplots()
ax2.plot(team_df.index, team_df["cumulative_points"], marker="o")
ax2.set_xlabel("Match")
ax2.set_ylabel("Cumulative Points")
ax2.set_title(f"Cumulative Points for {team_choice}")
st.pyplot(fig2)

# Pie chart outcomes
win_count = (team_df["points"] == 3).sum()
draw_count = (team_df["points"] == 1).sum()
loss_count = (team_df["points"] == 0).sum()

fig3, ax3 = plt.subplots()
ax3.pie([win_count, draw_count, loss_count], labels=["Wins", "Draws", "Losses"], autopct="%1.1f%%")
ax3.set_title(f"Match Outcomes for {team_choice}")
st.pyplot(fig3)

# Advanced: possession vs shots heatmap
st.subheader("🔥 Shots vs Possession Heatmap(Home matches)")
fig4, ax4 = plt.subplots()
heatmap_data = team_df[["home_possession", "home_shots"]]
sns.heatmap(heatmap_data.corr(), annot=True, cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

# Advanced: scatter of shots vs goals
st.subheader("⚡ Shots vs Goals Scatter Plot(Home matches)")
fig5, ax5 = plt.subplots()
ax5.scatter(team_df["home_shots"], team_df["home_goals"].where(team_df["home_team"] == team_choice, team_df["away_goals"]))
ax5.set_xlabel("Shots")
ax5.set_ylabel("Goals")
ax5.set_title(f"Shots vs Goals for {team_choice}")
st.pyplot(fig5)

# Optional: save visualizations
if st.button("Save all plots"):
    fig1.savefig(Path(__file__).resolve().parent.parent / "visualizations" / f"{team_choice}_goals_bar.png")
    fig2.savefig(Path(__file__).resolve().parent.parent / "visualizations" / f"{team_choice}_cumulative_points.png")
    fig3.savefig(Path(__file__).resolve().parent.parent / "visualizations" / f"{team_choice}_outcomes_pie.png")
    fig4.savefig(Path(__file__).resolve().parent.parent / "visualizations" / f"{team_choice}_heatmap.png")
    fig5.savefig(Path(__file__).resolve().parent.parent / "visualizations" / f"{team_choice}_shots_goals_scatter.png")
    st.success("Plots saved to visualizations folder!")



