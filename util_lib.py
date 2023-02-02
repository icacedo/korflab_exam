def parse_fasta(file1):

	while True:
		line = file1.readline()
		line = line.rstrip()
		# idk why it prints an empty line at the end
		yield line
		
		if not line:
			break


























