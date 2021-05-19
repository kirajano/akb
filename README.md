
In this project, we tackle the Kaggle Rossman challenge.
The goal is to predict the Sales of a given store on a given day.
The dataset consists of two csv files: store.csv and train.csv
    the former holds info about each store and
    the latter holds the sales info per day for each store.
Submissions are evaluated on the root mean square percentage error (RMSPE).

We go through the following steps:

1- Exploring data:
    EDA and visualization

2- Cleaning data:
    drop data with no store
    drop data with no DayOfWeek
    drop data when store in NOT open
    drop data where promo is NaN
    drop SchoolHoliday data where promo is NaN
    drop parameters that don't seem useful:   
          ('CompetitionOpenSinceMonth','CompetitionOpenSinceYear',/
          'Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval')
    drop all rows with NaNs - Approximately 3% of rows
    convert all the columns to int when necessary

3- Encoding:   
    add Month as dummies
    add a feature for scaled CompetitionDistance
    convert DayOfWeek to dummies
    convert StateHoliday to dummies
    convert StoreType to dummies
    convert Assortment to dummies


3- Looking at the correlations of the Sales with different parameters
    sales has significant correlation with:
      Customers
      DayOfWeek
      StateHoliday
      StoreType
      Scaled CompetitionDistance
      etc.

4- Test / Train Split
