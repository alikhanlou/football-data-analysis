# ⚽ Football Dashboard

## Overview
This **Football Dashboard** is an interactive visualization app built with **Streamlit**.  
It provides users with dynamic statistics and visualizations based on the **matches_2022_2023** dataset (a synthetic dataset simulating match results from major leagues).  
Users can select a team to view:

- Total matches played, goals scored, and goals conceded
- Bar chart comparing goals scored vs. goals conceded
- Cumulative points over matches (line chart)
- Match outcome distribution (pie chart)
- Shots vs. possession correlation heatmap (for home matches)
- Shots vs. goals scatter plot (for home matches)

## Features
✅ Interactive team selection via a dropdown menu  
✅ Automatic generation of multiple visualizations for the selected team  
✅ Ability to **save all generated plots** by clicking the **"Save all plots"** button located at the bottom-left of the dashboard  
✅ A detailed description of the dashboard’s features and functionalities is available in `dashboard_report.md`.

## Technologies Used
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**

## Dataset
- `matches_2022_2023.csv`  
This is a synthetic CSV dataset containing data from 700 simulated matches across major European leagues (Premier League, La Liga, Bundesliga).

## How to Run

#### 1️⃣ Open the root folder of the repository in your terminal.

#### 2️⃣ Run the following command to launch the dashboard:
streamlit run football_dashboard/scripts/streamlit_app.py

#### 3️⃣ The dashboard will open automatically in your web browser.

## Saving Visualizations
You can save all plots for the selected team by clicking the **"Save all plots"** button.  
The plots will be saved in the `visualizations` directory inside the project folder.
