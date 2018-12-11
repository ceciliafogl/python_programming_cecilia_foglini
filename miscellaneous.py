# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
L = list(range(21,40))
# print the numbers of the list that are even
print(L[::2])
# print the numbers of the list that are multiples of 3
for m in L:  
	if  % 3 == 0:
		print(m)
# Exercise 2
# Print the last two elements of L 
print(L[-1:])
# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = [1, 2, 3]
for i in range(10):
    	if i in L:
		print('%d is in the list' % i)
    	else:
		print('%d not found' % i)    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 
fastafile= open('sprot_prot.fasta','r')
reading_line= fastafile.readline()
print(reading_line)
half_string=reading_line.split('OS=')[-1:]  
print(half_string)



# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
second_element = str(half_string-strip('[]')
second_element = half_string[1].split(' ')
print(second_element[0] + second_element[1])



# Exercise 6
print(s[::-1]) #reverse the string s = 'asor rosa'

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
L.sort()
print(L)
# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
new_list = L.sorted()
# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
f = open('newfile.txt', 'w')#write every element on the row separated by a tab, and then go to another line to print the next row
f.write("2 \t 4 \n3 \t 6")

