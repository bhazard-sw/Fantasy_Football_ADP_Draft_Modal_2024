######################################################################################################################
# Importing Pandas for use of Dataframes
import pandas as pd

# Creating the datafeed and reading from a .csv file hosted on a public GitHub
adp_df = pd.read_csv('https://raw.githubusercontent.com/bhazard-sw/Fantasy_Football_ADP_Draft_Modal_2024/main/Underdog_NFL_ADP_6-26-2024.csv')

# Making sure the dataframe is working
print(adp_df.head())

# Cleaning up this Dataframe to be an ideally formatted dataframe

adp_df = adp_df.rename({
    'Name': 'Player',
    'Position': 'Pos',
    'Underdog': 'Current ADP'
}, axis=1).drop('PosRk', axis=1)


# Creating a new column in the dataframe to represent the Rank of a players ADP
adp_df['ADP Rank'] = adp_df['Current ADP'].rank(ascending=True)

# Wanting to cutoff the dataframe so it only consists of the top 100
adp_df_cutoff = adp_df[:100]

print(adp_df_cutoff.head())


# THIS IS WHERE I WOULD CALL THE ADP RANKED DATAFRAME
######################################################################################################################

# We are going to get the last player by position in the top 100 ADP Dataframe
# Going to look at these players projected values, which will be our replacement values
# Then go back and look at each players projected values, subtract the replacement value
# This gives Value Over Replacement (VOR)
# Then sort Dataframe by VOR

# Creating an empty dictionary that will grab values from the dataframe eventually
replacement_players = {
    'QB':'',
    'RB':'',
    'WR':'',
    'TE':''
}

# Finding replacement players by iterating over dataframe
# iterrows lets us iterate through a dataframe, using 2 placeholder values
# for index, row
for _,row in adp_df_cutoff.iterrows():
  position = row['Pos']
  player = row['Player']

# If this is in the keys of the dictionary
  if position in replacement_players:
    replacement_players[position] = player

print(replacement_players)


######################################################################################################################
# Scaling stats to get total Fantasy Points

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



# THIS IS WHERE WE WOULD CALL THE GET POJECTED FANTASY POINTS
##############################################################################################################

# Next, replace the replacement players with replacement values; their projected points

# First, take out the unecessary columns
df = df[['Player','Pos','Team','FantasyPoints']]

df.head()

# Now we look for the replacement values for these players

# Sustantiating an empty dictionary
replacement_values = {}

# Since dictionaries are inhenerently not itterable, this is method to iterate
for position, player_name in replacement_players.items():
  player = df.loc[df['Player'] == player_name]

  # Converting this new series object into a list object and 'flattening' it
  replacement_value = player['FantasyPoints'].tolist()[0]

  # Updating
  replacement_values[position] = replacement_value


# Printing values
print(replacement_values)

# replacement_values is not a dictionary with postion as keys and the values as their replacement value

# Now calculating the VOR value of each player
# What is Value Over Replacement Player (VORP) Rankings? VORP measures player values by looking at each player's fantasy points
# compared to the points of a “replacement player” at the same position that could be picked up off the waiver wire.

# Lamda is an anonymous function
# Apply is applying this function across every row in the dataframe
# The function below is taking a row. Then accessing the FantasyPoints value for each row, while accessing the Pos value each row
# and using Dictionary Indexing to look in the replacement_values.
# It is taking a players FantasyPoints and subtracting the replacement values from it
# The access=1 allows us to go through the entire dataframe. If it's not included, it only lets us go through a Series object
df['VOR'] = df.apply(
    lambda row: row['FantasyPoints'] - replacement_values[row['Pos']], axis=1
)

df.head()


# Sorting by VOR
df = df.sort_values('VOR', ascending=False)

df.head()

# Creating a rank by VOR

df['VOR Rank'] = df['VOR'].rank(ascending=False)

df.head()

df.head(100)

# Since Pandas truncates our dataframe. I will be switching that option off
pd.set_option('display.max_rows',None)

df.head(100)

# Groupby method: Lets us create Pivot Tables
# This will give you info of each position based on VOR
df.groupby('Pos')['VOR'].describe()

# Judging by the above data, you can tell RBs are the most valuable by the mean, QBs are the lease
# Note the TE might be slightly higher than WR because of Kelce


# Normalizing our data: The process of rescaling numerical data to a common scale
# Two forms of normalization mention: min/max normalization and z-score normalization
# We are using the min/max normalization which scales things between 0 and 1
# Subrtract minimum value from each data point and then divide by the range

# Pandas does have function to do this but here is the logic for it instead
df['VOR'] = df['VOR'].apply(lambda x: (x-df['VOR'].min())/(df['VOR'].max() - df['VOR'].min()))

df.head()

import seaborn as sns

# Box-plotting
sns.boxplot(x=df['Pos'], y=df['VOR'])

# Joinging the VOR and the ADP Dataframes to then be able to look for players unvalued by their ADP

# Renaming columns in dataframe
df = df.rename({
    'VOR': 'Value',
    'VOR Rank': 'Value Rank'
}, axis=1)

df.head()

adp_df.head()

# Merging the dataframes

# First have to replace some values as the two dataframes come from two different sources so the player names are different
df['Player'] = df['Player'].replace({
    'Kenneth Walker III': 'Kenneth Walker',
    'Travis Etienne Jr.': 'Travis Etienne',
    'Brian Robinson Jr.': 'Brian Robinson',
    'Pierre Strong Jr.': 'Pierre Strong',
    'Michael Pittman Jr.': 'Michael Pittman',
    'A.J. Dillon': 'AJ Dillon',
    'D.J. Moore': 'DJ Moore'
})

# Merging now with left-join which means we are prioritzing the left dataframe
final_df= df.merge(adp_df, how='left', on=['Player', 'Pos'])

final_df.head(10)

# As you can see, there are duplicate team values, so we are goingto drop one from one of the original dataframes
adp_df = adp_df.drop('Team', axis=1)

adp_df.head()

# Updating dataframe
# Merging now with left-join which means we are prioritzing the left dataframe
final_df= df.merge(adp_df, how='left', on=['Player', 'Pos'])

final_df.head(10)

# Now calculating the difference between ADP in value to find players who are over and under valued
final_df['Diff in ADP and Value'] = final_df['ADP Rank'] - final_df['Value Rank']

final_df.head()

# Getting the 'sleepers' the people with the highest diff in ADP and Value
final_df.sort_values(by='Diff in ADP and Value', ascending=False).head(10)

# To find the most overvalued players
final_df.sort_values(by='Diff in ADP and Value', ascending=True).head(10)

