
import pandas as pd

def get_projected_fantasypoints_dataframe():
    # Creating the datafeed and reading from a .csv file hosted on a public GitHub
    proj_df = pd.read_csv(
        'https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/BetIQ_Projected_NFL_Player_Stats_6-24-26-2026%20(2).csv')

    # Since we only care about the skill positions and our dataframe includes non, we will filter
    skill_positions = ['QB', 'WR', 'TE', 'RB']

    proj_df = proj_df.loc[proj_df['Pos'].isin(skill_positions)]

    # Our numeric values are coming up as objects, so converting
    proj_df['PassingYds'] = pd.to_numeric(proj_df['PassingYds'], errors='coerce')
    proj_df['PassingTD'] = pd.to_numeric(proj_df['PassingTD'], errors='coerce')
    proj_df['Int'] = pd.to_numeric(proj_df['Int'], errors='coerce')
    proj_df['RushingYds'] = pd.to_numeric(proj_df['RushingYds'], errors='coerce')
    proj_df['RushingTD'] = pd.to_numeric(proj_df['RushingTD'], errors='coerce')
    proj_df['Receptions'] = pd.to_numeric(proj_df['Receptions'], errors='coerce')
    proj_df['ReceivingYds'] = pd.to_numeric(proj_df['ReceivingYds'], errors='coerce')
    proj_df['ReceivingTD'] = pd.to_numeric(proj_df['ReceivingTD'], errors='coerce')

    # These are how fantasy points are weighted for PPR (Points Per Reception)
    scoring_weights = {
        'receptions': 1.0,  # PPR
        'receiving_yds': 0.1,
        'receiving_td': 6,
        'rushing_yds': 0.1,
        'rushing_td': 6,
        'passing_yds': 0.04,
        'passing_td': 4,
        'int': -2
    }

    # Doing arithmatic on stats and hosting them in a new colum called FantasyPoints

    proj_df['FantasyPoints'] = (
            proj_df['Receptions'] * scoring_weights['receptions'] + proj_df['ReceivingYds'] * scoring_weights['receiving_yds'] +
            proj_df['ReceivingTD'] * scoring_weights['receiving_td'] +
            proj_df['RushingYds'] * scoring_weights['rushing_yds'] + proj_df['RushingTD'] * scoring_weights['rushing_td'] +
            proj_df['PassingYds'] * scoring_weights['passing_yds'] + proj_df['PassingTD'] * scoring_weights['passing_td'] +
            proj_df['Int'] * scoring_weights['int'])

    return proj_df
