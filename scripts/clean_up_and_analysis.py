"""
NBA Playoff Analysis (1992-2022)
Function Calls:
    - save_cleaned_csv() = saves the cleaned CSV file (Goal 1)
    - three_point_analysis() = exports 3-point metrics + prints correlations/insights (Goal 2A)
    - offense_vs_defense() = prints offense vs defense metrics (Goal 2B)
    - star_player_influence() = calculates composite metric & saves CSV (Goal 2C)
"""

import pandas as pd
import os
import numpy as np
from scipy.stats import zscore

# ==============================================
# 0. Setup
# ==============================================
os.system("cls" if os.name == "nt" else "clear")

# Input CSV
input_csv = r"C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\NBA Playoff Analysis (1992 - 2022)\csv_files\states_dataframe.csv"

# Output folder for all CSVs
output_folder = r"C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\NBA Playoff Analysis (1992 - 2022)\csv_files"

# Load data
df = pd.read_csv(input_csv)

# ==============================================
# 1. Data Cleaning (Goal 1)
# ==============================================
def save_cleaned_csv(df):
    """Clean the data and save to CSV"""
    # Ensure season is integer
    df["season"] = pd.to_numeric(df["season"], errors="coerce").astype("Int64")

    # Champions list (1992–2022)
    champions_list = [
        "CHI", "CHI", "HOU", "HOU", "CHI", "CHI", "CHI",
        "SAS", "LAL", "LAL", "LAL", "SAS", "DET", "SAS", "MIA",
        "SAS", "BOS", "LAL", "LAL", "DAL", "MIA", "MIA", "SAS",
        "GSW", "CLE", "GSW", "GSW", "TOR", "LAL", "MIL", "GSW"
    ]
    year_list = list(range(1992, 2023))
    champ_dict = dict(zip(year_list, champions_list))

    # Add champion flag
    df["champion"] = df.apply(
        lambda row: str(row["team_id"]).strip().upper() == champ_dict.get(int(row["season"]), None)
        if pd.notnull(row["team_id"]) and pd.notnull(row["season"]) else False,
        axis=1
    )

    # Drop rows with missing keys & keep 1992+
    df = df.dropna(subset=["team_id", "season"])
    df = df[df["season"] >= 1992]

    # Save cleaned CSV
    cleaned_csv_path = f"{output_folder}\\states_dataframe_clean.csv"
    df.to_csv(cleaned_csv_path, index=False)
    print(f"✅ Data cleaned and saved: {cleaned_csv_path}")
    return df

# ==============================================
# 2A. Three Point Shooting Analysis
# ==============================================
def three_point_analysis(df):
    """Analyze 3PT trends and save CSVs"""
    df_threes = df[["player", "season", "fg3_per_g", "fg3a_per_g", "fg3_pct", "champion"]].fillna(0)

    # League-wide yearly trends
    df_trend = (
        df_threes.groupby("season")[["fg3_per_g", "fg3a_per_g"]]
        .agg(Makes=("fg3_per_g", "sum"), Attempts=("fg3a_per_g", "sum"))
        .reset_index()
    )
    df_trend["Percentage"] = df_trend["Makes"] / df_trend["Attempts"]

    # Correlations
    correlation_makes_vs_ws = np.corrcoef(df["fg3_per_g"].fillna(0), df["ws"].fillna(0))[0,1].round(4)
    correlation_ts_vs_3p = np.corrcoef(df["ts_pct"].fillna(0), df["fg3_pct"].fillna(0))[0,1].round(4)

    # Team-level yearly efficiency
    df_team = (
        df.groupby(["season", "team_id"])
          .agg(Attempts=("fg3a_per_g", "sum"),
               Percentage=("fg3_pct", "mean"),
               Champion=("champion", "max"))
          .reset_index()
    )

    # High-volume shooters
    attempt_threshold = df_threes["fg3a_per_g"].median()
    df_high_volume = df_threes[df_threes["fg3a_per_g"] > attempt_threshold]
    avg_champ_pct = df_high_volume[df_high_volume["champion"] == 1]["fg3_pct"].mean().round(3)
    avg_non_champ_pct = df_high_volume[df_high_volume["champion"] == 0]["fg3_pct"].mean().round(3)

    # Save CSVs
    df_threes.to_csv(f"{output_folder}\\three_point_data.csv", index=False)
    df_trend.to_csv(f"{output_folder}\\three_point_trend_team.csv", index=False)
    df_team.to_csv(f"{output_folder}\\yearly_team_3pt_pct_champions.csv", index=False)

    print("✅ 3PT CSV files saved!")
    print(f"Correlation (3PT Makes vs WS): {correlation_makes_vs_ws}")
    print(f"Correlation (TS% vs 3PT%): {correlation_ts_vs_3p}")
    print(f"High-volume shooters (champ avg 3P%): {avg_champ_pct}")
    print(f"High-volume shooters (non-champ avg 3P%): {avg_non_champ_pct}")

# ==============================================
# 2B. Offense vs Defense Analysis
# ==============================================
def offense_vs_defense(df):
    """Compare OBPM vs DBPM and BPM vs WS correlations"""
    cor = np.corrcoef(df["bpm"].fillna(0), df["ws"].fillna(0))[0,1].round(4)
    champ = df[df["champion"] == True]
    non_champ = df[df["champion"] == False]

    champ_obpm, champ_dbpm = champ["obpm"].mean().round(4), champ["dbpm"].mean().round(4)
    non_champ_obpm, non_champ_dbpm = non_champ["obpm"].mean().round(4), non_champ["dbpm"].mean().round(4)

    print(f"Correlation BPM vs WS: {cor}")
    print(f"Champ OBPM={champ_obpm}, DBPM={champ_dbpm}")
    print(f"Non-Champ OBPM={non_champ_obpm}, DBPM={non_champ_dbpm}")
    
    if champ_dbpm > champ_obpm:
        print(f"Defense > Offense by {champ_dbpm - champ_obpm:.2f} → defensive edge in champions.")
    elif champ_obpm > champ_dbpm:
        print(f"Offense > Defense by {champ_obpm - champ_dbpm:.2f} → offensive edge in champions.")
    else:
        print("Balanced OBPM and DBPM → both matter equally.")

# ==============================================
# 2C. Star Player Influence
# ==============================================
def star_player_influence(df):
    """Compute composite metric (PER, BPM, WS) for top player per team/season"""
    df_star = df[["season", "team_id", "player", "mp_per_g", "per", "bpm", "ws", "champion"]].dropna()
    df_star["per_z"] = zscore(df_star["per"])
    df_star["bpm_z"] = zscore(df_star["bpm"])
    df_star["ws_z"] = zscore(df_star["ws"])
    df_star["Composite"] = df_star[["per_z", "bpm_z", "ws_z"]].mean(axis=1)

    # Top player per team/season

    df_star_top = (
        df_star
            .sort_values(["season", "team_id", "Composite"], ascending=[True, True, False])
            .groupby(["season", "team_id"])
            .head(1)
            .reset_index(drop=True)
    )


    champ_stars = df_star_top[df_star_top["champion"] == 1]
    non_champ_stars = df_star_top[df_star_top["champion"] == 0]

    championship_rate = round(len(champ_stars) / len(df_star_top), 3)
    avg_champ_composite = champ_stars["Composite"].mean().round(3)
    avg_non_champ_composite = non_champ_stars["Composite"].mean().round(3)

    # Save CSV
    df_star_top.to_csv(f"{output_folder}\\star_player_influence.csv", index=False)
    print("✅ Star Player Influence CSV saved!")
    print(f"Championship Rate of Stars: {championship_rate*100}%")
    print(f"Champion Stars Avg Composite: {avg_champ_composite}")
    print(f"Non-Champion Stars Avg Composite: {avg_non_champ_composite}")

# ==============================================
# === Run Analyses ===
# ==============================================
df = save_cleaned_csv(df)
print('-'*50)
three_point_analysis(df)
print('-'*50)
offense_vs_defense(df)
print('-'*50)
star_player_influence(df)
