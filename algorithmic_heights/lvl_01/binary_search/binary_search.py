"""
Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.
Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
	And has to be the EARLIEST correct index if there are duplicates
"""

#Extracts the sorted array and the numbers to find
f = open('c://Users//Paul A. Hanson//Desktop//python_stuff//Rosalind//algorithmic_heights//level 1//binary_search//input.txt', 'r')
line_list = f.readlines()
sorted_array = line_list[2].split()
to_find = line_list[3].split()

#Traverses through to_find, each time using a binary search
#	to find stuff in sorted_array
index_list = []
for number in to_find:
	left = 0
	right = len(sorted_array) - 1
	mid = int((right + left) / 2)
	
	while (number != sorted_array[mid] and left <= right):
		if (number < sorted_array[mid]):
			right = mid - 1
			mid = int((right + left) / 2)
		elif (number > sorted_array[mid]):
			left = mid + 1
			mid = int((right + left) / 2)

	if (number == sorted_array[mid]):
		index_list.append(mid + 1) #add one because it wants 1-based index numbering for output
	else:
		index_list.append(-1)
		
print(str(index_list).replace('[', '').replace(',', '').replace(']', ''))
