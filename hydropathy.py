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

scores = {
	"I": 4.5,
	"V": 4.2,
	"L": 3.8,
	"F": 2.8,
	"C": 2.5,
	"M": 1.9,
	"A": 1.8,
	"G": -0.4,
	"T": -0.7,
	"S": -0.8,
	"W": -0.9,
	"Y": -1.3,
	"P": -1.6,
	"H": -3.2,
	"E": -3.5,
	"Q": -3.5,
	"D": -3.5,
	"N": -3.5,
	"K": -3.9,
	"R": -4.5
}

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
	total = 0
	for aa in win:
		total += scores[aa]
	avg = total/n
	# literally need tabs?
	print(i+1, win, "%.1f" % avg)




























