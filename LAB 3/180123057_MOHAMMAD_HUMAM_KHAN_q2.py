##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN_q2.py

import random
import math
import numpy as np
import statistics
import matplotlib.pyplot as plt




##Function to calculate value of f(x)
def f(x):
	y = 20*x*((1-x)**3)
	return y

##Distribution Function of f(x)
def F(x):
	y = 10 * x**2 - 20 * x**3 + 15 * x**4 - 4 * x**5
	return y



##Actual Function to generate numbers according to acceptance-rejection method
def Accept_Rej(results, iterations):
	it = 0
	for i in range(100000):
		it = it+1
		x = random.uniform(0,1)
		u = random.uniform(0,1)
		if u <= (f(x)/c):
			results.append(round(x,5))
			iterations.append(it)
			it = 0
	return results,iterations		



#Calculating Cummulative Frequencies
def cummulative_freq(results, intervals, cum_freq):
	for i in results:
		for j in range(100):
			if (i <= intervals[j]):
				cum_freq[j] = cum_freq[j] + 1
	for i in range(100):
		cum_freq[i] = cum_freq[i]/len(results)



##Plotting the results
def plot_result(intervals, cum_freq, c, avg, length, number_avg, name):
	#plt.legend(["Distribution of generated numbes", "Original Distribution"], loc ="lower right")
	plt.figure(figsize=(20,12))
	plt.title("Cummulative Distribution Function of Generated Numbers  \n Value of c = %s \n Avg number of times steps 1 repeated = %s  \n Average value of Generated Numbers = %s \n Number of generated numbers = %s" % (c, avg, number_avg, length), fontsize=15)
	plt.ylabel("Normalized Cummulative frequency Values", fontsize=15)
	plt.xlabel("Intervals", fontsize=15)
	plt.plot(intervals,cum_freq)
	plt.scatter(intervals, cum_freq)

	r = np.linspace(0,1,5000,endpoint=True)
	y = []
	for i in range(5000):
		y.append(F(r[i]))
	plt.plot(r, y, color='r')	
	plt.savefig(name)
	plt.clf()




##Declaring the required arrays
results = []
iterations = []
cum_freq = [0]*100

intervals = []
val = 0.01
for i in range(100):
	intervals.append(round(val,2))
	val += 0.01


		

##PART-1 
c = 2.109375
[results, iterations] = Accept_Rej(results, iterations)

##Calculating the average of Number of times step 1 was repeated
avg = statistics.mean(iterations)

##Calculating the average of generated numbers
number_avg = statistics.mean(results)

cummulative_freq(results, intervals, cum_freq)
plot_result(intervals, cum_freq, c, avg, len(results), number_avg, "q2_part1")




##PART-2 
results.clear()
iterations.clear()
cum_freq = [0]*100
c = 5
[results, iterations] = Accept_Rej(results, iterations)

##Calculating the average of Number of times step 1 was repeated
avg = statistics.mean(iterations)

##Calculating the average of generated numbers
number_avg = statistics.mean(results)

cummulative_freq(results, intervals, cum_freq)
plot_result(intervals, cum_freq, c, avg, len(results), number_avg, "q2_part2")




##PART-3 
results.clear()
iterations.clear()
cum_freq = [0]*100
c = 10
[results, iterations] = Accept_Rej(results, iterations)

##Calculating the average of Number of times step 1 was repeated
avg = statistics.mean(iterations)

##Calculating the average of generated numbers
number_avg = statistics.mean(results)

cummulative_freq(results, intervals, cum_freq)
plot_result(intervals, cum_freq, c, avg, len(results), number_avg, "q2_part3")