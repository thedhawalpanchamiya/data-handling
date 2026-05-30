#In This FIle i will be doing some work with numpy and pandas to get a better understanding of how they work and how to use them in my projects.

#First i will import the necessary libraries and then i will create some numpy arrays and pandas dataframes to work with.
import numpy as np
 
#Creating a data of 100 students with random marks in 5 subjects (P,C,B,M,E)
#Creating a numpy array of shape (100,5) with random integers between 0 and 100

data = np. random.randint(0, 101, (100, 5))

#for this data, I will be looking at 5 entries to get a better understanding of how the data looks like and what kind of operations i can perform on it.
print(data[:5],data.shape) #printing the first 5 rows and all columns except the last one (which is the total marks)

# for a student, we need to find out did he pass or fail, for that we will be using the following criteria:
# if the student has scored more than 40 in all subjects, then he is considered as passed, otherwise he is considered as failed.
# we will be creating a new column in the data array which will contain the total marks of each student and another column which will contain the pass or fail status of each student.  

#Creating a new column for total marks
total_marks_percentage = (np.sum(data, axis=1))/5 #summing up the marks of each student across all subjects and dividing it by 5 to get the percentage of marks obtained by each student.
data = np.hstack((data, total_marks_percentage.reshape(-1,1))) #hstack is used to stack the total marks column to the original data array 
 
print("---------------------------------------------------------------------------------------- ")
print(data[:5],data.shape)

#By considering your this data, we will create a new data array that contains pass or fail of same studnent in same order as the original data array. We will be using the following criteria to determine pass or fail:
# if the student has scored more than 40 in all subjects, then he is considered as passed, otherwise he is considered as failed.
pf_status = np.where(data >= 40, 1, 0)

print("---------------------------------------------------------------------------------------- ")

print(pf_status[:5],pf_status.shape) #printing the first 5 rows and all columns of the pass or fail status array

#if all values in a row of pf_status are 1, then the student is considered as passed, otherwise he is considered as failed. We will be creating a new column in the data array which will contain the pass or fail status of each student based on the values in the pf_status array.
final_pf_status = np.array([1 if np.all(row == 1) else 0 for row in pf_status]) #applying the condition to each row of the pf_status array to get the final pass or fail status of each student
data = np.hstack((data, final_pf_status.reshape(-1,1))) #hstack is used to stack the final pass or fail status column to the original data array

print("---------------------------------------------------------------------------------------- ")
print(data[:5],data.shape) #printing the first 5 rows and all columns of the final data array which contains the marks, total marks percentage and pass or fail status of each student      

#Now lets calculate the average marks of each subject and the average total marks percentage of all students. We will be using the following functions to calculate the average:
average_marks = np.mean(data[:,:5], axis=0) #calculating the average marks of each subject by taking the mean of the first 5 columns of the data array
average_total_marks_percentage = np.mean(data[:,5]) #calculating the average total marks percentage of all students by taking the mean of the 6th column of the data array
print("---------------------------------------------------------------------------------------- ")
print("Average Marks of Each Subject: ", average_marks) #printing the average marks of each subject
print("Average Total Marks Percentage of All Students: ", average_total_marks_percentage) #printing the average total marks percentage of all students

# Now lets create a new classifacation factor as students with 85 above marks in all subejcts knwon as "Excellent", students with marks between 70 and 85 in all subjects known as "Good", students with marks between 40 and 70 in all subjects known as "Average" and students with marks below 40 in any subject known as "Poor". We will be creating a new column in the data array which will contain the classification factor of each student based on the marks obtained by each student in all subjects.

classification_factor = np.array(["Excellent" if np.all(row[:5] >= 85) else "Good" if np.all((row[:5] >= 70) & (row[:5] < 85)) else "Average" if np.all((row[:5] >= 40) & (row[:5] < 70)) else "Poor" for row in data]) #applying the condition to each row of the data array to get the classification factor of each student based on the marks obtained by each student in all subjects
data = np.hstack((data, classification_factor.reshape(-1,1))) 

print("---------------------------------------------------------------------------------------- ")
print(data[:5],data.shape) #printing the first 5 rows and all columns of

#Find top 10 students based on total marks percentage and print their marks, total marks percentage, pass or fail status and classification factor. We will be using the following functions to find the top 10 students:
top_10_students = data[np.argsort(data[:,5])[-10:]] #sorting

print("---------------------------------------------------------------------------------------- ")
print("Top 10 Students Based on Total Marks Percentage: ")
print(top_10_students) #printing the marks, total marks percentage, pass or fail status
