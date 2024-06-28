Fantasy Football ADP DataFrame
This script creates a DataFrame of ranked top Average Draft Pick (ADP) values for fantasy football players. It currently sources data from Underdog and is designed to be extensible for additional sources in the future.

Function: get_adp_dataframe
Purpose
The get_adp_dataframe function reads ADP data from a CSV file, processes it, and returns a DataFrame containing the top players based on their ADP rank.

Parameters
cutoff (int): The number of top players to include in the returned DataFrame.
Function Workflow
Load Data:

The function reads a CSV file from a specified URL (currently sourcing from Underdog).
DataFrame Generalization:

Renames columns to maintain consistency and readability:
'Name' to 'Player'
'Position' to 'Pos'
'Underdog' to 'Current ADP'
Drops the 'PosRk' column as it is not required for the current analysis.
ADP Ranking:

Adds a new column 'ADP Rank' to represent the rank of each player's ADP value in ascending order.
DataFrame Cutoff:

Slices the DataFrame to include only the top players up to the specified cutoff.
Return:

Returns the processed and sliced DataFrame.



----------------------------------------------------------------------------------------------------------------------------------------


Fantasy Football Projected Fantasy Points DataFrame
This script processes projected fantasy football player statistics from a CSV file and calculates their projected fantasy points based on a specific scoring system. It focuses on skill positions (QB, WR, TE, RB).

Function: get_projected_fantasypoints_dataframe
Purpose
The get_projected_fantasypoints_dataframe function reads player statistics from a CSV file, filters for skill positions, converts relevant columns to numeric types, calculates projected fantasy points, and returns the processed DataFrame.

Parameters
This function does not take any parameters.

Function Workflow
Load Data:

Reads a CSV file from a specified URL (sourcing from BetIQ).
Filter Skill Positions:

Filters the DataFrame to include only the skill positions: QB, WR, TE, and RB.
Display Initial Data:

Prints the initial rows of the DataFrame and sets display options to show more rows and columns.
Convert Data Types:

Converts relevant columns to numeric types to ensure accurate calculations:
'PassingYds'
'PassingTD'
'Int'
'RushingYds'
'RushingTD'
'Receptions'
'ReceivingYds'
'ReceivingTD'
Define Scoring Weights:

Defines the scoring system for calculating fantasy points:
1 point per reception (PPR)
0.1 points per receiving yard
6 points per receiving touchdown
0.1 points per rushing yard
6 points per rushing touchdown
0.04 points per passing yard
4 points per passing touchdown
-2 points per interception
Calculate Fantasy Points:

Performs arithmetic operations on the stats to calculate the projected fantasy points and stores them in a new column 'FantasyPoints'.
Display Processed Data:

Prints the processed DataFrame.
Return:

Returns the processed DataFrame.


-------------------------------------------------------------------------------------------------------------------
