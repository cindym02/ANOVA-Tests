#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:35:52 2021

@author: cindy
"""


import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import norm, kurtosis, skew, bartlett

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)

diabetes = diabetes.replace('?', np.NaN)

# There are 17 levels of PAYER CODE
diabetes.payer_code.value_counts() 
diabetes['payer_code'].value_counts() 
len(diabetes.payer_code.value_counts())

# There are 5 levels of RACE
diabetes.race.value_counts() 
diabetes['race'].value_counts() 
len(diabetes.age.value_counts())

# There are 72 levels of MEDICAL SPECIALTY
diabetes.medical_specialty.value_counts() 
diabetes['medical_specialty'].value_counts() 
len(diabetes.medical_specialty.value_counts())

# Continuous DV variable
labprocedures = diabetes['num_lab_procedures'] 
# IV variable 1
medspecialty = diabetes['medical_specialty']

# Assumption testing 1
medspecialty1 = diabetes[diabetes['medical_specialty'] == 'InternalMedicine']
medspecialty2 = diabetes[diabetes['medical_specialty'] == 'Emergency/Trauma']
medspecialty3 = diabetes[diabetes['medical_specialty'] == 'Family/GeneralPractice']
medspecialty4 = diabetes[diabetes['medical_specialty'] == 'Cardiology']
medspecialty5 = diabetes[diabetes['medical_specialty'] == 'Surgery-General']
                          
# Kurtosis 
print(kurtosis(medspecialty1['num_lab_procedures']))
print(kurtosis(medspecialty2['num_lab_procedures']))
print(kurtosis(medspecialty3['num_lab_procedures']))
print(kurtosis(medspecialty4['num_lab_procedures']))
print(kurtosis(medspecialty5['num_lab_procedures']))

# Skewness
print(skew(medspecialty1['num_lab_procedures']))
print(skew(medspecialty2['num_lab_procedures']))
print(skew(medspecialty3['num_lab_procedures']))
print(skew(medspecialty4['num_lab_procedures']))
print(skew(medspecialty5['num_lab_procedures']))

# Bartlett testing for homogeneity
stats.bartlett(medspecialty1['num_lab_procedures'],
               medspecialty2['num_lab_procedures'],
               medspecialty3['num_lab_procedures'],
               medspecialty4['num_lab_procedures'],
               medspecialty5['num_lab_procedures']
               )

# Non-parametric ANOVA test
stats.f_oneway(medspecialty1['num_lab_procedures'],
               medspecialty2['num_lab_procedures'],
               medspecialty3['num_lab_procedures'],
               medspecialty4['num_lab_procedures'],
               medspecialty5['num_lab_procedures'])

# 1. Is there a difference between the levels of MEDICAL SPECIALTY and number of lab procedures?
# 1. Yes there is statistical difference. We reject the null hypothesis since the P-value is <= 0.05


# Continuous DV variable
diagnosesnumber = diabetes['number_diagnoses'] 
# IV variable 2
race = diabetes['race']

race1 = diabetes[diabetes['race'] == 'Asian']
race2 = diabetes[diabetes['race'] == 'AfricanAmerican']
race3 = diabetes[diabetes['race'] == 'Hispanic']
race4 = diabetes[diabetes['race'] == 'Other']
race5 = diabetes[diabetes['race'] == 'Caucasian']

print(kurtosis(race1['number_diagnoses']))
print(kurtosis(race2['number_diagnoses']))
print(kurtosis(race3['number_diagnoses']))
print(kurtosis(race4['number_diagnoses']))
print(kurtosis(race5['number_diagnoses']))

print(skew(race1['number_diagnoses']))
print(skew(race2['number_diagnoses']))
print(skew(race3['number_diagnoses']))
print(skew(race4['number_diagnoses']))
print(skew(race5['number_diagnoses']))

stats.bartlett(race1['number_diagnoses'],
               race2['number_diagnoses'],
               race3['number_diagnoses'],
               race4['number_diagnoses'],
               race5['number_diagnoses']
               )

stats.f_oneway(race1['number_diagnoses'],
               race2['number_diagnoses'],
               race3['number_diagnoses'],
               race4['number_diagnoses'],
               race5['number_diagnoses'])

# 2. Is there a difference between the levels of RACE and number of diagnoses?
# 2. Yes there is statistical difference. We reject the null hypothesis since the P-value is <= 0.05

# Continuous DV variable
labprocedures = diabetes['num_lab_procedures'] 
# IV variable 3
payercode = diabetes['payer_code']

# Assumptions testing 3
payercode1 = diabetes[diabetes['payer_code'] == 'MC']
payercode2 = diabetes[diabetes['payer_code'] == 'HM']
payercode3 = diabetes[diabetes['payer_code'] == 'SP']
payercode4 = diabetes[diabetes['payer_code'] == 'BC']
payercode5 = diabetes[diabetes['payer_code'] == 'MD']

print(kurtosis(payercode1['num_lab_procedures']))
print(kurtosis(payercode2['num_lab_procedures']))
print(kurtosis(payercode3['num_lab_procedures']))
print(kurtosis(payercode4['num_lab_procedures']))
print(kurtosis(payercode5['num_lab_procedures']))

print(skew(payercode1['num_lab_procedures']))
print(skew(payercode2['num_lab_procedures']))
print(skew(payercode3['num_lab_procedures']))
print(skew(payercode4['num_lab_procedures']))
print(skew(payercode5['num_lab_procedures']))

stats.bartlett(payercode1['num_lab_procedures'],
               payercode2['num_lab_procedures'],
               payercode3['num_lab_procedures'],
               payercode4['num_lab_procedures'],
               payercode5['num_lab_procedures']
               )

# Non-parametric ANOVA test
stats.f_oneway(payercode1['num_lab_procedures'],
               payercode2['num_lab_procedures'],
               payercode3['num_lab_procedures'],
               payercode4['num_lab_procedures'],
               payercode5['num_lab_procedures'])

# 3. Is there a difference between the levels of insurance company ID and number of lab procedures?
# 3. Yes there is statistical difference. We reject the null hypothesis since the P-value is <= 0.05








