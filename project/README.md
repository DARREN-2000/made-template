## Project Title: 
# Unveiling the Relationship between GDP and Inflation Rate and Predicting GDP using Regression in Germany

Author: Morris Darren Babu

Date: Januaury, 2024

### Description:

This project investigates the relationship between gross domestic product (GDP) and inflation rate in Germany and utilizes regression analysis to forecast future GDP values based on inflation rate data.

### Data Sources:

#### GDP data: 
link to World Bank GDP data for Germany: 
https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=DE
#### Inflation rate data: 
link to World Bank inflation data for Germany: 
https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=DE

### Data Preprocessing:

#### GDP data:
Remove rows with missing values.Convert the data into numerical format (e.g., convert "200,000" to 200000). Standardize the data to ensure that all variables have a mean of 0 and a standard deviation of 1.
Inflation rate data:
Remove rows with missing values. Convert the data into numerical format. Ensure that the inflation rate data is in the same timeframe as the GDP data.

#### Exploratory Data Analysis (EDA):
Scatter plots: Visualize the relationship between GDP and inflation rate over time.
Correlation matrix: Measure the correlation between GDP and inflation rate.
Time series plots: Examine trends in GDP and inflation rate over time.
Box plots: Identify outliers and assess the distribution of GDP and inflation rate data.

#### Regression Model Development:
Linear regression model: Employ a linear regression model to assess the linear relationship between GDP and inflation rate.
Polynomial regression model: Investigate a polynomial regression model to capture potential nonlinear relationships.
Logarithmic regression model: Consider a logarithmic regression model to account for exponential growth or decay.

#### Model Evaluation:
Mean Squared Error (MSE): Calculated the mean squared error to assess the model's overall performance.
Root Mean Squared Error (RMSE): Measured the root mean squared error as a standardized metric of model accuracy.
R-squared: Measured the proportion of variance in GDP explained by inflation rate.

#### GDP Prediction:
Model Application: Applied the trained regression model to predict future GDP values based on inflation rate data.
Prediction Visualization: Presented predicted GDP values for a specified timeframe.

#### Model Validation: 
Evaluated the model's performance on unseen data to assess itsgeneralizability.

#### Implications:
Understanding Inflation Rate Impact: The findings suggest that inflation rate plays a significant role in influencing GDP growth.
Policymaking Guidance: Regression analysis can inform economic policies aimed at stabilizing inflation and promoting economic growth.
Business Forecasting: Businesses can utilize the model to predict future economic conditions and make informed business plans.

#### Limitations and Future Directions:
The model performs well on historical data but may not be accurate in forecasting unforeseen events.
Other economic factors, such as interest rates, unemployment rates, and government spending, may also influence GDP growth.
Expanding the analysis to a broader range of countries could provide more generalizable insights.
Incorporating advanced machine learning techniques could improve the forecasting accuracy.

