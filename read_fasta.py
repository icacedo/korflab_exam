import util_lib as ul
import sys

fasta = sys.argv[1]
file1 = open(fasta, 'r')

for line in ul.parse_fasta(file1):
	print(line)


