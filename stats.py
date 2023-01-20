import argparse
import warnings
import sys

parser = argparse.ArgumentParser()
parser.add_argument("list", help="enter a comma separated list of \
	values with type int and/or float")
args = parser.parse_args()

values = args.list

print(values)

'''
Why does this work?
https://stackoverflow.com/questions/26430861/make-pythons-warnings-warn-not-mention-itself
def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
	return '%s:%s: %s: %s\n' % (filename, lineno, category.__name__, message)
warnings.formatwarning = warning_on_one_line
warnings.warn()
warnings.formatwarning is called by warnings.warn
'''


for x in values.split(','):
	try:
		x = float(x)
		print(x)
	except ValueError as e:
		warnings.warn(f'{e}', stacklevel=2)
		#warnings.formatwarning()
		#warnings.warn("\'" + x + "\'" + " is not a number", stacklevel=2)
		# warning vs exception?
		# what is writing a warning to a file? the file defaults to sys.stderr
		# print(f'{e}')

#sys.stderr.write("al;dfja")
#print(file=sys.stderr)









