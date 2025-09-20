

# 🏀 NBA Playoff Analysis (1992–2022)

This project analyzes **NBA player and team statistics (1992–2022)** to identify the factors that contribute most to winning championships. The analysis focuses on:

* **Three-point shooting**
* **Offense vs. defense balance**
* **Star player influence**

🔗 **Dataset:** [NBA Playoffs Dataset (Kaggle)](https://www.kaggle.com/datasets/robertsunderhaft/nba-playoffs)

---

## 🎯 Project Goals

1. **Data Cleaning**

   * Standardize and clean raw data.
   * Add a championship flag per player (based on team success each season).
   * Export a cleaned dataset for further analysis.

2. **Three-Point Shooting**

   * Track league-wide 3PT attempts, makes, and percentages across seasons.
   * Correlate 3PT production with team win shares.
   * Compare volume shooters from champion vs. non-champion teams.

3. **Offense vs. Defense**

   * Study correlation between Box Plus-Minus (BPM) and Win Shares (WS).
   * Compare Offensive BPM (OBPM) vs. Defensive BPM (DBPM).
   * Evaluate which side of the game contributes more to championships.

4. **Star Player Influence**

   * Create a **composite performance metric** (average of PER, BPM, WS).
   * Select the **top player per team per season** based on minutes & impact.
   * Compare championship rates and performance gaps between stars on champions vs. non-champions.

5. **Data Visualization**

   * **3PT Trends:** Line charts for league & team shooting growth.
   * **3PT vs. Team Success:** Scatter plots (3PT Makes vs. WS).
   * **Efficiency:** TS% vs. 3PT%.
   * **Offense vs. Defense:** Bar/boxplots of OBPM & DBPM (champs vs. non-champs).
   * **Star Influence:** Heatmap/matrix of top players’ composite scores.
   * **High-Volume Shooters:** Champion vs. non-champion comparisons.

---

## 📂 Generated Files

| File                                | Description                        |
| ----------------------------------- | ---------------------------------- |
| `states_dataframe_clean.csv`        | Cleaned master dataset (1992–2022) |
| `three_point_data.csv`              | Player-level 3PT stats             |
| `three_point_trend_team.csv`        | League-wide 3PT trends per season  |
| `yearly_team_3pt_pct_champions.csv` | Team-level 3PT efficiency          |
| `star_player_influence.csv`         | Top player composite metrics       |

---

## 📊 Results

### 1. Data Cleaning

✅ **Cleaned dataset saved:** [`states_dataframe_clean.csv`](csv_files/states_dataframe_clean.csv)

```python
def save_cleaned_csv():
    df.to_csv("csv_files/states_dataframe_clean.csv", index=False)
    print("✅ Data cleaned and saved successfully!")
```

---

### 2. Three-Point Shooting

✅ **Saved CSVs:**

* [`three_point_data.csv`](csv_files/three_point_data.csv)
* [`three_point_trend_team.csv`](csv_files/three_point_trend_team.csv)
* [`yearly_team_3pt_pct_champions.csv`](csv_files/yearly_team_3pt_pct_champions.csv)

**Findings:**

* Correlation (3PT Makes vs. WS): **0.319**
* Correlation (TS% vs. 3PT%): **0.382**
* Avg 3PT%: Champions = **35.2%**, Non-Champions = **33.5%**

📈 **Graph:** ![3PT Shooting Trends](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/blob/master/charts/3PT_Trends.png?raw=true)
*Three-point attempts increased steadily, peaking around 2020, with league averages \~32%.*

---

### 3. Offense vs. Defense

**Findings:**

* Correlation (BPM vs. WS): **0.167**
* Champions → OBPM = **-0.71**, DBPM = **0.97**
* Non-Champions → OBPM = **-1.25**, DBPM = **0.24**
* **Observation:** Champions gained a **defensive edge** (DBPM advantage of \~1.68).

📈 **Graphs:**

![Offense vs Defense (Champs)](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/blob/master/charts/Offense_vs_Defense_Champs.png?raw=true)  
![Offense vs Defense (Non-Champs)](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/blob/master/charts/Offense_vs_Defense_Non-Champs.png?raw=true)


---

### 4. Star Player Influence

✅ **Saved CSV:** [`star_player_influence.csv`](csv_files/star_player_influence.csv)

**Findings:**

* Championship Rate of Stars: **6.2%**
* Avg Composite Score → Champs = **2.55**, Non-Champs = **1.20**

📈 **Graphs:**

![TS% vs. 3PT%](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/blob/master/charts/TSvs3PT.png?raw=true) → Guards & modern shooters dominate; Ray Allen as outlier (70% TS, >50% 3PT).  

![3PT Makes vs. Win Shares](https://github.com/HansChristopher-Tech/NBA-Playoffs-Data-Analysis-1992---2022-/blob/master/charts/WSvs3PT_Makes.png?raw=true) → Weak overall correlation; only outliers like LeBron show strong efficiency despite low 3PT volume.


---

## 📊 Dashboard

* 📄 [Dashboard (PDF)](Output%20Dashboard/NBA_Playoff%20Dashboard.pdf)
* 📂 [Dashboard (PBIX)](Output%20Dashboard/NBA_Playoff%20Dashboard.pbix)

The dashboard includes:

* Championship filters
* 3PT & efficiency charts
* OBPM vs DBPM scatter plots
* Star player composite performance visuals

---

## ⚡ Summary

* **3PT shooting** moderately correlates with team success, but not strongly across eras.
* **Defense (DBPM)** is more influential than offense for championship teams.
* **Star players** perform far better than non-stars, but their **championship conversion rate is low (6.2%)**, showing team depth and defense remain crucial.

This project highlights the evolving role of **3PT shooting, defensive impact, and star dominance** in the NBA playoffs over 30 years.

---

👉 Much cleaner, with consistent formatting, easy-to-read metrics, and direct graph links.


