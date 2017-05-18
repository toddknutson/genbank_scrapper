#!/bin/python3

# ---------------------------------------------------------------------
# Create a fasta file from tab-delimited file
#
# By Todd Knutson
# 2017-05-18
#
# USAGE:
# python3 genbank_make_fasta_from_table.py metadata.txt sequence accession definition > meta.fasta
#
# Above, "sequence", "accession", and "definition" are the names of the header row in the "metadata.txt" file,
# which correspond to the columns of text to be printed with each sequence.
#
# The contents are printed to STDOUT
# You can redirect contents using bash > operator.
# ---------------------------------------------------------------------

import sys


# Import a single or multi-genbank flat file
tab_delim_file = sys.argv[1] 
fasta_sequence = sys.argv[2]
fasta_names = sys.argv[3:]
#print(fasta_names)






with open(tab_delim_file, 'r') as table:
	header_line = table.readline().strip().split('\t')
	array = [line.strip().split('\t') for line in table]


# Get index value that matches the input sequence name in table (i.e. sequence column in table)
seq_idx = header_line.index(fasta_sequence)

# Get index values that matches the input header names in table (i.e. name columns in table)
head_idx = []
for k,v in enumerate(fasta_names):
	head_idx.append(header_line.index(v))




# Isolate the corresponding sequence column
seqs = [row[seq_idx] for row in array]


# Isolate the header names


# names = {i: [row[head_idx[i]] for row in array] for i in range(len(fasta_names))}
# print(type(names))


names = []
for i in range(len(fasta_names)):
	x = [row[head_idx[i]] for row in array]
	names.append(x)


# Print to screen (use > to print to file)
for i in range(len(seqs)):
	merged_name = []
	for j in range(len(names)):
		merged_name.append(names[j][i])
	
	print(">" + ' '.join(merged_name))
	print(seqs[i])
