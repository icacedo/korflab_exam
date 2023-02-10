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

win = 4
# only look at local
for i in range(len(seq3)):
	if len(seq3[i:win+i]) < win: 
		continue

	freq = {
		'A': 0, 'C': 0, 'G': 0, 'T': 0,
	}
	for j in seq3[i:win+i]:
		freq[j] += 1/win
	
	H = 0
	for k in freq:
		if freq[k] == 0:
			p = -math.inf
		else:
			p = freq[k]
			H += p*math.log(p,2)
	print(H)
	print(seq3[i:win+i])



