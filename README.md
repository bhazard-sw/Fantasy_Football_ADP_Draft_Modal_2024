
# Fantasy Football Value Over Replacement (VOR) Analysis

## Overview

This project is a comprehensive Draft Package for fantasy football enthusiasts. It includes tools to analyze player data and make informed drafting decisions. Key features of the package include:

- **ADP Chart:** Provides insights into Average Draft Positions (ADP) for players.
- **VOR Chart:** Calculates and visualizes Value Over Replacement (VOR) to identify player value.
- **Sleeper Players:** Highlights players with potential undervaluation based on ADP and VOR analysis.
- **Overvalued Players:** Identifies players who may be drafted too early based on their ADP and VOR rankings.

By utilizing these tools, fantasy football managers can optimize their draft strategies and build competitive teams.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [get_top_adp.py](#get_top_adppy)
  - [get_projected_fantasy_points_PPR.py](#get_projected_fantasy_points_pprpy)
  - [get_replacement_players.py](#get_replacement_playerspy)
  - [get_replacement_values.py](#get_replacement_valuespy)
  - [get_player_VOR.py](#get_player_vorpy)
- [Data Sources](#data-sources)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/fantasy-football-vor.git
   ```

2. Install the required packages:

   ```sh
   pip install -r pandas
   pip install -r seaborn
   ```

## Usage

1. Ensure you have the necessary CSV files from the specified data sources.

2. Run the `main.py` script to execute the analysis:

   ```sh
   python main.py
   ```

## Functions

### get_top_adp.py

- **Function:** `get_adp_dataframe(cutoff)`
- **Purpose:** Fetches and processes the Average Draft Position (ADP) data from a specified CSV file. The ADP data is then ranked and truncated to the top players based on the cutoff value.

### get_projected_fantasy_points_PPR.py

- **Function:** `get_projected_fantasypoints_dataframe()`
- **Purpose:** Fetches and processes projected fantasy points data for skill positions (QB, WR, TE, RB) from a specified CSV file. Calculates fantasy points using PPR (Points Per Reception) scoring.

### get_replacement_players.py

- **Function:** `get_replacement_players_dictionary(adp_df)`
- **Purpose:** Identifies the replacement players for each position from the ADP data, representing the lowest-ranked player in the top 100.

### get_replacement_values.py

- **Function:** `get_replacement_vales_dictionary(proj_df, replacement_players)`
- **Purpose:** Calculates the fantasy points for each replacement player, creating a dictionary of replacement values by position.

### get_player_VOR.py

- **Function:** `get_player_VOR_dataframe(proj_df, replacement_values)`
- **Purpose:** Calculates the Value Over Replacement (VOR) for each player and ranks them accordingly. Normalizes the VOR values and provides descriptive statistics.

## Data Sources

- **ADP Data:** [Underdog NFL ADP](https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/Underdog_NFL_ADP_6-26-2024.csv)
- **Projected Fantasy Points:** [BetIQ Projected NFL Player Stats](https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/BetIQ_Projected_NFL_Player_Stats_6-24-26-2026%20(2).csv)
