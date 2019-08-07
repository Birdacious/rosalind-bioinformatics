"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

#Arranges the seqs and their names into lists
f = open('c://Users//Paul A. Hanson//Desktop//python_stuff//Rosalind//bioinfo_stronghold//level 4//consensus_and_profile//input.txt', 'r')
line_list = f.readlines()
name_list = []
seq_list = []
seq_string = ""

for i in range(len(line_list)):
	if (line_list[i].find('>') == 0):		#if name line
		name_list.append(line_list[i])
		if (seq_string != ""):
			seq_list.append(seq_string.replace('\n', ''))
			seq_string = ""
	else:									#if seq line
		seq_string += line_list[i]
seq_list.append(seq_string.replace('\n', ''))

"""
print(line_list)
print(name_list)
print(seq_list)
"""

#Profiling
#Builds profile 2D list of appropriate length
profile = [[], [], [], []]
for l in profile:
	for letter in seq_list[0]:
		l.append(0)
		
#Builds profile	
for seq in seq_list:
	for j in range(len(seq)):
		if (seq[j] == 'A'):
			profile[0][j] += 1
		elif (seq[j] == 'C'):
			profile[1][j] += 1
		elif (seq[j] == 'G'):
			profile[2][j] += 1
		elif (seq[j] == 'T'):
			profile[3][j] += 1


#Building consensus
consensus = ""
for i in range(len(profile[0])):
	greatest = 0
	for j in range(1, len(profile)):
		if (profile[j][i] > profile[greatest][i]):
			greatest = j
	if (greatest == 0):
		consensus += "A"
	if (greatest == 1):
		consensus += "C"
	if (greatest == 2):
		consensus += "G"
	if (greatest == 3):
		consensus += "T"
	

#Printing
#Prints consensus
print(consensus)

#Prints profile
print("A: " + str(profile[0]).replace('[', '').replace(']', '').replace(',', ''))
print("C: " + str(profile[1]).replace('[', '').replace(']', '').replace(',', ''))
print("G: " + str(profile[2]).replace('[', '').replace(']', '').replace(',', ''))
print("T: " + str(profile[3]).replace('[', '').replace(']', '').replace(',', ''))
