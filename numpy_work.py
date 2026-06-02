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


#standard deviation of marks in each subject and total marks percentage of all students. We will be using the following functions to calculate the standard deviation:
std_dev_marks = np.std(data[:,:5].astype(float), axis=0) #calculating the standard deviation of marks in each subject by taking the std of the first 5 columns of the data array
std_dev_total_marks_percentage = np.std(data[:,5].astype(float)) #calculating the standard deviation of total marks percentage of all students by taking the std of the 6th column of the data array
print("---------------------------------------------------------------------------------------- ")
print("Standard Deviation of Marks in Each Subject: ", std_dev_marks) #printing the standard deviation of marks in each subject
print("Standard Deviation of Total Marks Percentage of All Students: ", std_dev_total_marks_percentage) #printing the standard deviation of total marks percentage of all students      


#Variance of marks in each subject and total marks percentage of all students. We will be using the following functions to calculate the variance:

variance_marks = np.var(data[:,:5].astype(float), axis=0) #calculating the variance of marks in each subject by taking the var of the first 5 columns of the data array
variance_total_marks_percentage = np.var(data[:,5].astype(float)) #calculating the variance of total marks percentage of all students by taking the var of the 6th column of the data array
print("---------------------------------------------------------------------------------------- ")
print("Variance of Marks in Each Subject: ", variance_marks) #printing the  variance of marks in each subject       

print("Variance of Total Marks Percentage of All Students: ", variance_total_marks_percentage) #printing the variance of total marks percentage of all students     

#Coorelation martix between marks of each subject and total marks percentage of all students. We will be using the following functions to calculate the coorelation matrix:
correlation_matrix = np.corrcoef(data[:,:6].astype(float).T) #calculating the coorelation matrix between marks of each subject and total marks percentage of all students by taking the corr
#coef of the first 6 columns of the data array and transposing it to get the coorelation between each subject and total marks percentage
print("---------------------------------------------------------------------------------------- ")
print("Coorelation Matrix Between Marks of Each Subject and Total Marks Percentage of All Students: ")
print(correlation_matrix) #printing the coorelation matrix between marks of each subject and total marks percentage of all students 

#Normalization of marks in each subject and total marks percentage of all students. We will be using the following functions to normalize the marks:
normalized_marks = (data[:,:5].astype(float) - np.min(data[:,:5].astype(float), axis=0)) / (np.max(data[:,:5].astype(float), axis=0) - np.min(data[:,:5].astype(float), axis=0)) #normalizing the marks in each subject by applying the min-max normalization formula to the first 5 columns of the data array
normalized_total_marks_percentage = (data[:,5].astype(float) - np.min(data[:,5].astype(float))) / (np.max(data[:,5].astype(float)) - np.min(data[:,5].astype(float))) #normalizing the total marks percentage of all students by applying the min-max normalization formula to the 6th column of the data array
print("---------------------------------------------------------------------------------------- ")
print("Normalized Marks in Each Subject: ")
print(normalized_marks) #printing the normalized marks in each subject
print("Normalized Total Marks Percentage of All Students: ")
print(normalized_total_marks_percentage) #printing the normalized total marks percentage of all students        

#Using z score normalization to normalize the marks in each subject and total marks percentage of all students. We will be using the following functions to normalize the marks using z score normalization:
z_score_normalized_marks = (data[:,:5].astype(float) - np.mean(data[:,:5].astype(float), axis=0)) / np.std(data[:,:5].astype(float), axis=0) #normalizing the marks in each subject by applying the z score normalization formula to the first 5 columns of the data array
z_score_normalized_total_marks_percentage = (data[:,5].astype(float) - np.mean(data[:,5].astype(float))) / np.std(data[:,5].astype(float)) #normalizing the total marks percentage of all students by applying the z score normalization formula to the 6th column of the data array
print("---------------------------------------------------------------------------------------- ")
print("Z Score Normalized Marks in Each Subject: ")         
print(z_score_normalized_marks) #printing the z score normalized marks in each subject
print("Z Score Normalized Total Marks Percentage of All Students: ")
print(z_score_normalized_total_marks_percentage) #printing the z score normalized total marks percentage of all students

#Vectorized operations to calculate the pass or fail status of each student based on the marks obtained by each student in all subjects. We will be using the following functions to calculate the pass or fail status using vectorized operations:
vectorized_pf_status = np.where(data[:,:5].astype(float) >= 40, 1, 0) #calculating the pass or fail status of each student based on the

marks obtained by each student in all subjects by applying the condition to the first 5 columns of the data array using vectorized operations
final_vectorized_pf_status = np.array([1 if np.all(row == 1) else 0 for row in vectorized_pf_status]) #applying the condition to each row of the vectorized_pf_status array to get the final pass or fail status of each student based on the marks obtained by each student in all subjects using vectorized operations
print("---------------------------------------------------------------------------------------- ")
print("Pass or Fail Status of Each Student Based on Marks Obtained in All Subjects Using Vectorized Operations: ")
print(final_vectorized_pf_status) #printing the pass or fail status of each student based on the marks obtained by each student in all subjects using vectorized operations         


#Loop Based Operations to calculate the pass or fail status of each student based on the marks obtained by each student in all subjects. We will be using the following functions to calculate the pass or fail status using loop based operations:
loop_based_pf_status = [] #initializing an empty list to store the pass or fail status of each student based on the marks obtained by each student in all subjects using loop based operations
for row in data: #iterating     
    if np.all(row[:5].astype(float) >= 40): #checking if the marks obtained by each student in all subjects are greater than or equal to 40
        loop_based_pf_status.append(1) #if the condition is true, then the student is considered as passed and we append 1 to the list
    else:
        loop_based_pf_status.append(0) #if the condition is false, then the student is considered as failed and we append 0 to the list
print("---------------------------------------------------------------------------------------- ")
print("Pass or Fail Status of Each Student Based on Marks Obtained in All Subjects Using Loop Based Operations: ")
print(loop_based_pf_status) #printing the pass or fail status of each student based on the marks obtained by each student in all subjects using loop based operations   

