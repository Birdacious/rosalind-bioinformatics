"""
Given: A simple graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the degree of vertex i.
"""

#Makes a list of all the ints in the dataset
f = open('c://Users//Paul A. Hanson//Desktop//python_stuff//Rosalind//algorithmic_heights//level 1//degree_array//input.txt', 'r')
num_list = []
for line in f:
	temp_list = line.split()
	num_list += temp_list
print(num_list)

#Makes a list of all the vertices
#And parallel list to store their amount of connections
vertices = []
connections = []
for i in range(int(num_list[0])):
	vertices.append(i + 1)
	connections.append(0)
print(vertices)
print(connections)

#Traverses num_list (starting after the first two items n and m),
#	adding 1 to the score of each vertex each time it appears
for i in range(2, len(num_list)):
	connections[int(num_list[i]) - 1] += 1
print(str(connections).replace("[", "").replace(",", "").replace("]", ""))
