### Abeer

- Data Cleaning
- Data Label Encoding (StoreType, Assortment, StateHoliday)
- Data Freq Encoding (Store)

### Bahar

- Data Label Encoding (StoreType, Assortment, StateHoliday)
- Data Cleaning (dropped everything with PROMO2)
- Customers and Promo correlate with Sales

### Kiril

- Data Cleaning
- Data Target Encoding (Store based on Customers, DayOfWeek based on Customers) 
- Train / Test split
- Baseline Model with Average 
- Random Forest Regressor



## TO DO FOR TODAY / TOMORROW

- Build a pipeline with other Regressors (RandomForest, XGBoost, SVR) --> (Kiril)
- Hyperparameter tuning
- Apply TimeSeries predictors (Exponential Smoothing, ARIMA)
- Feature Engineering:
	- Standardization / Scaling (understand what to scale and see effect) --> (Kiril et al.)
	- Promo2 (understand how to use) --> (Bahar)
	- DayOfWeek investigate how to improve --> (Kiril)
	- Seasonality (Xmas, other) --> (Abeer)
	- Comptetitor Distance (perhaps opening shop time)
	- Encoding Assortment to see effect --> (Kiril)
	- Encoding StoreType to see effect --> (Kiril)
- Visualization: --> (Abeer)
	- Covariance for Correlations
	- Predictions
	- Visualing NAs
- Cross-Validation for Overfitting --> (Kiril et al.)


	

