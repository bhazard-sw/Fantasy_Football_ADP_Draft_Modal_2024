
import pandas as pd
def get_adp_dataframe(cutoff):
    # Source: Underdog
    adp_df = pd.read_csv('https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/Underdog_NFL_ADP_6-26-2024.csv')

    # Generalizing the dataframe as there will be additional sources implemented in the future
    adp_df = adp_df.rename({
        'Name': 'Player',
        'Position': 'Pos',
        'Underdog': 'Current ADP'
    }, axis=1).drop('PosRk', axis=1)

    # Creating a new column in the dataframe to represent the Rank of a players ADP
    adp_df['ADP Rank'] = adp_df['Current ADP'].rank(ascending=True)

    # Wanting to cutoff the dataframe so it only consists of the top 100
    adp_df_cutoff = adp_df[:cutoff]

    return adp_df_cutoff
