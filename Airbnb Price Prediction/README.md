[<img src="https://github.com/csmangum/portfolio/blob/master/img/airbnb_portfolio_title.png" width="850">](https://github.com/csmangum/portfolio/tree/master/Airbnb%20Price%20Prediction)

<p> Airbnb is a popular and fast-growing alternative to traditional lodging options. It opened in 2008 in San Francisco California and quickly grew around the world. Los Angeles California is a diverse and popular destination with multiple amusement parks, beaches, and outdoor locations offering people many reasons to visit the area. With the rise in the sharing economy, Airbnb has the potential to offer both customers and hosts more choices.</p>

The purpose of this project is to predict listing price based on several possible features available from data collected through [Inside Airbnb](http://insideairbnb.com/get-the-data.html). This high-level overview will showcase my work with the data while there will be links to the specific notebooks with all the work completed to achieve project results.

![](airbnb_growth.gif)

***
## Initial Cleaning

### Findings
* Many columns have missing data and four columns have more than 90% of values missing
* Four other columns had only one unique values

### Actions
* I will removed these columns that have more than 90% of values missing. Other columns with missing data will be handled later with imputation
* I removed columns 'experiences_offered', 'country_code', 'country', 'has_availability' due to having only one unique value
* Converted all the columns to appropriate data type
* Changed T/F columns to binary
* Cleaned the currency related fields, zipcodes, and percentage columns
* Removed listings with $600 or more daily price. Around 95% of listings are below this amount
***

## Data Exploration
<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/response_time.png" width="500">

### Findings
* Most hosts respond within an hour
* Most hosts are neither verified or superhosts
* Bed type, requires license, and host has a profile pic are not a useful field
* There are a handful of features that are correlated with price
* A few features are highly correlated with each other
* The target variable is skewed and will need to be log transformed 


***

## Feature Selection
![](feature_importance.png)
![](cumulative_importance.png)

### Findings
* The wireless accommodation category has a low correlation
* Bedrooms are the most important feature

### Actions
* Created a variable for when a security deposit is required
* Bundled misc property types in 'other' category
* Created new features based on the amenities text field
* Removed 'zipcode', 'availability_60', 'availability_90', 'bed_type', 'host_has_profile_pic', 'requires_license'
* One-hot-encoded all categorical features
* Imputed all missing values with the median value
* Log transformed the price target
* I used step forward feature selection to choose 10 features

***

## Model Development
### Initial Model
![](initial_model.png)

### Optimized Model
![](final_model.png)

## Conclusion

## Notebooks
1. [Initial Cleaning](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/1.%20Initial%20Cleaning.ipynb)
2. [Data Exploration](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/2.%20Data%20Exploration.ipynb)
3. [Preprocessing](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/3.%20Preprocessing.ipynb) 
4. [Feature Selection](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/4.%20Feature%20Selection.ipynb)
5. [Model Selection and Optimization](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/5.%20Model%20Selection%20%26%20Optimization.ipynb) 
