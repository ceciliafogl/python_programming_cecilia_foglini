# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
10 times
input: numbers from the keyboard 
-put them in a list;
-calculate the average (sum/length)
output: list of numbers, average of numbers
 
'''
import math

def average_function():
	vector_list = []
	for i in range(0,11):
		vector = int(input("Type the components of a vector: "))
		vector_list.append(vector)
	print(vector_list)
	for x in vector_list:
		average = sum(int(x))/float(len(x))
		print(average)
		
