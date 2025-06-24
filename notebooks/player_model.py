from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


players_data = Path(__file__).resolve().parent.parent / "data" / "raw" / "top5_leagues_players_2023.csv"
df = pd.read_csv(players_data)
df["custom_rating"] = (
    df["goals"] * 4 +
    df["assists"] * 3 +
    df["shots"] * 0.5 -
    df["yellow_cards"] -
    df["red_cards"] * 3
)


X = df[["goals", "assists", "minutes"]]
y = df["custom_rating"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")


coeff_df = pd.DataFrame(model.coef_, X.columns, columns=["Coefficient"])
print(coeff_df)