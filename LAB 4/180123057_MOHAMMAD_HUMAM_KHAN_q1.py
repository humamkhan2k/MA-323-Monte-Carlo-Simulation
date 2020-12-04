##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN_q1.py

import random
import math
import math
import numpy as np
import statistics
import matplotlib.pyplot as plt




##Function to calculate value of f(x)
def f(x, alpha_1, alpha_2):
	y = (math.gamma(alpha_1 + alpha_2)/(math.gamma(alpha_1)*math.gamma(alpha_2))) * (x**(alpha_1 - 1)) * ((1-x)**(alpha_2 - 1))
	return y



#Function to calculate x* i.e. point at which maximum value of f is achieved
def calculate_x_star(alpha_1, alpha_2):
	c = (alpha_1 - 1)/(alpha_1 + alpha_2 - 2)
	return c



##Actual Function to generate numbers according to acceptance-rejection method
def Accept_Rej(c, alpha_1, alpha_2):
	results = []
	iterations = []
	it = 0
	for i in range(100000):
		it = it+1
		x = random.uniform(0,1)
		u = random.uniform(0,1)
		if u <= (f(x,alpha_1,alpha_2)/c):
			results.append(round(x,5))
			iterations.append(it)
			it = 0
	return results,iterations		



#Calculating Frequencies for different intervals
def calculate_frequency(results, intervals, freq):
	for i in results:
		for j in range(100):
			if (i <= intervals[j]):
				freq[j] = freq[j] + 1
				break
	for i in range(100):
		freq[i] = freq[i]*100/len(results)



##Plotting the results
def plot_result(intervals, freq, c, avg, length, number_avg, name, alpha_1, alpha_2):
	
	plt.figure(figsize=(20,12))
	plt.title("Histogram showing Frequencies of Generated Numbers  \n Value of c = %s :::: Avg number of times steps 1 repeated = %s  \n Average value of Generated Numbers = %s \n Number of generated numbers = %s \n alpha_1 = %s ; alpha_2 = %s" % (c, round(avg,5), number_avg, length, alpha_1, alpha_2), fontsize=15)
	plt.ylabel("Scaled frequency Values", fontsize=15)
	plt.xlabel("Intervals", fontsize=15)
	plt.bar(intervals, freq, width=0.01, edgecolor='black', color='lightgreen')

	r = np.linspace(0,1,5000,endpoint=True)
	y = []
	for i in range(5000):
		y.append(f(r[i], alpha_1, alpha_2))
	plt.plot(r, y, color='r')
	plt.savefig(name)
	plt.clf()




##Base Function to simulate the whole experiment
def Simulate(alpha_1, alpha_2, name):

	#Generating the intervals
	intervals = []
	val = 0.01
	for i in range(100):
		intervals.append(round(val,2))
		val += 0.01	


	freq = [0]*100  
	print("%s  %s" % (alpha_1, alpha_2))                                                            #Declaring frequency array
	print("1/B(alpha_1, alpha_2) = %s" % (math.gamma(alpha_1 + alpha_2)/(math.gamma(alpha_1)*math.gamma(alpha_2))))
	x_star = calculate_x_star(alpha_1, alpha_2)  
	print("x* = %s" % x_star)                                                   #Calculating x*
	c = f(x_star, alpha_1, alpha_2)                                             #Calculating c
	print("c = %s" % c)
	print("\n")
	[results, iterations] = Accept_Rej(c, alpha_1, alpha_2)                     #Calling function to generate randon numbers

	avg = statistics.mean(iterations)                                           ##Calculating the average of Number of times step 1 was repeated

	number_avg = statistics.mean(results)                                       ##Calculating the average of generated numbers

	calculate_frequency(results, intervals, freq)
	plot_result(intervals, freq, c, avg, len(results), number_avg, name, alpha_1, alpha_2)






Simulate(1,3, "Figure_1")
Simulate(4,7, "Figure_2")
Simulate(2,2, "Figure_3")
Simulate(6,3, "Figure_4")
Simulate(4,1, "Figure_5")




