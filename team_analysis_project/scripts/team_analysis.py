import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


players_data = Path(__file__).resolve().parent.parent / "data" / "matches_2022_2023.csv"
df = pd.read_csv(players_data)


print(df.head())
print("\n---------------------------\n")
print(df.info())
print("\n---------------------------\n")
print(df.describe())
print("\n---------------------------\n")


print("Missing values per column:")
print(df.isnull().sum())
print("\n---------------------------\n")


goals = df.groupby("home_team")["home_goals"].sum() + df.groupby("away_team")["away_goals"].sum()
goals = goals.sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=goals.values, y=goals.index)
plt.title("Total Goals Scored by Teams")
plt.xlabel("Goals")
plt.ylabel("Team")
plt.tight_layout()
plt.show()


ownership = df.groupby("home_team")["home_possession"].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=ownership.values, y=ownership.index)
plt.title("Average Possession by Teams (Home Matches)")
plt.xlabel("Possession (%)")
plt.ylabel("Team")
plt.tight_layout()
plt.show()


cards = df.groupby("home_team")[["home_yellow", "home_red"]].sum().sort_values(by="home_yellow", ascending=False)

cards.plot(kind="bar", figsize=(12,7))
plt.title("Yellow & Red Cards by Teams (Home)")
plt.xlabel("Team")
plt.ylabel("Number of Cards")
plt.tight_layout()
plt.show()










def calculate_points(row):
    if row["home_goals"] > row["away_goals"]:
        return 3, 0  # home win
    elif row["home_goals"] < row["away_goals"]:
        return 0, 3  # away win
    else:
        return 1, 1  # draw

df[["home_points", "away_points"]] = df.apply(calculate_points, axis=1, result_type="expand")


home_summary = df.groupby("home_team").agg({
    "home_points": "sum",
    "home_goals": "sum",
    "away_goals": "sum",
    "home_possession": "mean",
    "home_yellow": "sum",
    "home_red": "sum"
}).rename(columns={
    "home_goals": "goals_scored",
    "away_goals": "goals_conceded"
})

away_summary = df.groupby("away_team").agg({
    "away_points": "sum",
    "away_goals": "sum",
    "home_goals": "sum",
    "away_possession": "mean",
    "away_yellow": "sum",
    "away_red": "sum"
}).rename(columns={
    "away_goals": "goals_scored",
    "home_goals": "goals_conceded"
})


team_summary = home_summary.add(away_summary, fill_value=0)


team_summary = team_summary.sort_values(by="home_points", ascending=False)

print(team_summary)


team_summary["total_points"] = team_summary["home_points"]
plt.figure(figsize=(10,6))
sns.barplot(x=team_summary["total_points"], y=team_summary.index)
plt.title("Team Ranking by Points (Home)")
plt.xlabel("Points")
plt.ylabel("Team")
plt.tight_layout()
plt.show()


team_summary[["goals_scored", "goals_conceded"]].plot(kind="bar", figsize=(12,7))
plt.title("Goals Scored vs Conceded by Teams")
plt.xlabel("Team")
plt.ylabel("Goals")
plt.tight_layout()
plt.show()



