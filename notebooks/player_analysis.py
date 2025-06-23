from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

players_data = Path(__file__).resolve().parent.parent / "data" / "raw" / "top5_leagues_players_2023.csv"
df = pd.read_csv(players_data)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 827cceb (new2)


print(df.head())
print("--------------------\n--------------------")
print(df.info())
print("--------------------\n--------------------")
print(df.describe())
print("--------------------\n--------------------")
print(df.corr(numeric_only=True))
print("--------------------\n--------------------")
print(df.isnull().sum())
print("--------------------\n--------------------")



df["custom_rating"] = (
    df["goals"] * 4 +
    df["assists"] * 3 +
    df["shots"] * 0.5 -
    df["yellow_cards"] -
    df["red_cards"] * 3
)
top_player = df.sort_values(by="custom_rating",ascending=False).head(1)
print(top_player[["name","club","age","goals","assists","custom_rating"]])


print("--------------------\n--------------------")


goals_by_position = df.groupby("position")["goals"].sum().sort_values(ascending=False)
sns.barplot(x=goals_by_position.values, y=goals_by_position.index)
plt.title("Total Goals by Position")
plt.xlabel("Goals")
plt.ylabel("Position")
plt.tight_layout()
plt.show()




sns.scatterplot(x="minutes", y="custom_rating", data=df)
plt.title("Rating vs Minutes Played")
plt.xlabel("Minutes Played")
plt.ylabel("Custom Rating")
plt.tight_layout()
plt.show()



position_stats = df.groupby("position").agg({
    "goals": "mean",
    "assists": "mean",
    "custom_rating": "mean"
}).sort_values(by="custom_rating", ascending=False)
print(position_stats)




sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
<<<<<<< HEAD
plt.show()
=======
print(df.head())
print("--------------------\n--------------------")
print(df.info())
print("--------------------\n--------------------")
print(df.describe())
print("--------------------\n--------------------")
print(df.corr(numeric_only=True))
print("--------------------\n--------------------")
print(df.isnull().sum())

>>>>>>> 477add7 (new)
=======
plt.show()
>>>>>>> 827cceb (new2)
