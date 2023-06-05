# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:13:12 2023

@author: Kasra
"""

''''
Text and categorical data problems
''''


''''
Finding consistency
In this exercise and throughout this chapter, 
you'll be working with the airlines DataFrame which 
contains survey responses on the San Francisco Airport from airline customers.

The DataFrame contains flight metadata such as the airline, the destination, 
waiting times as well as answers to key questions regarding cleanliness, 
safety, and satisfaction. Another DataFrame named categories was created, 
containing all correct possible values for the survey columns.

In this exercise, you will use both of these DataFrames to find 
survey answers with inconsistent values, and drop them, 
effectively performing an outer and inner join on both these DataFrames 
as seen in the video exercise. The pandas package has been imported as pd, 
and the airlines and categories DataFrames are in your environment.

Instructions 1/4

Print the categories DataFrame and take a close look at all possible 
correct categories of the survey columns.

Print the unique values of the survey columns 
in airlines using the .unique() method.
''''

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

''''
IPython Shell

      cleanliness           safety          satisfaction
0           Clean          Neutral        Very satisfied
1         Average        Very safe               Neutral
2  Somewhat clean    Somewhat safe    Somewhat satisfied
3  Somewhat dirty      Very unsafe  Somewhat unsatisfied
4           Dirty  Somewhat unsafe      Very unsatisfied
Cleanliness:  ['Clean', 'Average', 'Unacceptable', 'Somewhat clean', 'Somewhat dirty', 'Dirty']
Categories (6, object): ['Average', 'Clean', 'Dirty', 'Somewhat clean', 'Somewhat dirty', 'Unacceptable'] 

Safety:  ['Neutral', 'Very safe', 'Somewhat safe', 'Very unsafe', 'Somewhat unsafe']
Categories (5, object): ['Neutral', 'Somewhat safe', 'Somewhat unsafe', 'Very safe', 'Very unsafe'] 

Satisfaction:  ['Very satisfied', 'Neutral', 'Somewhat satisfied', 'Somewhat unsatisfied', 'Very unsatisfied']
Categories (5, object): ['Neutral', 'Somewhat satisfied', 'Somewhat unsatisfied', 'Very satisfied', 'Very unsatisfied']
''''

''''
Instructions 2/4

Question
Take a look at the output. Out of the cleanliness, safety and satisfaction 
columns, which one has an inconsistent category and what is it?

answer: 
    Cleanness because it has an Unacceptable answer
''''

''''
Instructions 3/4

Create a set out of the cleanliness column in airlines using set() 
and find the inconsistent category by finding the difference 
in the cleanliness column of categories.

Find rows of airlines with a cleanliness value not in categories 
and print the output.
''''

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

''''
IPython Shell

       id        day           airline  destination  dest_region dest_size boarding_area   dept_time  wait_min   cleanliness         safety        satisfaction
4    2992  Wednesday          AMERICAN        MIAMI      East US       Hub   Gates 50-59  2018-12-31     559.0  Unacceptable      Very safe  Somewhat satisfied
18   2913     Friday  TURKISH AIRLINES     ISTANBUL  Middle East       Hub  Gates 91-102  2018-12-31     225.0  Unacceptable      Very safe  Somewhat satisfied
100  2321  Wednesday         SOUTHWEST  LOS ANGELES      West US       Hub   Gates 20-39  2018-12-31     130.0  Unacceptable  Somewhat safe  Somewhat satisfied

''''



''''
Instructions 4/4

Print the rows with the consistent categories of cleanliness only.

''''

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])

''''
IPython Shell

       id        day           airline  destination  dest_region dest_size boarding_area   dept_time  wait_min   cleanliness         safety        satisfaction
4    2992  Wednesday          AMERICAN        MIAMI      East US       Hub   Gates 50-59  2018-12-31     559.0  Unacceptable      Very safe  Somewhat satisfied
18   2913     Friday  TURKISH AIRLINES     ISTANBUL  Middle East       Hub  Gates 91-102  2018-12-31     225.0  Unacceptable      Very safe  Somewhat satisfied
100  2321  Wednesday         SOUTHWEST  LOS ANGELES      West US       Hub   Gates 20-39  2018-12-31     130.0  Unacceptable  Somewhat safe  Somewhat satisfied
        id       day        airline        destination    dest_region dest_size boarding_area   dept_time  wait_min     cleanliness         safety        satisfaction
0     1351   Tuesday    UNITED INTL             KANSAI           Asia       Hub  Gates 91-102  2018-12-31     115.0           Clean        Neutral      Very satisfied
1      373    Friday         ALASKA  SAN JOSE DEL CABO  Canada/Mexico     Small   Gates 50-59  2018-12-31     135.0           Clean      Very safe      Very satisfied
2     2820  Thursday          DELTA        LOS ANGELES        West US       Hub   Gates 40-48  2018-12-31      70.0         Average  Somewhat safe             Neutral
3     1157   Tuesday      SOUTHWEST        LOS ANGELES        West US       Hub   Gates 20-39  2018-12-31     190.0           Clean      Very safe  Somewhat satisfied
5      634  Thursday         ALASKA             NEWARK        East US       Hub   Gates 50-59  2018-12-31     140.0  Somewhat clean      Very safe      Very satisfied
...    ...       ...            ...                ...            ...       ...           ...         ...       ...             ...            ...                 ...
2804  1475   Tuesday         ALASKA       NEW YORK-JFK        East US       Hub   Gates 50-59  2018-12-31     280.0  Somewhat clean        Neutral  Somewhat satisfied
2805  2222  Thursday      SOUTHWEST            PHOENIX        West US       Hub   Gates 20-39  2018-12-31     165.0           Clean      Very safe      Very satisfied
2806  2684    Friday         UNITED            ORLANDO        East US       Hub   Gates 70-90  2018-12-31      92.0           Clean      Very safe      Very satisfied
2807  2549   Tuesday        JETBLUE         LONG BEACH        West US     Small    Gates 1-12  2018-12-31      95.0           Clean  Somewhat safe      Very satisfied
2808  2162  Saturday  CHINA EASTERN            QINGDAO           Asia     Large    Gates 1-12  2018-12-31     220.0           Clean      Very safe  Somewhat satisfied

[2474 rows x 12 columns]

''''
''''
''''
''''
''''

''''
Inconsistent categories

In this exercise, you'll be revisiting the airlines DataFrame 
from the previous lesson.

As a reminder, the DataFrame contains flight metadata such as the airline, 
the destination, waiting times as well as answers to key questions regarding 
cleanliness, safety, and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this 
DataFrame, dest_region and dest_size respectively, assess how to address 
them and make sure that they are cleaned and ready for analysis. 
The pandas package has been imported as pd, and the airlines DataFrame 
is in your environment.

Instructions 1/4

Print the unique values in dest_region and dest_size respectively.
''''
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

''''
IPython Shell

['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
 'Middle East' 'Europe' 'eur' 'Central/South America'
 'Australia/New Zealand' 'middle east']
['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
 'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
''''

''''
Instructions 2/4

Question
From looking at the output, what do you think is the problem with these columns?
''''

''''
Instructions 3/4

Change the capitalization of all values of dest_region to lowercase.
Replace the 'eur' with 'europe' in dest_region using the .replace() method.
''''

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

''''
IPython Shell

['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
 'Middle East' 'Europe' 'eur' 'Central/South America'
 'Australia/New Zealand' 'middle east']
['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
 'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
''''

''''
Instructions 4/4

Strip white spaces from the dest_size column using the .strip() method.
Verify that the changes have been into effect by printing 
the unique values of the columns using .unique() .
''''

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

''''
IPython Shell

['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
 'Middle East' 'Europe' 'eur' 'Central/South America'
 'Australia/New Zealand' 'middle east']
['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
 'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
['asia' 'canada/mexico' 'west us' 'east us' 'midwest us' 'middle east'
 'europe' 'central/south america' 'australia/new zealand']
['Hub' 'Small' 'Medium' 'Large']
''''

''''
Remapping categories
To better understand survey respondents from airlines, 
you want to find out if there is a relationship between 
certain responses and the day of the week and wait time at the gate.

The airlines DataFrame contains the day and wait_min columns, 
which are categorical and numerical respectively. 
The day column contains the exact day a flight took place, 
and wait_min contains the amount of minutes it took travelers to 
wait at the gate. To make your analysis easier, you want to 
create two new categorical variables:

wait_type: 'short' for 0-60 min, 'medium' for 60-180 and long for 180+
day_week: 'weekday' if day is in the weekday, 'weekend' if day is in the weekend.
The pandas and numpy packages have been imported as pd and np. 
Let's create some new categorical data!

Instructions

Create the ranges and labels for the wait_type column 
mentioned in the description.

Create the wait_type column by from wait_min by using pd.cut(), 
while inputting label_ranges and label_names in the correct arguments.

Create the mapping dictionary mapping weekdays to 'weekday' 
and weekend days to 'weekend'.

Create the day_week column by using .replace().
''''

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)

''''
IPython Shell

mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)
''''

''''
''''
''''
''''

''''
Removing titles and taking names

While collecting survey respondent metadata in the airlines DataFrame, 
the full name of respondents was saved in the full_name column. 
However upon closer inspection, you found that a lot of the different names 
are prefixed by honorifics such as "Dr.", "Mr.", "Ms." and "Miss".

Your ultimate objective is to create two new columns named first_name and 
last_name, containing the first and last names of respondents respectively. 
Before doing so however, you need to remove honorifics.

The airlines DataFrame is in your environment, alongside pandas as pd.

Instructions

Remove "Dr.", "Mr.", "Miss" and "Ms." from full_name by replacing them 
with an empty string "" in that order.

Run the assert statement using .str.contains() that tests whether full_name 
still contains any of the honorifics.
''''
# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")


# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

''''
IPython Shell

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")


# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False
''''

''''
Keeping it descriptive

To further understand travelers' experiences in the San Francisco Airport, 
the quality assurance department sent out a qualitative questionnaire to all 
travelers who gave the airport the worst score on all possible categories. 
The objective behind this questionnaire is to identify common patterns 
in what travelers are saying about the airport.

Their response is stored in the survey_response column. 
Upon a closer look, you realized a few of the answers gave 
the shortest possible character amount without much substance. 
In this exercise, you will isolate the responses with a character 
count higher than 40 , and make sure your new DataFrame contains 
responses with 40 characters or more using an assert statement.

The airlines DataFrame is in your environment, and pandas is imported as pd.

Instructions

Using the airlines DataFrame, store the length of each instance 
in the survey_response column in resp_length by using .str.len().

Isolate the rows of airlines with resp_length higher than 40.

Assert that the smallest survey_response length in airlines_survey 
is now bigger than 40.
''''

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])

''''
IPython Shell

18    The airport personnell forgot to alert us of d...
19    The food in the airport was really really expe...
20    One of the other travelers was really loud and...
21    I don't remember answering the survey with the...
22    The airport personnel kept ignoring my request...
23    The chair I sat in was extremely uncomfortable...
24    I wish you were more like other airports, the ...
25    I was really unsatisfied with the wait times b...
27    The flight was okay, but I didn't really like ...
28    We were really slowed down by security measure...
29    There was a spill on the aisle next to the bat...
30    I felt very unsatisfied by how long the flight...
Name: survey_response, dtype: object
''''







