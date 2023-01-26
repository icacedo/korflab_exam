import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fasta", type=argparse.FileType('r'))
args = parser.parse_args()

fasta = args.fasta

# only works with uppercase letters ACTG

def get_aa_comp(fasta):

	seq = ''
	for line in fasta.readlines():
		if line.startswith('>'): continue
		line = line.rstrip()
		seq += line

	aa_comp = {
		'A': 0,
		'C': 0,
		'T': 0,
		'G': 0
	}

	total = 0
	for aa in seq:
		aa_comp[aa] += 1
		total += 1

	for aa in aa_comp:
		aa_comp[aa] = round(aa_comp[aa]/total, 2)

	return aa_comp

