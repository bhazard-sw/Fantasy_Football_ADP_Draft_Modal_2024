
import pandas as pd

def get_player_VOR_dataframe(proj_df, replacement_values):

    # Now calculating the Value Over Replacement (VOR) value of each player
    # VOR: Measures player values by looking at each player's fantasy points
    # compared to the points of a “replacement player” at the same position that could be picked up off the waiver wire.
    proj_df['VOR'] = proj_df.apply(
        lambda row: row['FantasyPoints'] - replacement_values[row['Pos']], axis=1
    )

    # Sorting by VOR
    proj_df = proj_df.sort_values('VOR', ascending=False)

    # Creating a rank by VOR
    proj_df['VOR Rank'] = proj_df['VOR'].rank(ascending=False)

    # Since Pandas truncates our dataframe. I will be switching that option off
    pd.set_option('display.max_rows', None)

    # This gives info of each position based on VOR
    proj_df.groupby('Pos')['VOR'].describe()

    # Normalizing using min/max
    # Pandas does have function to do this but using logic instead
    proj_df['VOR'] = proj_df['VOR'].apply(
        lambda x: (x - proj_df['VOR'].min()) / (proj_df['VOR'].max() - proj_df['VOR'].min()))

    proj_df.head()

    return proj_df
