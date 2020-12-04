##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN_q1.py


import random
import math
import numpy as np
import statistics
import matplotlib.pyplot as plt



#Calculating Cummulative Frequencies
def cummulative_freq(results, intervals):
	cum_freq = [0]*5001
	for i in results:
		for j in range(5001):
				if (i <= intervals[j]):
					cum_freq[j] = cum_freq[j] + 1
	#for i in range(5001):
	#	cum_freq[i] = cum_freq[i]/len(results)

	return cum_freq



c = []
c.append(0)
for i in range(1,10000,2):
	c.append(i)


q = []
x=0
for i in range(5001):
	q.append(i/5000)


##Actual Algorithm to sample numbers from given Discrete Distribution 
x = []
iterations = 0
for i in range(10000):
	iterations = iterations+1
	u = random.uniform(0,1)
	for i in range(1,5001):
		if q[i-1]<u and u<=q[i]:
			x.append(c[i])
			break

cum_freq = cummulative_freq(x, c)


##Writing the output to file

file = open("q1_ans.txt", "w")
for i in x:
	file.write("%s \n" % i)
file.close()


##Plotting the results to verify that generated numbers are from uniform distribution
plt.figure(figsize=(20,12))
plt.plot(c[1:],cum_freq[1:])
plt.title("Cummulative Frequency Distribution Plot", fontsize=20)
plt.xlabel("Points in Discrete Distribution", fontsize=15)
plt.ylabel("Cummulative Frequency", fontsize=15)
plt.savefig("q1")
plt.clf()


