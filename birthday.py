import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("class_size", help="number of students in a hypothetical \
	classroom", type=int)
args = parser.parse_args()

class_size = args.class_size

# only need ONE PAIR

npairs = int((class_size*(class_size-1))/2)

students = [random.randint(1,365) for x in range(class_size)]

print(students)


