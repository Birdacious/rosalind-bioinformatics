"""
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif N{P}[ST]{P},
	output its given access ID
	followed by a list of locations in the protein string where the motif can be found.
"""

import urllib.request

#Makes lists of the protein names, links to their fasta seqs, and trimmed seqs
f = open('c://Users//Paul A. Hanson//Desktop//python_stuff//Rosalind//bioinfo_stronghold//level 4//finding_a_protein_motif//input.txt', 'r')
protein_names = f.readlines()
for i in range(len(protein_names)):
	protein_names[i] = protein_names[i].replace('\n', '')
print(protein_names)

protein_links = []
for i in range(len(protein_names)):
	protein_links.append('https://www.uniprot.org/uniprot/' + protein_names[i] + '.fasta')
print(protein_links)
	
protein_seqs = []
for i in range(len(protein_links)):
	fasta = str(urllib.request.urlopen(protein_links[i]).read())
	trimmed_seq = fasta[fasta.find('\\n'):].replace('\\n', '').replace("'", '')
	protein_seqs.append(trimmed_seq)
print(protein_seqs)


#Traverses list of sub_seqs, printing the name and then the indices where
#	the motif is found in the main_seq
for i in range(len(protein_seqs)):
	motif_positions = []
	for j in range(len(protein_seqs[i])):
		if (protein_seqs[i][j] == 'N'):
			if (protein_seqs[i][j+1] != 'P'):
				if (protein_seqs[i][j+2] == 'S' or protein_seqs[i][j+2] == 'T'):
					if (protein_seqs[i][j+3] != 'P'):
						motif_positions.append(j + 1)
	if (motif_positions != []):
		print(protein_names[i])
		print(str(motif_positions).replace('[', '').replace(']', '').replace(',', ''))
