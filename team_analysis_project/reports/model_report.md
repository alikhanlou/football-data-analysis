# Random Forest Model - Match Result Prediction

## Overview
In this project, we trained a **Random Forest Classifier** to predict the outcome of football matches (win, draw, or loss for the home team) in the 2022-2023 season, based on features related to possession and disciplinary records.

## Data
The dataset includes match records from **Premier League**, **La Liga**, and **Bundesliga** with the following features used for prediction:
- `home_possession`
- `away_possession`
- `home_yellow`
- `away_yellow`
- `home_red`
- `away_red`

The target variable (`result`) was defined as:
- `1`: Home team win
- `0`: Draw
- `-1`: Home team loss

## Model
- **Algorithm:** Random Forest Classifier  
- **Train/Test Split:** 80% training, 20% testing  
- **Random Seed:** 42 (for reproducibility)

## Results

**Confusion Matrix**
```
[[13  5 26]
 [ 7  7 19]
 [27  8 28]]
```

**Classification Report**
```
              precision    recall  f1-score   support

          -1       0.28      0.30      0.29        44
           0       0.35      0.21      0.26        33
           1       0.38      0.44      0.41        63

    accuracy                           0.34       140
   macro avg       0.34      0.32      0.32       140
weighted avg       0.34      0.34      0.34       140
```

## Interpretation
- The model achieved **34% overall accuracy**, which is modest and indicates the difficulty of predicting match outcomes based only on possession and card statistics.
- The model performed slightly better at identifying home wins (`1`) compared to draws or losses.
- The relatively low precision and recall suggest that including additional features (such as shots, goals scored, team strength indicators, or player ratings) could improve predictive performance.

## Files generated
- `models/random_forest_model.pkl`: The trained Random Forest model (saved using `joblib`).
- `reports/model_results.txt`: A text file containing the confusion matrix and classification report.

## Next steps
- Enhance the feature set to include offensive and defensive metrics.
- Try hyperparameter tuning of the Random Forest model.
- Experiment with other classification algorithms (e.g., Gradient Boosting, XGBoost, Logistic Regression).
