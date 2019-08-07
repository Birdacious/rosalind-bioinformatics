"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated
"""

# Separates the file into two arrays:
# one of sequence names, and one of the sequences themselves.
# The indices correspond.
f = open('c://Users//Paul A. Hanson//Desktop//input.txt', 'r')
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

print(line_list)
print(name_list)
print(seq_list)


# Finds the sequence with the greatest gc content from the seq_array
# and then prints that seq's name along with the calculated gc % value 
def find_gc_percent(seq):
	return (seq.count('G') + seq.count('C')) / len(seq)
	
greatest_so_far_index = 0
for i in range(1, len(seq_list)):
	if (find_gc_percent(seq_list[i]) > find_gc_percent(seq_list[greatest_so_far_index])):
		greatest_so_far_index = i
		
print(name_list[greatest_so_far_index][1:] +
	str(100 * find_gc_percent(seq_list[greatest_so_far_index])))
