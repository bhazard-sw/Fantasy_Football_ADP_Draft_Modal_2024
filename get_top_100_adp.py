# Importing Pandas for use of Dataframes
import pandas as pd

# Creating the datafeed and reading from a .csv file hosted on a public GitHub
adp_df = pd.read_csv('https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/Underdog_NFL_ADP_6-26-2024.csv')

# Making sure the dataframe is working
print(adp_df.head())

# Cleaning up this Dataframe to be an ideally formatted dataframe

adp_df = adp_df.rename({
    'Name':'Player',
    'Position': 'Pos',
    'Underdog': 'Current ADP'
}, axis=1).drop('PosRk', axis=1)

# Making sure it is newly formatted
print(adp_df.head())

# Creating a new column in the dataframe to represent the Rank of a players ADP
adp_df['ADP Rank'] = adp_df['Current ADP'].rank(ascending=True)

# Wanting to cutoff the dataframe so it only consists of the top 100
adp_df_cutoff = adp_df[:100]

print(adp_df_cutoff)