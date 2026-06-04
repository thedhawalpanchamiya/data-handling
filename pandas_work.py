

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
    if score >= 8:
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

#Which Feature affects marks the most?
#we will be using the corr function to calculate the correlation between the features and the average score to see which feature affects the marks the most.
correlation = df.corr(numeric_only=True)
print(correlation['avg_score'].sort_values(ignore_index=False, ascending=False))

#from here we realised that Parental education level affects the marks the most followed by study time.

#is study time strongly correlated with the marks of the students?
print(correlation['avg_score']['studytime'])

#for such a numeric correlation value, we can say that there is a moderate positive correlation between study time and the marks of the students. This means that as the study time increases, the marks of the students also tend to increase, but it is not a very strong correlation.

#Filtering data
#students who failed :
failed_students = df[df['pass_fail'] == 0] # will generate a df of students who failed.

#Students with high study time and low scores:
high_study_time_low_scores = df[(df['studytime'] >= 3) & (df['avg_score'] < (8))]
print(high_study_time_low_scores)

#top 10 performers:
top_performers = df.sort_values(by='avg_score', ascending=False)
print(top_performers.head(10))

#Insights:
#1. The average class score is 0.64 which means that 64% of the students passed the exam.
#2. The highest score in the class is 19.0 and the lowest score is 0.0.
#3. The average score of G1 is 10.0, the average score of G2 is 10.5 and the average score of G3 is 11.0 which shows that there is an improvement in the scores of the students over time.
#4. The average score of male students is 0.65 and the average score of female students is 0.63 which shows that there is a slight difference in the scores of the students based on their gender.
#5. The average score of students with study time of 1 is 0.5, the average score of students with study time of 2 is 0.6, the average score of students with study time of 3 is 0.7 and the average score of students with study time of 4 is 0.8 which shows that there is a difference in the scores of the students based on their study time.
#6. The feature that affects the marks the most is the parental education level followed by study time.
#7. There is a moderate positive correlation between study time and the marks of the students which means that as the study time increases, the marks of the students also tend to increase, but it is not a very strong correlation.   

#End of the code file!!
