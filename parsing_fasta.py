# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 
'''Pseudo-code:
-recognize the file records using on the '>' sign
-return only the records that do not contain the string 'OS=Homo sapiens'
-write those record in a new file
-find the organism name in those records 
-find the lenght of the strings
-print source organism and sequence length'''
import re
def parsing_fasta():
	seq_fasta = open('sprot_prot.fasta', 'r')
	l = seq_fasta.readlines()
	n = open('new_file.txt', 'w') #prepare the new file in order to be written 
	seq = ''
	header = ''
	
	for line in seq_fasta:
		if line[0] == '>':	
			if line.find("Homo sapiens") == -1: #it means there is no Homo Sapiens in the first line
           		 	header = line
		else:
           		if header:
           			seq = seq + line
	if header:
		record = header + seq			 
		n.write(header + seq)  		
	for line in seq_fasta:
		x = line.split("\n") #split the different lines
		organism = re.search("OS=*([^GN]+)", x[0]).group(0) #find the organism
		for i in range(1, lex(x)):
			seq = seq + x[i]
		print("source organism: %s, sequence length: %d" % (org, len(seq)) )	
parsing_fasta()		#finds the lenght
	
				



				
