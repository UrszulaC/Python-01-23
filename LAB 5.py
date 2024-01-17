import statistics
from statistics import mean
from statistics import median
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

#To extract information from this string, you'll need to split it by ',' as delimiter.
#Put the resulting List into a variable called grades.
#Tip: use the string's split function and pass it ',' as delimiter.
grades = data.split(',')
grades = list(map(int, grades))
print(grades)

#Display the minimum value of the grades.
#Tip: use the min() function
min_grades = min(grades)
print(min_grades)

#6.	Display the maximum value of grades.
#Tip: use the max() function

max_grades = max(grades)
print(max_grades)

#7.	Test your code and check if the values are correct.
#Did your code display 100 for the minimum value and 99 for the maximum?
#But how can 100 be a minimum? Any ideas why this is so. 
#Think about this before reading the next step.

#OK, as you've guessed it, we're dealing with a list of strings who just look like a List of numbers! That is why "100" is less than "17" because the first character '1' is the same but the second character '0' is less than the letter '3'.
#So, you need to cast every element of a List of strings into a List of integers. This is a common task and a hard one to code but the clever Python 3.0 gives us a tool called map to do this task. 
#The map function was not covered in the lectures, so we'll cover this useful function here in this lab.
#Just after splitting the string into a list of strings called grades, type:
#grades = list(map(int, grades))
#This line of code casts grades into a list of ints.

#10.	Now, run your code again. Does it give the right values for min and max (14 & 100)?

#11.	Display the average of grades to 2 decimal points.
#Tip: use the sum(), len() and round() functions.
grade_avarage = sum(grades)/len(grades)
print(round(grade_avarage, 2))

#12.	Import the statistics library.
#Tip: at the first line of your file type import statistics

#13.	Use the statistics' mean() function to get the average grade to 2 decimal places.
#Tip: use the statistics.mean() function
mean_value = round(mean(grade_avarage), 2)
print(mean_value)
#14.	Display the median values using the statistics.median() function.
#Note: this is not the same as the mean value. Please investigate what a median is if you're not sure.

median_result = median(grades)
print(median_result)

#15.	Use the string.format() function to display the min, max,average, mean() and median values.
print("The min grade is {min_grades}, max value is {max_grades}, avarage value {grade_avarage}, mean value is {mean_value} and median value is {median_result}.format" )