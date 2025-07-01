from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def load_data():
    data_path = Path(__file__).resolve().parent.parent / "data" / "matches_2022_2023.csv"
    df = pd.read_csv(data_path)
    return df

def create_result_column(df):
    def match_result(row):
        if row["home_goals"] > row["away_goals"]:
            return 1
        elif row["home_goals"] < row["away_goals"]:
            return -1
        else:
            return 0
    df["result"] = df.apply(match_result, axis=1)
    return df

def build_and_evaluate_model(df):
    features = [
        "home_possession", "away_possession",
        "home_yellow", "away_yellow",
        "home_red", "away_red"
    ]
    
    X = df[features]
    y = df["result"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)


    reports_path = Path(__file__).resolve().parent.parent / "reports" / "model_results.txt"
    with open(reports_path, "w") as f:
        f.write("Random Forest Model Evaluation\n\n")
        f.write("Confusion Matrix:\n")
        f.write(str(cm) + "\n\n")
        f.write("Classification Report:\n")
        f.write(cr)

    
    model_path = Path(__file__).resolve().parent.parent / "models" / "random_forest_model.pkl"
    joblib.dump(model, model_path)

    print("✅ Model trained and results saved.")
    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(cr)

if __name__ == "__main__":
    df = load_data()
    df = create_result_column(df)
    build_and_evaluate_model(df)
