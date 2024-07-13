
import pandas as pd

def get_replacement_players_dictionary(adp_df):
    # We are going to get the last player by position in the top 100 ADP Dataframe
    # Going to look at these players projected values, which will be our replacement values
    # Then go back and look at each players projected values, subtract the replacement value
    # This gives Value Over Replacement (VOR)
    # Then sort Dataframe by VOR

    # Creating an empty dictionary that will grab values from the dataframe eventually
    replacement_players = {
        'QB': '',
        'RB': '',
        'WR': '',
        'TE': ''
    }

    # Finding replacement players by iterating over dataframe
    # iterrows lets us iterate through a dataframe, using 2 placeholder values
    # for index, row
    for _, row in adp_df.iterrows():
        position = row['Pos']
        player = row['Player']

        # If this is in the keys of the dictionary
        if position in replacement_players:
            replacement_players[position] = player

    return replacement_players
