# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:25:16 2023

@author: Kasra
"""

''''
Advanced data problems
In this chapter, we're looking at more advanced data cleaning problems, such as

uniformity
cross field validation
dealing with missing data
''''

''''
**Uniformity**
''''

#upload the dataset file
from google.colab import files
uploaded = files.upload()

# read the uploaded file
airlines = pd.read_csv('banking.csv')

''''
Ambiguous dates

You have a DataFrame containing a subscription_date column that was 
collected from various sources with different Date formats such 
as YYYY-mm-dd and YYYY-dd-mm. What is the best way to unify the formats 
for ambiguous values such as 2019-04-07?:
''''    
    

''''
   Ambiguous dates

Question

You have a DataFrame containing a subscription_date column that was collected from various sources with different Date formats such as

YYYY-mm-dd
YYYY-dd-mm.
What is the best way to unify the formats for ambiguous values such as 2019-04-07?

Possible Answers

Set them to NA and drop them.

Infer the format of the data in question by checking the format of subsequent and previous values.

Infer the format from the original data source.

All of the above are possible, as long as we investigate where our data comes from, and understand the dynamics affecting it before cleaning it.

Answer

All of the above are possible, as long as we investigate where our data comes from, and understand the dynamics affecting it before cleaning it.
    ''''
   
    ''''
    
**Exercise: Uniform currencies**

---



> In this exercise and throughout this chapter, you will be working with a retail banking dataset stored in the banking DataFrame. The dataset contains data on 
* the amount of money stored in accounts (acct_amount), 
* their currency (acct_cur), 
* amount invested (inv_amount), 
* account opening date (account_opened), and 
* last transaction date (last_transaction) 
that were consolidated from American and European branches.

> You are tasked with understanding the average account size and how investments vary by the size of account, however in order to produce this analysis accurately, you first need to unify the currency amount into dollars. The pandas package has been imported as pd, and the banking DataFrame is in your environment.
''''

''''
**Instructions**

---



* Find the rows of acct_cur in banking that are equal to 'euro' and store them in the variable acct_eu.

* Find all the rows of acct_amount in banking that fit the acct_eu condition, and convert them to USD by multiplying them with 1.1.

* Find all the rows of acct_cur in banking that fit the acct_eu condition, set them to 'dollar'.
''''
   
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

''''
**Uniform dates**

---



> After having unified the currencies of your different account 
amounts, you want to add a temporal dimension to your analysis and 
see how customers have been investing their money given the size of 
their account over each year. The account_opened column represents 
when customers opened their accounts and is a good proxy for segmenting 
customer activity and investment over time.

> However, since this data was consolidated from multiple sources, 
you need to make sure that all dates are of the same format. You will 
do so by converting this column into a datetime object, while making 
sure that the format is inferred and potentially incorrect formats are 
set to missing. The banking DataFrame is in your environment and pandas 
was imported as pd.
''''
''''
**Instructions 1/4**

---

* Print the header of account_opened from the banking DataFrame and take a look at the different results.
''''

# Print the header of account_opened
print(banking['account_opened'].head())

''''
IPython Shell

0          2018-03-05

1            21-01-18

2    January 26, 2018

3            21-14-17

4            05-06-17

Name: account_opened, dtype: object
''''

''''    
Question
Take a look at the output. You tried converting the values to datetime 
using the default to_datetime() function without changing any argument, 
however received the following error:

ValueError: month must be in 1..12
Why do you think that is?

answers:
     
The 21-14-17 entry is erroneous and leads to an error.     

''''

''''
> **Instructions 3/4**

---



Convert the account_opened column to datetime, 
while making sure the date format is inferred and 
that erroneous formats that raise error return a missing value.
''''

# Print the header of account_opened
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

''''
> **Instructions 4/4**

---



Extract the year from the amended account_opened column and assign it to the acct_year column.

Print the newly created acct_year column.
''''

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])


''''
> **IPython Shell**

---



    0     2018

    1     2018

    2     2018

    3      NaN

    4     2017

      ... 

    92    2017

    93    2018

    94    2018

    95    2017

    96    2017

    Name: acct_year, Length: 97, dtype: object

Cunning calendar cleaning! Now that the acct_year column is created, a simple .groupby() will show you how accounts are opened on a yearly!
''''

''''
>> **Cross field validation**

---

Cross field validation is the use of multiple fields in your dataset to sanity check the integrity of your data. For example in our flights dataset, this could be summing economy, business and first class values and making sure they are equal to the total passengers on the plane. 
''''
''''
> **How's our data integrity?**

---



New data has been merged into the banking DataFrame that contains details on how investments in the inv_amount column are allocated across four different funds A, B, C and D.

Furthermore, the age and birthdays of customers are now stored in the age and birth_date columns respectively.

You want to understand how customers of different age groups invest. However, you want to first make sure the data you're analyzing is correct. You will do so by cross field checking values of inv_amount and age against the amount invested in different funds and customers' birthdays. Both pandas and datetime have been imported as pd and dt respectively.
''''


''''
> **Dataset: banking**

---



         cust_id birth_date  age  acct_amount  inv_amount  ...   fund_B   fund_C   fund_D  account_opened last_transaction

    0   870A9281 1962-06-09   61     63523.31       51295  ...   4138.0   1420.0  15632.0        02-09-18         22-02-19

    1   166B05B0 1962-12-16   61     38175.46       15050  ...    938.0   6696.0   2421.0        28-02-19         31-10-18

    2   BFC13E88 1990-09-12   33     59863.77       24567  ...   4590.0   8469.0   1185.0        25-04-18         02-04-18

    3   F2158F66 1985-11-03   38     84132.10       23712  ...    492.0   6482.0  12830.0        07-11-17         08-11-18

    4   7A73F334 1990-05-17   39    120512.00       93230  ...  51281.0  13434.0  18383.0        14-05-18         19-07-18

    ..       ...        ...  ...          ...         ...  ...      ...      ...      ...             ...              ...

    95  CA507BA1 1974-08-10   49     12209.84        7515  ...    931.0   1451.0   4943.0        26-05-18         11-09-19

    96  B99CD662 1989-12-12   34     92838.44       49089  ...   7892.0  31486.0   7258.0        04-05-17         12-03-19

    97  13770971 1984-11-29   39     92750.87       27962  ...   7547.0   8486.0   8577.0        16-08-17         24-04-19

    98  93E78DA3 1969-12-14   54     41942.23       29662  ...  11174.0  11650.0   5080.0        09-10-17         15-04-18

    99  AC91D689 1993-05-18   30     99490.61       32149  ...  17918.0   6714.0   5333.0        01-08-17         04-08-19

    [100 rows x 11 columns]
''''


''''
> **Instructions 1/2**

---



1. 
* Find the rows where the sum of all rows of the fund_columns in banking are equal to the inv_amount column.

* Store the values of banking with consistent inv_amount in consistent_inv, and those with inconsistent ones in inconsistent_inv.
''''

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])


''''
> **IPython Shell**

Number of inconsistent investments:  8
''''

''''
> **Instructions 2/2**

2. 
* Store today's date into today, and manually calculate customers' ages and store them in ages_manual.

* Find all rows of banking where the age column is equal to ages_manual and then filter banking into consistent_ages and inconsistent_ages.
''''

# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = ages_manual == banking['age']

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])


''''
> **IPython Shell**

---

Number of inconsistent ages:  4

 There are only 8 and 4 rows affected by inconsistent ***inv_amount*** and ***age values***, respectively. 
 
 In this case, it's best to investigate the underlying data sources before deciding on a course of action!
''''


''''
>> **completeness and missing data**

---

missing data is when no data value is stored for a variable in an observation. 

Missing data is most commonly represented as 
* NA 
* NaN

but can take on arbitrary values like 
* 0
* dot

Like a lot of the problems that we've seen thus far in the course, it's commonly due to 
* technical error 
* human errors.
''''

''''
> **Is this missing at random?**

---



You've seen in the video exercise how there are a variety of missingness types when observing missing data. As a reminder, missingness types can be described as the following:

1. Missing Completely at Random: No systematic relationship between a column's missing values and other or own values.

2. Missing at Random: There is a systematic relationship between a column's missing values and other observed values.

3. Missing not at Random: There is a systematic relationship between a column's missing values and unobserved values.

''''


''''
> **Question:**

---



You have a DataFrame containing customer satisfaction scores for a service. What type of missingness is the following?

       A customer satisfaction_score column with missing values for highly dissatisfied customers.

Possible Answers:

1. Missing completely at random.

2. Missing at random.

3. Missing not at random.

Answer:
3. Missing not at random.

This is a clear example of missing not at random, where low values of satisfaction_score are missing because of inherently low satisfaction!
''''


''''
> **Exercise: Missing investors**

---



Dealing with missing data is one of the most common tasks in data science. There are a variety of types of missingness, as well as a variety of types of solutions to missing data.

You just received a new version of the banking DataFrame containing data on the amount held and invested for new and existing customers. However, there are rows with missing inv_amount values.

You know for a fact that most customers below 25 do not have investment accounts yet, and suspect it could be driving the missingness. The pandas, missingno and matplotlib.pyplot packages have been imported as pd, msno and plt respectively. The banking DataFrame is in your environment.
''''


''''
> **Dataset:**

---



        cust_id  age  acct_amount  inv_amount account_opened last_transaction

    0   8C35540A   54     44244.71    35500.50       03-05-18         30-09-19

    1   D5536652   36     86506.85    81921.86       21-01-18         14-01-19

    2   A631984D   49     77799.33    46412.27       26-01-18         06-10-19

    3   93F2F951   56     93875.24    76563.35       21-08-17         10-07-19

    4   DE0A0882   21     99998.35         NaN       05-06-17         15-01-19

    ..       ...  ...          ...         ...            ...              ...

    92  CEC1CAE5   32     92169.14    77896.86       26-11-17         08-10-18

    93  4C7F8638   23     21942.37         NaN       14-07-18         02-02-19

    94  A81D31B3   24     74010.15         NaN       02-06-18         12-09-18

    95  93A17007   36     40651.36     9387.87       28-05-17         08-03-19

    96  E961CA44   57     27907.16    10967.69       23-10-17         11-07-19

    [97 rows x 6 columns]
''''

''''
> **Instructions 1/4**


* Print the number of missing values by column in the banking DataFrame.

* Plot and show the missingness matrix of banking with the msno.matrix() function.
''''


# Print number of missing values in banking
print(banking['inv_amount'].isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

''''
> **output:**

    13

> Indented block
''''


''''
> **Instructions 2/4**

* Isolate the values of banking missing values of inv_amount into missing_investors and with non-missing inv_amount values into investors.
''''

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

''''
> **Instructions 3/4**

**Question:**

* Now that you've isolated banking into investors and missing_investors, use the .describe() method on both of these DataFrames in the IPython shell to understand whether there are structural differences between them. What do you think is going on?
''''

investors.describe()

''''
> **Output:**

          age  acct_amount  inv_amount

    count  84.000       84.000      84.000

    mean   43.560    75095.273   44717.885

    std    10.411    32414.506   26031.246

    min    26.000    12209.840    3216.720

    25%    34.000    57373.062   22736.037

    50%    45.000    83061.845   44498.460

    75%    53.000    94165.965   66176.803

    max    59.000   250046.760   93552.690
''''

missing_investors.describe()

''''
> **Output:**

          age  acct_amount  inv_amount

    count  13.000       13.000         0.0

    mean   21.846    73231.238         NaN

    std     1.519    25553.327         NaN

    min    20.000    21942.370         NaN

    25%    21.000    66947.300         NaN

    50%    21.000    86028.480         NaN

    75%    23.000    89855.980         NaN

    max    25.000    99998.350         NaN
''''


''''
> **Instructions 4/4**

* Sort the banking DataFrame by the age column and plot the missingness matrix of banking_sorted.
''''

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by = 'age')
msno.matrix(banking_sorted)
plt.show()



''''
* Notice how all the white spaces for inv_amount are on top? Indeed missing values are only due to young bank account holders not investing their money! Better set it to 0 with .fillna().

> Indented block

''''


''''
> **EXERCISE: Follow the money**

In this exercise, you're working with another version of the banking DataFrame that contains missing values for both the cust_id column and the acct_amount column.

You want to produce analysis on how many unique customers the bank has, the average amount held by customers and more. You know that rows with missing cust_id don't really help you, and that on average acct_amount is usually 5 times the amount of inv_amount.

In this exercise, you will drop rows of banking with missing cust_ids, and impute missing values of acct_amount with some domain knowledge.
''''


''''
> **Dataset:**

         cust_id  acct_amount  inv_amount account_opened last_transaction
    0   8C35540A     44244.71    35500.50       03-05-18         30-09-19
    1   D5536652          NaN    81921.86       21-01-18         14-01-19
    2   A631984D          NaN    46412.27       26-01-18         06-10-19
    3   93F2F951          NaN    76563.35       21-08-17         10-07-19
    4   DE0A0882          NaN    18669.01       05-06-17         15-01-19
    ..       ...          ...         ...            ...              ...
    92  CEC1CAE5     92169.14    77896.86       26-11-17         08-10-18
    93  4C7F8638     21942.37    11715.24       14-07-18         02-02-19
    94  A81D31B3     74010.15    48787.47       02-06-18         12-09-18
    95  93A17007     40651.36     9387.87       28-05-17         08-03-19
    96       NaN     27907.16    10967.69       23-10-17         11-07-19

    [97 rows x 5 columns]
''''




''''
> **Instructions**

* Use .dropna() to drop missing values of the cust_id column in banking and store the results in banking_fullid.

* Use inv_amount to compute the estimated account amounts for banking_fullid by setting the amounts equal to inv_amount * 5, and assign the results to acct_imp.

* Impute the missing values of acct_amount in banking_fullid with the newly created acct_imp using .fillna().
''''


# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())

''''
> **output:**

    cust_id             0
    acct_amount         0
    inv_amount          0
    account_opened      0
    last_transaction    0
    dtype: int64

* As you can see no missing data left, you can definitely _bank_ on getting your analysis right!
''''












