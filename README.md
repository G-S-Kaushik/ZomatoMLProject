# ZomatoMLProject

## Preprocessing and Exploratory Data Analysis (EDA)
In this phase, I utilized the following libraries: pandas, seaborn, matplotlib.pyplot, and the statistics library. I followed these steps:

Data Cleanup: Removed unnecessary columns like URL, address, and phone, while retaining key features for further analysis. This helped streamline the dataset.

Handling Duplicates: Eliminated duplicate rows from the dataset to ensure data integrity.

Data Cleaning: Cleaned columns for better analysis and understanding.

Handling Null Values: Removed rows with null values to ensure accurate analysis.

Column Renaming: Renamed columns for clarity and easier interpretation during analysis.

Univariate and Bivariate Analysis: Conducted both univariate and bivariate analysis using Python. This provided a fundamental understanding of the dataset.

Exporting Cleaned Data: Exported the cleaned data as a CSV file for subsequent stages.

## Excel-CSV Data Transformation
Using Power Query in Excel, I performed the following tasks:

Cuisine Cleaning: Cleaned the "cuisines" column to ensure each cuisine type had a unique food category. This enhanced data quality and clarity.

## Tableau Visualization
Employing Tableau, I created comprehensive multivariate analyses. The dashboard aided in achieving business objectives and enabled users to navigate data insights effortlessly.

## MySQL Querying
Utilizing MySQL, I addressed specific user queries, enhancing the project's user-friendliness.

## Machine Learning
For building predictive models, I used the following libraries: scikit-learn, tabulate, and the previously mentioned libraries. I followed these steps:

Dataset Selection: Utilized the cleaned Zomato.csv file with preprocessing and feature engineering already performed.

Target Feature Definition: Chose "cost_per_plate" as the target feature for regression analysis.

Regression Techniques: Employed regression techniques for modeling. Among them, the stacked model showed superior performance compared to other regression models.

## Model Deployment
Using the pickle and Streamlit libraries, I developed an interactive web app. This app allows end users to receive estimated results from the machine learning model with ease.

![app](https://github.com/G-S-Kaushik/ZomatoMLProject/assets/108515997/4a2a3669-434e-4438-b1a1-ef7597a03033)

