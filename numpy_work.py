#In this file i will be dealing with numpy arrays and their operations. I will be using the numpy library to perform various operations on arrays such as creation, manipulation, and mathematical operations.

#You are given a dataset of 100,000 students and their marks in 5 subjects.
#Your goal is to analyze performance efficiently using NumPy 
import numpy as np

np.random.seed(42) 

# Generate random marks for 100,000 students in 5 subjects
data = np.random.randint(0, 101, (100000, 5))

# Calculate the average marks for each student    
average_marks = np.mean(data, axis=1)

# Calculate the overall average marks for each subject
overall_average = np.mean(data, axis=0)

# Calculate the number of students who scored above 90 in each subject
above_90 = np.sum(data > 90, axis=0)

print("Average marks for each student:", average_marks)
print("Overall average marks for each subject:", overall_average)
print("Number of students who scored above 90 in each subject:", above_90)


