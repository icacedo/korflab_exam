import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("class_size", help="number of students in a hypothetical \
	classroom", type=int)
parser.add_argument("n_sims", help="number of simulations to run", type=int)
args = parser.parse_args()

class_size = args.class_size
n_sims = args.n_sims

# only need ONE PAIR

# what does "solve analytically" mean?
def birthday_sim(class_size):
	students = [random.randint(1,365) for x in range(class_size)]

	for i in range(class_size):
		for j in range(i, class_size):
			if i == j: continue
			elif students[i] == students[j]:
				yield 1 #, students[i], students[j]
			else:
				yield 0 #, students[i], students[j]

# probability of AT LEAST two

matches = 0
for i in range(n_sims):
	prev = 0
	for i in birthday_sim(class_size):
		if i == 1 and prev == 0:
			# check tuples
			#print(i[0], i[1], i[2])
			matches += 1
			prev += 1

print("prob of same birthday: ", matches/n_sims)











