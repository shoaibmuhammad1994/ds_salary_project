# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:47:38 2020

@author: Shoaib
"""
import pandas as pd

# read data
df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
##############################################################################

# create columns for per hour and employer provided salary
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

# remove columns with -1 as salary
df = df[df['Salary Estimate'] != '-1']

# remove words, K and $ from Salary Estimate column
salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0].replace('K', "").replace('$', ''))

# remove Per Hour from salary
salary = salary.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

# create min and max salaries series
df['min_salary'] = salary.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = salary.apply(lambda x: int(x.split('-')[1]))

# create avg_salary from df['min_salary'] and df['max_saslary']
df['avg_salary'] = (df.min_salary+df.max_salary)/2

##############################################################################

# company name text only
##############################################################################
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)
##############################################################################

# state field
##############################################################################
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()
##############################################################################

# check if job location and headquarter are the same
##############################################################################
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
##############################################################################

# age of company
##############################################################################
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)
##############################################################################

# parsing of jobs description (python, etc.)
##############################################################################
# check how Job Description is mentioned
df['Job Description'][0]

#### python ####
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#### r studio ####
# df.drop(['r_studio'], axis=1, inplace=True)
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df.R_yn.value_counts()

#### spark ####
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#### aws ####
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#### excel ####
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()
##############################################################################

# remove the 'Unamed: 0' column
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# save df to csv
df.to_csv('salary_data_cleaned.csv', index=False)
