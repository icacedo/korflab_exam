import argparse
import aa_comp as ac

parser = argparse.ArgumentParser()
parser.add_argument("fasta", type=argparse.FileType('r'))
args = parser.parse_args()

fasta = args.fasta

aa_comp = ac.get_aa_comp(fasta)

# doesn't care if two aa percents are the same
print('least common aa: ', min(aa_comp, key=aa_comp.get))
print('most common aa: ', max(aa_comp, key=aa_comp.get))

