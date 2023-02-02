import sys

fasta = sys.argv[1]

file1 = open(fasta, 'r')


while True:
	line = file1.readline()
	line = line.rstrip()
	# idk why it prints an empty line at the end
	print(line)
	if not line:
		break


























