import argparse
import warnings

parser = argparse.ArgumentParser()
parser.add_argument("list", help="enter a comma separated list of \
	values with type int and/or float")
args = parser.parse_args()

values = args.list

'''
Why does this work?
https://stackoverflow.com/questions/26430861/make-pythons-warnings-warn-not-mention-itself
def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
	return '%s:%s: %s: %s\n' % (filename, lineno, category.__name__, message)
warnings.formatwarning = warning_on_one_line
warnings.warn()
warnings.formatwarning is called by warnings.warn
'''

vals_list = []
for x in values.split(','):
	try:
		x = float(x)
		vals_list.append(x)
	except ValueError as e:
		warnings.warn(f'{e}', category=Warning, stacklevel=2)

print('input: ', vals_list)

sorted_vals = sorted(vals_list)

print('sorted: ', sorted_vals)

total = 0
for n in sorted_vals:
	total += n

mean = total/len(sorted_vals)

if len(sorted_vals)%2 == 0:
	mid = len(sorted_vals)/2
	mid = int(mid)
	median = (sorted_vals[mid-1] + sorted_vals[mid])/2
else:
	mid = (len(sorted_vals)-1)/2
	mid = int(mid)
	median = sorted_vals[mid]

total = 0
for n in sorted_vals:
	total += (n - mean) ** 2
var = total/len(sorted_vals)
stdev = var ** (1/2)

print('mean: ', mean, 'median: ', median, 'stdev: ', stdev)







