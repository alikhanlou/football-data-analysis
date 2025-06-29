# Machine Learning Model Report: Predicting Custom Player Rating

This report summarizes the development and evaluation of a simple machine learning model designed to predict a custom player rating based on performance metrics from the 2023 season of the top 5 European football leagues.

---

## Dataset Overview

The dataset consists of 10 players and includes the following features:
- `goals`
- `assists`
- `shots`
- `minutes`
- `yellow_cards`
- `red_cards`

A custom rating was calculated using:
```
custom_rating = (goals * 4) + (assists * 3) + (shots * 0.5) - yellow_cards - (red_cards * 3)
```

---

## Model Details

- **Model type:** Linear Regression
- **Input features:** `goals`, `assists`, `minutes`
- **Target variable:** `custom_rating`
- **Data split:** 80% training, 20% testing (random_state=42)

---

## Model Evaluation

The model was trained and tested, achieving the following results on the test set:
- **Mean Squared Error (MSE):** 1.05
- **R-squared Score (R²):** 1.00

These results indicate that the model fits the small dataset almost perfectly, although this could be due to overfitting because of the very limited data.

---

## Model Coefficients

| Feature | Coefficient |
|----------|-------------|
| goals | 4.33 |
| assists | 3.06 |
| minutes | 0.02 |

These coefficients align closely with the custom rating formula, confirming that the model successfully learned the relative importance of each feature.

---

## Notes

- The high R² score (1.00) reflects a perfect fit on the test data, but caution is advised when interpreting this result due to the small sample size (only 10 players).
- For a more robust model, it is recommended to use a larger dataset.
