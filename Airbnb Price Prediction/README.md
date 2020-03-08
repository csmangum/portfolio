[<img src="https://github.com/csmangum/portfolio/blob/master/img/airbnb_portfolio_title.png" width="900">](https://github.com/csmangum/portfolio/tree/master/Airbnb%20Price%20Prediction)
<img src="https://github.com/csmangum/portfolio/blob/master/img/quad_v2.gif">
<p> Airbnb is a popular and fast-growing alternative to traditional lodging options. It opened in 2008 in San Francisco California and quickly grew around the world. Los Angeles California is a diverse and popular destination with multiple amusement parks, beaches, and outdoor locations offering people many reasons to visit the area. With the rise in the sharing economy, Airbnb has the potential to offer both customers and hosts more choices.</p>

The purpose of this project is to predict listing price based on several possible features available from data collected through [Inside Airbnb](http://insideairbnb.com/get-the-data.html). This high-level overview will showcase my work with the data while there will be links to the specific notebooks with all the work completed to achieve project results.
***
## 1. Initial Cleaning & Processing

### Findings
The data quality is pretty good but there are some issues since the listings were scraped from the Airbnb website. There are 31,253 rows and more than 40 columns. For my use, I will only import 41 of them since many other are not useful for modeling. This first step includes some simple cleaning of data types and strings, followed by joining external data sources to provide further context for the algorithms. Many columns have missing data and four columns have more than 90% of values missing.

### Actions
* I removed columns that have more than 90% of values missing. Other columns with missing data will be handled later with imputation
* I removed columns 'experiences_offered', 'country_code', 'country', 'has_availability' due to having only one unique value
* Converted all the columns to appropriate data type
* Changed T/F columns to binary
* Cleaned the currency related fields, zipcodes, and percentage columns
* Removed listings with $500 or more daily price. Around 95% of listings are below this amount
* Added topic models from NLP work on the listing description
* Added zip code-based metrics for income and population

***

## 2. Data Exploration
I will look to predict daily listing price in the Los Angeles area. There are over 20,000 listings in the area with an average price around $126 a daily. Interestingly, the lowest daily price is $10 and the maximum all the way up to $10,000.

### Findings
* Most hosts respond within an hour
* Most hosts are neither verified or superhosts
* Bed type, requires license, and host has a profile pic are not a useful field
* There are a handful of features that are correlated with price
* A few features are highly correlated with each other
* The target variable is skewed and will need to be log transformed 


***Distribution of daily pricing before transformation***  
<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/original_price.png" width="500">

***Heatmap of listings across Los Angeles area***  
<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/heatmap.png" width="900">

***Top 10 Correlations with daily price***  
<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/top_10_correlations.png" width="900">

***

## 3. Feature Engineer
### Actions
* From the security deposit field, I create a boolean feature if there is/ or is not a security deposit required
* With property type, 'Apartment', 'House', 'Condominium', 'Townhouse', 'Loft', and 'Guesthouse' are the most frequent. I converted all other to a misc category named 'Other'
* From the amenities column I used simple text mining to identify boolean columns of specific amenities
* Created dummy variables for categorical features
* Imputed missing values with median values
* Log transformed target variable
* Created a clustering feature based on a few variables using k-means clustering

***Distribution of daily pricing after transformation***  
<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/transformed_price.png" width="500">

***

## 4. Feature Selection

With this section I wanted to see the benefit of feature selection on model performance and runtime. I used a Step-forward feature selection algorithm from the mlxtend library. In most cases, 15 features made up 95% of feature importance and I kept that number of features through the algorithm. In the end, feature selection had little impact on model performance or runtime for my needs.

<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/featue_importance.png" width="800">
<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/cum_importance.png" width="600">

***

## 6. Initial Model Development

I went forward with four algorithms: Linear Regression, Random Forests, Gradient Boosted Regression, and LightGBM from Microsoft. Model performance was similar, but the tree-based model performed better, especially the LightGBM model in both metrics and runtime. Next, I will optimize both gradient boosted models and see how they compare.

<img src="https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/img/main_results.png" width="500">

### Feature Selection (Step Forward)
| Model | R2 | RMSE | Median Absolute Error | Runtime (seconds) |
| :---: | :---: | :---: | :---: | :---: |
| Linear Regression | .741 | $52.00 | 19.7 | 2.2 |
| Random Forest | .742 | $49.10 | 20.1 | 27.6 |
| Gradient Boosted | .812 | $42.90 | 16.8 | 9.89 |
| Light GBM | .852 | $38.20 | 15.0 | 9.13 |

### All Features
| Model | R2 | RMSE | Median Absolute Error | Runtime (seconds) |
| :---: | :---: | :---: | :---: | :---: |
| Linear Regression | .780 | $47.60 | 17.7 | 8.21 |
| Random Forest | .744 | $48.80 | 20.0 | 64.5 |
| Gradient Boosted | .823 | $41.90 | 16.1 | 121.0 |
| Light GBM | .876 | $35.20 | 13.4 | 36.0 |


### Best Performing Model
![](initial_model.png)

***

## 7. Model Optimization

I used scikit learn's gridsearchcv algorithm to optimize a set of parameters for each model. This did result in high runtimes but nothing impractical. I wanted to get a good sense of performance without risking significant overfitting. Again, the LightGBM model performed better and was optimized in significantly less time. However, the model scored on the training set overfit much more based on the difference when scored on the test data.

### Feature Selection (Step Forward)
| Model | R2 | RMSE | Median Absolute Error | Runtime (minutes) |
| :---: | :---: | :---: | :---: | :---: |
| Gradient Boosted | .807 | $44.31 | 17.1 | 72.1 |
| Light GBM | .809 | $44.03 | 15.9 | 5.5 |

### All Features
| Model | R2 | RMSE | Median Absolute Error | Runtime (minutes) |
| :---: | :---: | :---: | :---: | :---: |
| Gradient Boosted | .819 | $43.02 | 16.8 | 254.0 |
| Light GBM | .825 | $42.15 | 15.2 | 13.2 |

### Optimized Model
![](final_model.png)

***

## 8. Natural Language Processing - Topic Modeling

### With NLP & Feature Selection (Step Forward)
| Model | R2 | RMSE | Median Absolute Error | Runtime (seconds)  |
| :---: | :---: | :---: | :---: | :---: |
| Linear Regression | .731 | $52.90 | 20.1 | 2.2 |
| Random Forest | .739 | $49.30 | 20.2 | 27.6 |
| Gradient Boosted | .812 | $43.00 | 16.7 | 23.2 |
| Light GBM | .854 | $37.90 | 14.7 | 8.9 |

### Optimized
| Model | R2 | RMSE | Median Absolute Error | Runtime (minutes) |
| :---: | :---: | :---: | :---: | :---: |
| Gradient Boosted | .807 | $44.02 | 15.9 | 72.9 |
| Light GBM | .809 | $43.67 | 15.7 | 5.9 |

### With NLP & All Features
| Model | R2 | RMSE | Median Absolute Error | Runtime (seconds) |
| :---: | :---: | :---: | :---: | :---: |
| Linear Regression | .783 | $47.40 | 17.4 | 7.2 |
| Random Forest | .744 | $48.80 | 20.0 | 52.4 |
| Gradient Boosted | .824 | $41.70 | 16.0 | 109.0 |
| Light GBM | .877 | $35.00 | 13.3 | 24.4 |

### Optimized
| Model | R2 | RMSE | Median Absolute Error | Runtime (minutes) |
| :---: | :---: | :---: | :---: | :---: |
| Gradient Boosted | .823 | $42.33 | 15.0 | 288.8 |
| Light GBM | .827 | $41.87 | 14.8 | 13.5 |


## 9. Conclusion

## Notebooks
1. [Initial Cleaning](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/1.%20Initial%20Cleaning.ipynb)
2. [Data Exploration](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/2.%20Data%20Exploration.ipynb)
3. [Preprocessing](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/3.%20Preprocessing.ipynb) 
4. [Feature Selection](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/4.%20Feature%20Selection.ipynb)
5. [Model Selection and Optimization](https://github.com/csmangum/portfolio/blob/master/Airbnb%20Price%20Prediction/5.%20Model%20Selection%20%26%20Optimization.ipynb) 
