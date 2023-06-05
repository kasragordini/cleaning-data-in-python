# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:41:14 2023

@author: Kasra
"""


''''
Cleaning Data in Python


Data type constraints

Numeric data or ... ?
In this exercise, and throughout this chapter, you'll be working with bicycle ride sharing data in San Francisco called ride_sharing. It contains information on the start and end stations, the trip duration, and some user information for a bike sharing service.
The user_type column contains information on whether a user is taking a free ride and takes on the following values:
•	1 for free riders.
•	2 for pay per ride.
•	3 for monthly subscribers.
In this instance, you will print the information of ride_sharing using .info() and see a firsthand example of how an incorrect data type can flaw your analysis of the dataset. The pandas package is imported as pd.
Instructions 1/3
•	Print the information of ride_sharing.
•	Use .describe() to print the summary statistics of the user_type column from ride_sharing.

•	# Print the information of ride_sharing
•	print(ride_sharing.info())
•	
•	# Print summary statistics of user_type column
•	print(ride_sharing['user_type'].describe())


Instructions 2/3
Question
By looking at the summary statistics - they don't really seem to offer much description on how users are distributed along their purchase type, why do you think that is?
Possible answers
 
The user_type column is not of the correct type, it should be converted to str.
 
The user_type column has an infinite set of possible values, it should be converted to category.
 
The user_type column has an finite set of possible values that represent groupings of data, it should be converted to category.

Instructions 3/3
•	Convert user_type into categorical by assigning it the 'category' data type and store it in the user_type_cat column.
•	Make sure you converted user_type_cat correctly by using an assert statement.###
''''

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())

''''
Summing strings and concatenating numbers
In the previous exercise, you were able to identify that category is the correct data type for user_type and convert it in order to extract relevant statistical summaries that shed light on the distribution of user_type.
Another common data type problem is importing what should be numerical values as strings, as mathematical operations such as summing and multiplication lead to string concatenation, not numerical outputs.
In this exercise, you'll be converting the string column duration to the type int. Before that however, you will need to make sure to strip "minutes" from the column in order to make sure pandas reads it as numerical. The pandas package has been imported as pd.
Instructions
•	Use the .strip() method to strip duration of "minutes" and store it in the duration_trim column.
•	Convert duration_trim to int and store it in the duration_time column.
•	Write an assert statement that checks if duration_time's data type is now an int.
•	Print the average ride duration.
''''

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())


''''
Data range constraints

         duration  station_A_id                                     station_A_name  station_B_id                                 station_B_name  bike_id   user_type  user_birth_year user_gender  \
0      12 minutes            81                                 Berry St at 4th St           323                             Broadway at Kearny     5480  Subscriber             1959        Male   
1      24 minutes             3       Powell St BART Station (Market St at 4th St)           118                Eureka Valley Recreation Center     5193  Subscriber             1965        Male   
2       8 minutes            67  San Francisco Caltrain Station 2  (Townsend St...            23                  The Embarcadero at Steuart St     3652  Subscriber             1993        Male   
3       4 minutes            16                            Steuart St at Market St            28                   The Embarcadero at Bryant St     1883  Subscriber             1979        Male   
4      11 minutes            22                              Howard St at Beale St           350                           8th St at Brannan St     4626  Subscriber             1994        Male   
...           ...           ...                                                ...           ...                                            ...      ...         ...              ...         ...   
25755  11 minutes            15  San Francisco Ferry Building (Harry Bridges Pl...            34                 Father Alfred E Boeddeker Park     5063  Subscriber             2000        Male   
25756  10 minutes            15  San Francisco Ferry Building (Harry Bridges Pl...            34                 Father Alfred E Boeddeker Park     5411  Subscriber             1998        Male   
25757  14 minutes            15  San Francisco Ferry Building (Harry Bridges Pl...            42  San Francisco City Hall (Polk St at Grove St)     5157    Customer             1995        Male   
25758  14 minutes            15  San Francisco Ferry Building (Harry Bridges Pl...            42  San Francisco City Hall (Polk St at Grove St)     4438    Customer             1995        Male   
25759  29 minutes            16                            Steuart St at Market St           115                             Jackson Playground     1705    Customer             1990        Male   

      tire_sizes  
0           27.0  
1           26.0  
2           26.0  
3           29.0  
4           27.0  
...          ...  
25755       29.0  
25756       26.0  
25757       29.0  
25758       26.0  
25759       27.0  

[25760 rows x 10 columns]

Tire size constraints
In this lesson, you're going to build on top of the work you've been doing with the ride_sharing DataFrame. You'll be working with the tire_sizes column which contains data on each bike's tire size.
Bicycle tire sizes could be either 26″, 27″ or 29″ and are here correctly stored as a categorical value. In an effort to cut maintenance costs, the ride sharing provider decided to set the maximum tire size to be 27″.
In this exercise, you will make sure the tire_sizes column has the correct range by first converting it to an integer, then setting and testing the new upper limit of 27″ for tire sizes.
Instructions
•	Convert the tire_sizes column from category to 'int'.
•	Use .loc[] to set all values of tire_sizes above 27 to 27.
•	Reconvert back tire_sizes to 'category' from int.
•	Print the description of the tire_sizes.
''''

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')
	
# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')
	
# Print tire size description
print(ride_sharing['tire_sizes'].describe())

''''
Back to the future
A new update to the data pipeline feeding into the ride_sharing DataFrame has been updated to register each ride's date. This information is stored in the ride_date column of the type object, which represents strings in pandas.
A bug was discovered which was relaying rides taken today as taken next year. To fix this, you will find all instances of the ride_date column that occur anytime in the future, and set the maximum possible value of this column to today's date. Before doing so, you would need to convert ride_date to a datetime object.
The datetime package has been imported as dt, alongside all the packages you've been using till now.
Instructions
•	Convert ride_date to a datetime object using to_datetime(), then convert the datetime object into a date and store it in ride_dt column.
•	Create the variable today, which stores today's date by using the dt.date.today() function.
•	For all instances of ride_dt in the future, set them to today's date.
•	Print the maximum date in the ride_dt column.
''''



# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

''''
2023-05-30

Finding duplicates
A new update to the data pipeline feeding into ride_sharing has added the ride_id column, which represents a unique identifier for each ride.
The update however coincided with radically shorter average ride duration times and irregular user birth dates set in the future. Most importantly, the number of rides taken has increased by 20% overnight, leading you to think there might be both complete and incomplete duplicates in the ride_sharing DataFrame.
In this exercise, you will confirm this suspicion by finding those duplicates. A sample of ride_sharing is in your environment, as well as all the packages you've been working with thus far.
Instructions
•	Find duplicated rows of ride_id in the ride_sharing DataFrame while setting keep to False.
•	Subset ride_sharing on duplicates and sort by ride_id and assign the results to duplicated_rides.
•	Print the ride_id, duration and user_birth_year columns of duplicated_rides in that order.
''''

# Find duplicates
duplicates = ride_sharing.duplicated(subset='ride_id', keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

''''
Treating duplicates
In the last exercise, you were able to verify that the new update feeding into ride_sharing contains a bug generating both complete and incomplete duplicated rows for some values of the ride_id column, with occasional discrepant values for the user_birth_year and duration columns.
In this exercise, you will be treating those duplicated rows by first dropping complete duplicates, and then merging the incomplete duplicate rows into one while keeping the average duration, and the minimum user_birth_year for each set of incomplete duplicate rows.
Instructions
•	Drop complete duplicates in ride_sharing and store the results in ride_dup.
•	Create the statistics dictionary which holds minimum aggregation for user_birth_year and mean aggregation for duration.
•	Drop incomplete duplicates by grouping by ride_id and applying the aggregation in statistics.
•	Find duplicates again and run the assert statement to verify de-duplication.

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby(by='ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
''''


