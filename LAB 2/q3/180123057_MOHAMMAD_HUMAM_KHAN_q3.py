## The dependencies needed are : python3, numpy, matplotlib
## To run the code type following command in terminal : python3 180123057_MOHAMMAD_HUMAM_KHAN_q3.py


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math


#Function to generate sequence of numbers according to given formula
def Generator(freq,intervals,rounds,plot_name):
	x_values = []
	for i in range (rounds):
		u = random.uniform(0,1)
		xi = (1/2)*(1 - math.cos(math.pi * u))
		x_values.append(xi)
		u = 0.00
		#Calculating Cummulative Frequencies
		for i in range(101):
			if (xi <= u):
				freq[i] = freq[i] + 1	
			u = round(u + 0.01, 4)	


	#Calculating mean and variance
	mean = round(np.mean(x_values), 5)
	variance = round(np.var(x_values), 5)
	
    #Plotting the graphs
	plt.figure(figsize=(20,12))
	plt.title("Frequency Distribution Function of generated numbers \n Sample Mean = %s \n Sample Variance = %s \n Number of Rounds in Simulation = %s" % (mean, variance,rounds), fontsize=20)
	plt.xlabel("Range of Intervals", fontsize=20)
	plt.ylabel("Cummulative Frequencies of xi in given range", fontsize=20)
	plt.plot(intervals, freq, color='b')
	plt.savefig(plot_name)
	plt.clf()		



#Function to plot Actual CDF
def Actual_CDF(rounds, i):
	x = np.linspace(0, 1, rounds)
	y = np.sqrt(x)
	y = np.arcsin(y)
	y = (2/math.pi) * y
	plt.figure(figsize=(20,12))
	plt.title("Actual CDF of F(x) \n Number of Rounds in simulation = %s" % rounds, fontsize=20)
	plt.xlabel("x-values", fontsize=20)
	plt.ylabel("F(x)-values", fontsize=20)
	plt.scatter(x,y)
	plt.savefig("180123057_q3_Actual_CDF_%s" % i)
	plt.clf()




# Intervals contain 100 intervals of size 0.05 each
# storing mid-point of the interval

intervals = []
freq = []
val = 0.00
for i in range(101):
	intervals.append(val)
	val += 0.01
	freq.append(0)


Generator(freq,intervals,1000,"180123057_q3_Plot_1")
Actual_CDF(1000, 1)

Generator(freq,intervals,10000,"180123057_q3_Plot_2")
Actual_CDF(10000, 2)

Generator(freq,intervals,100000,"180123057_q3_Plot_3")
Actual_CDF(100000, 3)


