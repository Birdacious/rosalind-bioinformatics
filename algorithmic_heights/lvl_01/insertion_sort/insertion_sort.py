"""
Given: A positive integer n≤103 and an array A[1..n] of integers.
Return: The number of swaps performed by insertion sort algorithm on A[1..n].
"""

f = open('c://Users//Paul A. Hanson//Desktop//python_stuff//Rosalind//algorithmic_heights//level 1//insertion_sort//input.txt', 'r')
line_list = f.readlines()
array = line_list[1].split()
print (array)

counter = 0
temp = 0
for i in range(1, len(array)):
	k = i
	while (k > 0 and int(array[k]) < int(array[k - 1])):
		temp = array[k]
		array[k] = array[k - 1]
		array[k - 1]  = temp
		counter += 1
		k = k - 1
		
print (array)
print (counter)
	
