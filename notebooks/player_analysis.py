from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

players_data = Path(__file__).resolve().parent.parent / "data" / "raw" / "top5_leagues_players_2023.csv"
df = pd.read_csv(players_data)

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())