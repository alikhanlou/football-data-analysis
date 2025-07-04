# 🏆 Team Analysis Project

## Overview
This **Team Analysis Project** provides comprehensive analytics and basic predictive modeling for football teams across three major European leagues: **Bundesliga**, **Premier League**, and **La Liga**.  
Using a synthetic dataset of **700 matches** from the **2022-2023 season**, the project explores various match statistics including:

- League and season
- Date of match
- Home and away teams
- Goals scored by each team
- Shots taken
- Possession percentages
- Yellow and red cards
- Match result

The analysis includes generation of summary tables, key performance indicators, and **five visualizations** that illustrate team performances, goal statistics, possession, discipline records, and match outcomes.

## Predictive Modeling
A **Random Forest Classifier** was developed to predict match outcomes (win, draw, lose) based on selected match statistics.  
⚠ The model achieved an accuracy of **34%**. The relatively low performance highlights the limitations of using minimal features and synthetic data, and emphasizes the importance of richer datasets in real-world applications where significantly better accuracy would be expected.

## Technologies Used
- **Python**
- **pandas**
- **matplotlib**
- **seaborn**
- **scikit-learn**

## Dataset
- `matches_2022_2023.csv`  
  A synthetic CSV file containing match data for 700 games across the three leagues.

## Reports
- `analysis_report.md` — Detailed analysis summary.
- `model_report.md` — Summary of the predictive model's performance.
- `model_results.txt` — Contains raw output of the trained model including confusion matrix and classification report.

## Notes
- This project uses synthetic data created for educational and demonstration purposes only.
