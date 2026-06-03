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

print("-----------------------------")
print(df.head())    

print(df.info())

print(df.describe()) #this is used to get the statistical summary of the dataframe. One of best functions in pandas.
