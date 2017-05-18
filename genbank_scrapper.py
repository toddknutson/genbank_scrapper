#!/panfs/roc/itascasoft/python3/3.4-conda/bin/python3

# ---------------------------------------------------------------------
# Scrape multi-genbank flat file
#
# By Todd Knutson
# 2016-10-28
#
# Input a GenBank flat file (single text file with multiple records listed)
# Output relevant information in tab-delimited text format
#
# Usage:
# ./get_genbank_info.py <mutli-genbank.txt>
#
# The contents are printed to STDOUT
# You can redirect contents using bash > operator. For example:
# ./get_genbank_info.py mutli-genbank.txt > results.txt
# ---------------------------------------------------------------------





import sys


# Import a single or multi-genbank flat file
genbank_file = sys.argv[1]


with open(genbank_file, 'r') as gb:
	results = {}
	record_counter = -1
	accession = None
	definition = None
	host = None
	segment = None
	gene = None
	serotype = None
	isolate = None
	isolation_source = None
	strain = None
	note = None
	organism = None
	country = None
	taxid = None
	genbank_date = None
	collection_date = None
	collection_year = None
	journal = None
	sequence = ''
	identical_to = None
	pubmed = None
	for line in gb:
		line = line.strip()
		if "LOCUS" in line:
			record_counter += 1
			line = line.split()
			genbank_date = line[7]

		if "DEFINITION" in line:
			line = line.split('DEFINITION')[1]
			definition = line.strip()
			for line in gb:
				if line.startswith("ACCESSION"):
					# get rid of period at end of definition
					if definition.endswith("."):
						definition = definition[:-1]
					break
				else:
					line = line.strip()
					definition = definition + " " + line
					if definition.endswith("."):
						definition = definition[:-1]

		if "reference sequence is identical to" in line:
			line = line.split('reference sequence is identical to')[1]
			line = line.split()[0]
			line = line.split('.')[0]
			identical_to = line.strip()

		if "VERSION" in line:
			line = line.split('VERSION')[1]
			accession = line.strip()
			
		if "JOURNAL" in line:
			line = line.split('JOURNAL')[1]
			journal = line.strip()

		if "PUBMED" in line:
			line = line.split('PUBMED')[1]
			pubmed = line.strip()

		if "/country=" in line: 
			line = line.split('"')
			country = line[1]

		if "/host=" in line:
			line = line.split('"')
			host = line[1].title()

		if "/segment=" in line:
			line = line.split('"')
			segment = line[1]

		if "/gene=" in line:
			line = line.split('"')
			gene = line[1]

		if "/serotype=" in line:
			line = line.split('"')
			serotype = line[1]

		if "/isolate=" in line:
			line = line.split('"')
			isolate = line[1]

		if "/isolation_source=" in line:
			line = line.split('"')
			isolation_source = line[1].title()

		if "/strain=" in line:
			line = line.split('"')
			strain = line[1]

		if "/note=" in line:
			line = line.split('"')
			note = line[1]

		if '/db_xref="taxon:' in line:
			line = line.split('taxon:')[1]
			line = line.split('"')
			taxid = line[0]

		if 'ORGANISM' in line:
			line = line.split('ORGANISM')[1]
			organism = line.strip()

		if "/collection_date=" in line:
			line = line.split('"')
			collection_date = str(line[1])
			if len(collection_date) == 4:
				collection_year = str(collection_date)
			elif '-' in collection_date:
				collection_year = str(collection_date.split('-')[-1])

		if 'ORIGIN' in line:
			for line in gb:
				line = line.strip()
				if line[0].isdigit():
					line_list = line.split()
					line_list = line_list[1:len(line_list)]
					curr_sequence = ''.join(line_list)
					sequence = sequence + curr_sequence
					sequence = sequence.upper()
				else:
					break

		if line == "//":
			# Record current data into dictionary
			results[record_counter] = [accession, definition, pubmed, sequence, host, segment, gene, serotype, isolate, isolation_source, strain, note, organism, country, collection_year, collection_date, genbank_date, journal, taxid, identical_to]
			# Then clear current data
			accession = None
			definition = None
			pubmed = None
			sequence = ''
			host = None
			segment = None
			gene = None
			serotype = None
			isolate = None
			isolation_source = None
			strain = None
			note = None
			organism = None
			country = None
			taxid = None
			genbank_date = None
			collection_date = None
			collection_year = None
			journal = None
			identical_to = None





	
# Print results to screen (direct to file using bash >)
print('accession\tdefinition\tpubmed\tsequence\thost\tsegment\tgene\tserotype\tisolate\tisolation_source\tstrain\tnote\torganism\tcountry\tcollection_year\tcollection_date\tgenbank_date\tjournal\ttaxid\tidentical_to')

for k,v in enumerate(results):
	curr_list = results[v]
	print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (curr_list[0], curr_list[1], curr_list[2], curr_list[3], curr_list[4], curr_list[5], curr_list[6], curr_list[7], curr_list[8], curr_list[9], curr_list[10], curr_list[11], curr_list[12], curr_list[13], curr_list[14], curr_list[15], curr_list[16], curr_list[17], curr_list[18], curr_list[19]))
	
