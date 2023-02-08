# Schmitt and Herzel, 1997, Estimating the entropy of DNA sequences
# https://pubmed.ncbi.nlm.nih.gov/9344742/


import argparse
import math
'''
parser = argparse.ArgumentParser()
parser.add_argument("fasta", help="amino acid sequence in fasta file format", \
	type=argparse.FileType('r'))
parser.add_argument("-nmer_size", help="size of sliding window given in n \
	bases", type=int, required=True)
parser.add_argument("-entropy_threshold", help="size of sliding window given in n \
	bases", type=int, required=True)
args = parser.parse_args()

n = args.window_size
'''
# from c elegans genomic fasta
seq1 = 'AGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCC'
seq2 = 'ATTCTCGTAGATCAAACCGAAATGGGACATTCTGACACCA'
seq3 = 'ATCCGCGTAA'
#use log 2
print(math.log(8,2))

win = 3

for i in range(len(seq3)):
	if len(seq3[i:win+i]) < win: 
		continue
		
	raw_counts = {
		'A': 0, 'C': 0, 'G': 0, 'T': 0,
	}
	for j in seq3[i:win+i]:
		raw_counts[j] += 1
	print(raw_counts)
	print(seq3[i:win+i])


