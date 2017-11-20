# -*- coding: utf-8 -*-
import pandas as pd

# Read in titanic csv
titanic = pd.read_csv('titanic-data.csv')

# View first 5 rows of dataframe
titanic.head()

# Delete all unnecessary columns
titanic_clean = titanic.drop(['PassengerId','Name','Ticket','Cabin', 
                              'Fare','Embarked', 'Parch', 'SibSp'], axis=1)

# View first 5 rows of new dataframe
titanic_clean.head()

# View missing value count of titanic_clean
titanic_clean.isnull().sum()

# Replace titanic_clean['Age'] 'NaN' values to median age value
age_median = titanic_clean['Age'].dropna().median()

if len(titanic_clean.Age[titanic_clean.Age.isnull()]) > 0:
    titanic_clean.loc[(titanic_clean.Age.isnull()), 'Age'] = age_median
                      
# Audit dataframe to make sure code executed properly
titanic_clean.describe(include="all")

# Create Age categories
titanic_clean['Age_categories'] = pd.cut(titanic_clean['Age'], 
                                  bins=[0,18,49,90], labels=["Child","Adult","Senior"])

# Drop 'Age' column
titanic_clean = titanic_clean.drop(['Age'], axis=1)

# View Survival Rate Based on Class and Gender
class_sex_survived = titanic_clean.groupby(['Pclass' , 'Sex'])[['Survived']].mean()
print class_sex_survived

# Create new dataframe with survival rates for gender/socioeconomic status
survival_rate_columns = ['Class', 'Sex', 'Survival Rate']
survival_rate_data = [('Upper', 'Female', 0.97),
                      ('Upper', 'Male', 0.37),
                      ('Middle', 'Female', 0.92),
                      ('Middle', 'Male', 0.16),
                      ('Lower', 'Female', 0.5),
                      ('Lower', 'Male', 0.14)]

survival_rates = pd.DataFrame.from_records(survival_rate_data, columns=survival_rate_columns)

# View New Dataframe
survival_rates.head()

# Export survival_rates DataFrame to .csv
survival_rates.to_csv('titanic_survival_rates2.csv')
