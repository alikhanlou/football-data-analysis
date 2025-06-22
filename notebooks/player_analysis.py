from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

players_data = Path(__file__).resolve().parent.parent / "data" / "raw" / "top5_leagues_players_2023.csv"
df = pd.read_csv(players_data)

print(df.head())
print("--------------------\n--------------------")
print(df.info())
print("--------------------\n--------------------")
print(df.describe())
print("--------------------\n--------------------")
print(df.corr(numeric_only=True))
print("--------------------\n--------------------")
print(df.isnull().sum())

