##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN_q3.py

import random
import math
import numpy as np
import statistics
import matplotlib.pyplot as plt


##Values taken by random variable X
X = []
for i in range(1,11):
	X.append(i)

##Corresponding probabilities of values taken by X
p = [0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]


##Cummulative Frequency Distribution of Discrete Uniform Variable
q = []
for i in range(10):
	q.append((i+1)/10)


##This is original Cummulative Frequency Distribution of X
cdf = []
cdf.append(p[0])
for i in range(1,10):
	cdf.append(cdf[i-1]+p[i])



##Function to sample x from discrete Uniform Distribution (in place of g) 
##Algorithm used is that of q1 of Assignment 3.
def generate():
	u = random.uniform(0,1)
	for i in range(10):
		if u<=q[i]:
			return X[i]

def f(x):
	return p[x-1];

def g(x):
	return (1/10);	

##Acceptance-Rejection Algorithm used to generate samples from X
def accept_rej(c):
	result = []
	iterations = []
	it = 0
	for i in range(100000):
		it = it + 1
		x = generate()
		u = random.uniform(0,1)
		if u<=(f(x)/(c*g(x))):
			result.append(x)
			iterations.append(it)
			it = 0
	return result,iterations		


##Calculating Cummulative Frequency Distribution of generated sample
def cummulative_freq(result, cum_freq):
	for i in result:
		for j in range(i,11):
			cum_freq[j-1] = cum_freq[j-1]+1

	for i in range(10):
		cum_freq[i] = cum_freq[i]/len(result)


## Plotting both original Distribution and Distribution of generated sample for comparison
def plot_result(X, cum_freq, cdf, c, avg, length, name):
	plt.figure(figsize=(20,12))
	plt.legend(["Distribution of generated numbes", "Original Distribution"], loc ="lower right")
	plt.title("Cummulative Distribution Function Plot \n Value of c = %s \n Avg number of times steps 1 repeated = %s \n Number of generated Numbers = %s" % (c,avg,length), fontsize=20)
	plt.xlabel("Values taken by X", fontsize=15)
	plt.ylabel("Normalized Cummulative Frequency of X values", fontsize=15)
	plt.plot(X,cum_freq,color='b')
	plt.scatter(X, cum_freq)
	plt.plot(X,cdf,color='r')
	plt.savefig(name)
	plt.clf()


##PART-1
c = 5
cum_freq = [0]*10;
[result, iterations] = accept_rej(c)
cummulative_freq(result, cum_freq)
avg = statistics.mean(iterations)
plot_result(X, cum_freq, cdf, c, avg, len(result), "q3_part1")



##PART-2
c = 10
cum_freq = [0]*10;
[result, iterations] = accept_rej(c)
cummulative_freq(result, cum_freq)
avg = statistics.mean(iterations)
plot_result(X, cum_freq, cdf, c, avg, len(result), "q3_part2")



##PART-2
c = 15
cum_freq = [0]*10;
[result, iterations] = accept_rej(c)
cummulative_freq(result, cum_freq)
avg = statistics.mean(iterations)
plot_result(X, cum_freq, cdf, c, avg, len(result), "q3_part3")

