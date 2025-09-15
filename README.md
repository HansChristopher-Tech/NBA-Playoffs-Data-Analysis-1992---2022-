# NBA Playoff Analysis (1992–2022)

This project analyzes NBA player and team statistics from 1992 to 2022 to understand key factors contributing to championship success, focusing on **three-point shooting**, **offense vs defense**, and **star player influence**.

---

## ✅ Project Goals

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

## 📊 Results So Far

### 1. Data Cleaning
- ✅ Data cleaned and saved:  
  `C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\NBA Playoff Analysis (1992 - 2022)\csv_files\states_dataframe_clean.csv`

### 2. Three-Point Shooting
- Correlation (3PT Makes vs WS): **0.3189**
- Correlation (TS% vs 3PT%): **0.382**
- High-volume shooters:
  - Champions avg 3P%: **0.352**
  - Non-champions avg 3P%: **0.335**

### 3. Offense vs Defense
- Correlation BPM vs WS: **0.1667**
- Champions: OBPM=-0.7098, DBPM=0.9657  
- Non-champions: OBPM=-1.2543, DBPM=0.2395  
- **Defense > Offense by 1.68 → defensive edge in champions.**

### 4. Star Player Influence
- Championship Rate of Stars: **6.2%**
- Champion Stars Avg Composite: **2.548**
- Non-Champion Stars Avg Composite: **1.196**

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
