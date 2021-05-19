# akb
In this project, we tackle the Kaggle Rossman challenge. The goal is to predict the Sales of a given store on a given day.

The dataset consists of two csv files: store.csv and train.csv
The former holds info about each store and the latter the sales info per day for each store.

Submissions are evaluated on the root mean square percentage error (RMSPE):

Zero sales days are ignored in scoring - part of your pipeline should look for these rows and drop them (in both test & train) 
