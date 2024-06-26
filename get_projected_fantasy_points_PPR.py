# Importing Pandas for use of Dataframes
import pandas as pd

# Creating the datafeed and reading from a .csv file hosted on a public GitHub
df = pd.read_csv('https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/BetIQ_Projected_NFL_Player_Stats_6-24-26-2026%20(2).csv')

# Making sure the dataframe is working
print(df.head())

print(df.info())

# Since we only care about the skill positions and our dataframe includes non, we will filter
skill_positions = ['QB', 'WR', 'TE', 'RB']

df = df.loc[df['Pos'].isin(skill_positions)]

print(df.head())
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
print(df)

# Our numeric values are coming up as objects, so converting
df['PassingYds'] = pd.to_numeric(df['PassingYds'], errors='coerce')
df['PassingTD'] = pd.to_numeric(df['PassingTD'], errors='coerce')
df['Int'] = pd.to_numeric(df['Int'], errors='coerce')
df['RushingYds'] = pd.to_numeric(df['RushingYds'], errors='coerce')
df['RushingTD'] = pd.to_numeric(df['RushingTD'], errors='coerce')
df['Receptions'] = pd.to_numeric(df['Receptions'], errors='coerce')
df['ReceivingYds'] = pd.to_numeric(df['ReceivingYds'], errors='coerce')
df['ReceivingTD'] = pd.to_numeric(df['ReceivingTD'], errors='coerce')
print(df.dtypes)

scoring_weights = {
    'receptions': 1.0, # PPR
    'receiving_yds': 0.1,
    'receiving_td': 6,
    'rushing_yds': 0.1,
    'rushing_td': 6,
    'passing_yds': 0.04,
    'passing_td': 4,
    'int': -2
}

# Doing arithmatic on stats and hosting them in a new colum called FantasyPoints

df['FantasyPoints'] = (
    df['Receptions']*scoring_weights['receptions'] + df['ReceivingYds']*scoring_weights['receiving_yds'] +
    df['ReceivingTD']*scoring_weights['receiving_td'] +
    df['RushingYds']*scoring_weights['rushing_yds'] + df['RushingTD']*scoring_weights['rushing_td'] +
    df['PassingYds']*scoring_weights['passing_yds'] + df['PassingTD']*scoring_weights['passing_td'] +
    df['Int']*scoring_weights['int'])

print(df.head())