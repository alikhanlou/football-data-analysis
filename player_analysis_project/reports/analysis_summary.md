# Top 5 European Leagues Players 2023 - Data Analysis Report

This analysis covers the performance of selected top players from the 2023 season across the five major European football leagues. The dataset includes **10 players** with statistics such as goals, assists, shots, minutes played, and disciplinary records.

---

## Dataset Overview
- **Number of players:** 10  
- **Attributes:** `name`, `league`, `club`, `age`, `position`, `goals`, `assists`, `shots`, `minutes`, `yellow_cards`, `red_cards`
- **Missing data:** None

---

## Descriptive Statistics
| Metric | Value |
|---------|-------|
| Average age | 28.3 years |
| Average goals | 23.5 |
| Average assists | 7.1 |
| Average shots | 76.8 |
| Average minutes played | 2573 |
| Average yellow cards | 2.1 |
| Average red cards | 0.1 |

Players' ages range from **22** to **35** years, and their goal counts range from **16** to **36**.

---

## Correlation Analysis
- Goals and shots have a very strong positive correlation (**0.96**).
- Goals and minutes played also show a strong positive correlation (**0.89**).
- Age shows a negative correlation with both goals (**-0.60**) and shots (**-0.67**), suggesting younger players scored more and took more shots on average.

---

## Custom Rating
A custom rating was calculated for each player using the formula:

```
custom_rating = (goals * 4) + (assists * 3) + (shots * 0.5) - yellow_cards - (red_cards * 3)
```

- **Top player:** Erling Haaland with a custom rating of **212.5**

---

## Position Statistics (Average Custom Rating)
| Position | Average Goals | Average Assists | Average Custom Rating |
|-----------|---------------|----------------|----------------------|
| ST | 26.14 | 5.43 | 158.21 |
| RW | 17.50 | 13.00 | 141.75 |
| LW | 17.00 | 7.00 | 122.00 |

---

## Visualizations
Three main charts were generated:
1. **Barplot:** Total goals by position, with strikers contributing the most.
2. **Scatter plot:** Relationship between minutes played and custom rating.
3. **Heatmap:** Correlation matrix of numeric features.
