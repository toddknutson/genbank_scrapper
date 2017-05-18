# `genbank_scrapper`: GenBank Metadata Extraction Tool

2017-05-18  
By Todd Knutson


## Introduction

The purpose of this tool is to extract metadata from a Genbank (or multi-Genbank) file. With a Genbank file as input, you can quickly extract some of the metadata associated with the header and features sections. Not all metadata is extracted, but much of the useful information is extracted. This will generate a tab-delimited text file as output.  

Then, using this tab-delimited text file, you can use a second script to quickly generate a fasta file. 

## Install and Run

The only dependency is `python3`, which is pre-installed on most computers. 

Download the repository and move into the directory. Make sure you make the python scripts executable.

```
cd genbank_scrapper
chmod u+x genbank_scrapper.py
chmod u+x genbank_make_fasta_from_table.py
```


To run the scripts: 

```
cd genbank_scrapper
python3 genbank_scrapper.py genbank_file.txt > metadata.txt
python3 genbank_make_fasta_from_table.py metadata.txt sequence accession definition collection_year country > metadata.fasta 
```





