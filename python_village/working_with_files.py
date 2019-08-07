"""
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""

# Open files
f = open('c://input.txt', 'r')
f2 = open('c://output.txt', 'w')

# Save lines as a list of strings
lineList = f.readlines()

# Prints only every other line into file2
for x in range(0, len(lineList)):
	if (x % 2 == 1):
		f2.write(lineList[x])
	
