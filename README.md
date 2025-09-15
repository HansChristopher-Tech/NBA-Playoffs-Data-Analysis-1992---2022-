# NBA Playoff Analysis (1992–2022)

This project analyzes NBA player and team statistics from 1992 to 2022 to understand key factors contributing to championship success, focusing on **three-point shooting**, **offense vs defense**, and **star player influence**.

🔗**Kaggle Dataset Link**: https://www.kaggle.com/datasets/robertsunderhaft/nba-playoffs

---

## ✅ Project Goals

## Project Goals

1. **Data Cleaning (Goal 1)**
   - Standardize and clean the raw dataset.
   - Add a championship flag for each player based on their team's success in a given season.
   - Save cleaned data for further analysis.

2. **Three-Point Shooting Analysis (Goal 2A)**
   - Track league-wide 3-point trends (attempts, makes, percentage) over seasons.
   - Explore correlation between 3-point production and team wins.
   - Compare high-volume shooters on championship vs. non-championship teams.

3. **Offense vs Defense Analysis (Goal 2B)**
   - Investigate the relationship between Box Plus-Minus (BPM) and Win Shares (WS).
   - Compare Offensive BPM (OBPM) vs Defensive BPM (DBPM) for champions vs non-champions.
   - Identify which side of the game contributes more to winning titles.

4. **Star Player Influence (Goal 2C)**
   - Create a **composite performance metric** (average of PER, BPM, WS) to rank players per season.
   - Ensure only one top player per team per season is considered.
   - Compare how often these top players won championships and their average performance.

5. **Data Visualization Goals**
   - **3-Point Shooting Trends:** Line charts showing league-wide and team-level 3PT makes, attempts, and percentages over the years.
   - **3PT vs Team Success:** Scatter plots to visualize the correlation between 3PT makes and Win Shares.
   - **True Shooting % vs 3PT %:** Scatter plots to explore relationships between efficiency metrics.
   - **Offense vs Defense:** Bar or boxplots comparing OBPM and DBPM for championship vs non-championship teams.
   - **Star Player Influence:** Heatmaps or radar charts showing top players’ composite scores (PER, BPM, WS) across seasons.
   - **High-Volume Shooters:** Comparative charts to highlight shooting efficiency of championship vs non-championship players.

---

## 📂 Files Generated

| File | Description |
|------|-------------|
| `states_dataframe_clean.csv` | Cleaned master dataset for 1992–2022 |
| `three_point_data.csv` | Player-level 3PT stats |
| `three_point_trend_team.csv` | League-wide 3PT trends per season |
| `yearly_team_3pt_pct_champions.csv` | Team-level 3PT efficiency per season |
| `star_player_influence.csv` | Top player composite metric per team/season |

---
## Results So Far

### 1. Data Cleaning
✅ **Cleaned Data Saved:** [states_dataframe_clean.csv](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/tree/master/csv_files/states_dataframe_clean.csv)

**Function Used:**
```python
def save_cleaned_csv():
    df.to_csv("csv_files/states_dataframe_clean.csv", index=False)
    print("✅ Data cleaned and saved successfully!")
````

---

### 2. Three-Point Shooting Analysis

✅ **3PT CSV Files Saved:**

* [three\_point\_data.csv](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/tree/master/csv_files/three_point_data.csv)
* [three\_point\_trend\_team.csv](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/tree/master/csv_files/three_point_trend_team.csv)
* [yearly\_team\_3pt\_pct\_champions.csv](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/tree/master/csv_files/yearly_team_3pt_pct_champions.csv)

**Key Metrics:**

* Correlation (3PT Makes vs WS): 0.3189
* Correlation (TS% vs 3PT%): 0.382
* High-volume shooters (Champions avg 3P%): 0.352
* High-volume shooters (Non-Champions avg 3P%): 0.335

**Function Used:**

```python
def print_three_point_csv():
    df_threes.to_csv("csv_files/three_point_data.csv", index=False)
    df_threes_trend_team.to_csv("csv_files/three_point_trend_team.csv", index=False)
    df_grouper_efficiency.to_csv("csv_files/yearly_team_3pt_pct_champions.csv", index=False)
    print("✅ 3PT CSV files saved!")
```

---

### 3. Offense vs Defense Analysis

**Key Metrics:**

* Correlation BPM vs WS: 0.1667
* Championship OBPM = -0.7098, DBPM = 0.9657
* Non-Championship OBPM = -1.2543, DBPM = 0.2395
* **Observation:** Defense > Offense by 1.68 → defensive edge in champions

**Function Used:**

```python
def offense_vs_defense():
    print(f"Correlation between BPM and WS (player-level): {cor}")
    print(f"Championship OBPM={champ_obpm}, DBPM={champ_dbpm}")
    print(f"Non-Championship OBPM={non_champ_obpm}, DBPM={non_champ_dbpm}")
```

---

### 4. Star Player Influence

✅ **Star Player Influence CSV Saved:** [star\_player\_influence.csv](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/tree/master/csv_files/star_player_influence.csv)

**Key Metrics:**

* Championship Rate of Stars: 6.2%
* Champion Stars Avg Composite: 2.548
* Non-Champion Stars Avg Composite: 1.196

**Function Used:**

```python
def star_influence_csv():
    df_star_top.to_csv("csv_files/star_player_influence.csv", index=False)
    print("✅ Star Player Influence CSV saved!")
    print(f"Championship Rate of Stars: {championship_rate*100}%")
    print(f"Champion Stars Avg Composite: {avg_champ_composite}")
    print(f"Non-Champion Stars Avg Composite: {avg_non_champ_composite}")
```
---
## 📈 Next Steps

- Create **Power BI dashboards** to visualize:
  - 3PT trends over time.
  - BPM vs WS scatterplots.
  - Composite star player metrics across seasons.
- Conduct **hypothesis testing** (t-tests) to quantify statistical differences between champions and non-champions.
- Optional: Explore predictive modeling for championship likelihood based on player/team metrics.

---

## ⚡ Summary

- **3-point shooting** shows moderate correlation with team success.  
- **Defensive impact** (DBPM) appears more influential than offensive metrics for champions.  
- **Top players** (composite metric) strongly outperform non-champions, but championship rate of stars is relatively low (6.2%).  

This project highlights key trends in NBA performance and sets the stage for interactive dashboards and further analysis.
