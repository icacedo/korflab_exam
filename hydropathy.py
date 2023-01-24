# https://www.ncbi.nlm.nih.gov/gene/173945
# https://www.uniprot.org/uniprotkb/P81299/entry
# https://rest.uniprot.org/uniprotkb/P81299.fasta

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fasta", help="amino acid sequence in fasta file format", \
	type=argparse.FileType('r'))
parser.add_argument("-window_size", help="size of sliding window given in n \
	bases", type=int, required=True)
args = parser.parse_args()

n = args.window_size

seq = ''
for line in args.fasta.readlines():
	line = line.rstrip()
	if line.startswith('>'): continue
	else:
		seq += line

print(seq)
for i in range(len(seq)):
	win = ''
	if len(seq[i:n+i]) == n:
		win = seq[i:n+i]
	else: continue
	print(win)










