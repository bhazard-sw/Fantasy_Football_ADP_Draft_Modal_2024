import pandas as pd

def get_replacement_vales_dictionary(proj_df, replacement_players):
    # Substantiating an empty dictionary
    replacement_values = {}

    # Since dictionaries are inherently not iterable, this is method to iterate
    for position, player_name in replacement_players.items():
        player = proj_df.loc[proj_df['Player'] == player_name]

        # Converting this new series object into a list object and 'flattening' it
        replacement_value = player['FantasyPoints'].tolist()[0]

        # Matching positions to their replacement value
        replacement_values[position] = replacement_value

    return replacement_values
