import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number", help="compute factorial of a given number, \
	must be an integer", type=int)
args = parser.parse_args()

num = args.number

fac = 1
for i in range(1,num+1):
	fac *= i

sfac = str(fac)
if len(sfac) > 12:
	print("{:e}".format(fac))
else:
	print(fac)

























