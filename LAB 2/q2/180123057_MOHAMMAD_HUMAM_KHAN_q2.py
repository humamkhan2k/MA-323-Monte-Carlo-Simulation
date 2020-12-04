## The dependencies needed are : python3, numpy, matplotlib
## To run the code type following command in terminal : python3 180123057_MOHAMMAD_HUMAM_KHAN_q2.py


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math


#Function to generate sequence of numbers according to given formula
def Generator(theta,cum_freq,intervals,rounds,plot_name):
	x_values = []
	for i in range (rounds):
		u = random.uniform(0,1)
		xi = -1*theta*math.log(1-u)
		x_values.append(xi)
		u = 0.00
		#Calculating Cummulative Frequencies
		for i in range(100):
			if (xi <= u):
				cum_freq[i] = cum_freq[i] + 1
			u = round(u + 0.05, 2)		

	#Calculating mean and variance		
	mean = round(np.mean(x_values), 5)
	variance = round(np.var(x_values), 5)	

	#Plotting the graphs
	plt.figure(figsize=(20,12))
	plt.title("Frequency Distribution Function of generated numbers \n Sample Mean = %s ---- Actual Mean = 0.5 \n Sample Variance = %s ---- Actual Variance = 0.25 \n Number of Rounds in Simulation = %s" % (mean, variance,rounds), fontsize=20)
	plt.xlabel("Range of Intervals of xi", fontsize=20)
	plt.ylabel("Cummulative Frequencies of xi in given range", fontsize=20)
	plt.plot(intervals, cum_freq, color='b')
	plt.savefig(plot_name)
	plt.clf()	
	
	



#Function to plot Actual CDF 
def Actual_CDF(rounds, i):
	x = np.linspace(0, 5, rounds)
	y = -x/theta
	y = np.exp(y)
	y = 1-y
	plt.figure(figsize=(20,12))
	plt.title("Actual CDF of F(x) \n Number of rounds in Simulation = %s" % rounds, fontsize=20)
	plt.xlabel("x-values", fontsize=20)
	plt.ylabel("F(x)-values", fontsize=20)
	plt.scatter(x,y)
	plt.savefig("180123057_q2_Actual_CDF_%s" % i)
	plt.clf()




# Intervals contain 100 intervals of size 0.05 each
# storing mid-point of the interval

intervals = []
freq = [0]*100
val = 0.00
for i in range(100):
	intervals.append(val)
	val += 0.05

theta = 0.5

Generator(theta,freq,intervals,1000,"180123057_q2_Plot_1")
Actual_CDF(1000, 1)

Generator(theta,freq,intervals,10000,"180123057_q2_Plot_2")
Actual_CDF(10000, 2)

Generator(theta,freq,intervals,100000,"180123057_q2_Plot_3")
Actual_CDF(100000, 3)


