# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

#Census
census = np.concatenate((new_record,data))

#Calculating age
age = census[:,0]

#Maximum age
max_age = np.max(age)
print(max_age)

#Minimum age 
min_age = np.min(age)
print(min_age)

#Mean age
age_mean = np.mean(age)
print(age_mean)

#Standard Deviation age
age_std = np.std(age)
print(age_std)

#Country's race distribution

race = census[:, 2]

race_0 = race[race == 0]
race_1 = race[race == 1]
race_2 = race[race == 2]
race_3 = race[race == 3]
race_4 = race[race == 4]

#Calculating length's of races

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)


length = list([len_0, len_1, len_2, len_3, len_4])

min_race = min(length)

#No of people in minority race
minority_race = length.index(min_race)
print(minority_race)

#Senior citizens
senior_citizens = census[age > 60]

#Total working sum
working_hours_sum = senior_citizens[:,6].sum()

#No of senior citizens
senior_citizens_len = len(senior_citizens)

#Average Working Hours of Senior Citiens
avg_working_hours = working_hours_sum / senior_citizens_len

print(avg_working_hours)

#People with high education

high = census[census[:, 1] > 10]

#People wth low education

low = census[census[:, 1] <= 10]

#Average pay of highly educated people
avg_pay_high = high[:, 7].mean()

#Average pay of lowly educated people
avg_pay_low = low[:, 7].mean()

print(avg_pay_high)
print(avg_pay_low)


