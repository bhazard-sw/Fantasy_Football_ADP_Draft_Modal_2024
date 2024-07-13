# Importing the necessary packages

import seaborn as sns
import get_top_adp
import get_projected_fantasy_points_PPR
import get_replacement_players
import get_replacement_values
import get_player_VOR

# Deciding how many players we want in our ADP chart
cutoff = 100

# Getting ADP Chart
adp_df = get_top_adp.get_adp_dataframe(cutoff)

# Getting Projection Chart
proj_df = get_projected_fantasy_points_PPR.get_projected_fantasypoints_dataframe()

# Getting Replacement Players
replacement_players = get_replacement_players.get_replacement_players_dictionary(adp_df)

# Cleaning up the projection dataframe
proj_df = proj_df[['Player', 'Pos', 'Team', 'FantasyPoints']]

# Now we look for the replacement values for these players
replacement_values = get_replacement_values.get_replacement_vales_dictionary(proj_df, replacement_players)

# Creating the Value Over Replacement dataframe
vor_df = get_player_VOR.get_player_VOR_dataframe(proj_df, replacement_values)

# Box-plotting
print(sns.boxplot(x=vor_df['Pos'], y=vor_df['VOR']))

# Joining the VOR and the ADP Dataframes to then be able to look for players valued by their ADP
# Renaming columns in dataframe
vor_df = vor_df.rename({
    'VOR': 'Value',
    'VOR Rank': 'Value Rank'
}, axis=1)

# Merging now with left-join which means we are prioritizing the left dataframe
final_df = vor_df.merge(adp_df, how='left', on=['Player', 'Pos'])

# As you can see, there are duplicate team values, so we are going to drop one from one of the original dataframes
adp_df = adp_df.drop('Team', axis=1)

# Updating dataframe
# Merging now with left-join which means we are prioritizing the left dataframe
final_df = vor_df.merge(adp_df, how='left', on=['Player', 'Pos'])

# Now calculating the difference between ADP in value to find players who are over and undervalued
final_df['Diff in ADP and Value'] = final_df['ADP Rank'] - final_df['Value Rank']

# Displaying the ADP dataframe
print(adp_df)

# Getting the 'sleepers' the people with the highest diff in ADP and Value
print(final_df.sort_values(by='Diff in ADP and Value', ascending=False).head(10))

# To find the most overvalued players
print(final_df.sort_values(by='Diff in ADP and Value', ascending=True).head(10))
