

#In this code file. I will be doing some work with pandas to get a better understanding of how they work and how to use them in my projects. I will be creating some pandas dataframes and performing some operations on them to get insights from the data. I will also be saving the insights in a text file for future reference.

#First i will import the necessary libraries and then i will create some pandas dataframes to work with.
import pandas as pd
import numpy as np

#unlike numpy project, i will be consider some data which can be used for predicition.
#We will be working on a dataset available on kaggle which is about the perforance of students in grade of maths by DEV ANSODARIYA.
#https://www.kaggle.com/datasets/devansodariya/student-performance-data is url of the dataset.
#I will be downloading the dataset and then loading it into a pandas dataframe to work with it.
#I will be using the read_csv function to load the dataset into a pandas dataframe.

df = pd.read_csv('student_data.csv')

#Now that we have loaded the dataset into a pandas dataframe, we can start performing some operations on it to get insights from the data.
#First i will check the shape of the dataframe to see how many rows and columns it has.

print(df.shape)

#data unstanding
print("-----------------------------")
print(df.head()) 
print(df.info())
print(df.describe()) #this is used to get the statistical summary of the dataframe. One of best functions in pandas.
print(df.columns)

#preprocessing the data
#checking for missing values
print(df.isnull().sum())    
if df.isnull().sum().any():
    print("There are missing values in the dataframe.")
else:    print("There are no missing values in the dataframe.")     

#As we can see there are no missing values in the dataframe, we can proceed with the analysis of the data.

#We will be doing some analysis on the data to get insights from it. We will be dealing with "average score for all subject"
avg_score = df[['G1', 'G2', 'G3']].mean(axis=1)
print(avg_score)
df['avg_score'] = avg_score
print(df.head())    

#we have avg score now if a student is at 40 percentile or above he is considered as pass otherwise fail. We will be creating a function named pass_fail and use avg_score as input and generate a new np array contain 0 and 1 where 1 is for pass and 0 is for fail. We will then add this new array as a new column in the dataframe and print the first 5 rows of the dataframe to see the new column.
def pass_fail(score):
    if score >= 40:
        return 1
    else:
        return 0    
    
df['pass_fail'] = avg_score.apply(pass_fail)    
print(df.head())

#Avg class score:
print(df['pass_fail'].mean(), " is the average class score.")

#Highest and lowest score in the class:
print(avg_score.max(), " is the highest score in the class")
print(avg_score.min(), " is the lowest score in the class")

print(df['G1'].mean(), " is the average score of G1")
print(df['G2'].mean(), " is the average score of G2")
print(df['G3'].mean(), " is the average score of G3")   

#compare the average score of G1, G2 and G3 to see if there is any improvement in the scores of the students over time.
print("Average score of G1: ", df['G1'].mean())
print("Average score of G2: ", df['G2'].mean())
print("Average score of G3: ", df['G3'].mean()) 

if df['G1'].mean() < df['G2'].mean() < df['G3'].mean():
    print("There is an improvement in the scores of the students over time.")
else:
    print("There is no improvement in the scores of the students over time.")

#Now lets have a look at coorelation between gender and score of the students. We will be using the groupby function to group the data by gender and then we will be calculating the average score for each gender and then we will be comparing the average scores of both genders to see if there is any difference in the scores of the students based on their gender.

gender_comparison = df.groupby('sex')['avg_score'].mean()
print(gender_comparison)

#Now lets see effects of study time on the scores of the students. We will be using the groupby function to group the data by study time and then we will be calculating the average score for each study time and then we will be comparing the average scores of each study time to see if there is any difference in the scores of the students based on their study time.
study_time_comparison = df.groupby('studytime')['avg_score'].mean()
print(study_time_comparison)

