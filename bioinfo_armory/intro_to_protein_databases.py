"""
Given: The UniProt ID of a protein.
Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
"""

from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('Q5SLP9') #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
print(dir(record))
print(record.cross_references[0])
# ???
