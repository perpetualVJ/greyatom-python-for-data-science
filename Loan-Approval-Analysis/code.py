# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

#Checking for categorical features

categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var)

#Checking for numerical features
numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var)

#Dimensions of Categorical_Variable
print(categorical_var.shape)

#Dimensions of Numerical_Variable
print(numerical_var.shape)

#Removing the missing values

#Droping the Loan_ID
banks = bank_data.drop('Loan_ID', axis = 1)

#Checking null values in each columns
print(banks.isnull().sum())

#Calculating Mode
bank_mode = banks.mode().iloc[0]
print(bank_mode)

#Filling missing(NaN) values of banks with bank_mode
banks.fillna(bank_mode, inplace = True)

#Checking missing values
print(banks.shape)
print(banks.isnull().sum().values.sum())

#Checking the loan amount of an average person based on Gender, Married and Self Employed
avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = ['LoanAmount'], aggfunc = 'mean')

print(avg_loan_amount)

#Checking the percentage of loan approved based on a person's employment type

loan_approved_se = banks.loc[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y'), ['Loan_Status']].count()

loan_approved_nse = banks.loc[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y'),['Loan_Status']].count();

percentage_se = loan_approved_se / 614 * 100
print(percentage_se)

percentage_nse = loan_approved_nse / 614 * 100
print(percentage_nse)


#finding applicants having long term amount loan

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x / 12)

big_loan_term = loan_term[loan_term >= 25].count()

print(big_loan_term)

#Checking average income of an applicant and the average loan given to a person based on the income

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()

print(mean_values)





