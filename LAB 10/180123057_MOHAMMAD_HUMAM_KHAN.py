##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN.py

import math
import random
import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt


# Function that implements the Monte Carlo Estimator
def Estimate(M):
	Y = []
	for i in range(M):
		u = np.random.uniform(0,1)
		u = math.sqrt(u)
		Y.append(math.exp(u))

	estimate = statistics.mean(Y)
	std_dev = math.sqrt(statistics.variance(Y))
	return estimate,std_dev


# Function that implements the Monte Carlo Estimator using Antithetic Variates
def Estimate_Antithetic(M):
	Y_cap = []
	for i in range(M):
		u = np.random.uniform(0,1)
		u1 = math.sqrt(u)
		u2 = math.sqrt(1-u)
		Y_cap.append((math.exp(u1) + math.exp(u2))/2)

	estimate = statistics.mean(Y_cap)
	std_dev = math.sqrt(statistics.variance(Y_cap))	
	return estimate,std_dev



# Function to simulate and print results
def Simulate(M):
	print("\n************** M = %s ************** \n" % M)
	IM,sigma = Estimate(M)
	low = IM - (1.96*sigma/math.sqrt(M))
	high = IM + (1.96*sigma/math.sqrt(M))
	length1 = high - low
	print("Mean(IM) = %s" % IM)
	print("Standard Deviation(sigma) = %s" % sigma)
	print("95%% confidence interval for IM = [%s, %s] " % (low, high))
	print("Length of 95%% Confidence Interval for IM = %s \n" % length1)
	

	IM_cap,sigma_cap = Estimate_Antithetic(M)
	low = IM_cap - (1.96*sigma_cap/math.sqrt(M))
	high = IM_cap + (1.96*sigma_cap/math.sqrt(M))
	length2 = high - low
	print("Mean(IM_cap) = %s" % IM_cap)
	print("Standard Deviation(sigma_cap) = %s" % sigma_cap)
	print("95%% confidence interval for IM_cap = [%s, %s] " % (low, high))
	print("Length of 95%% Confidence Interval for IM_cap = %s \n" % length2)
	

	ratio = length1/length2
	print("Ratio of length of confidence intervals = %s" % ratio)
	print("\n\n")




Simulate(100)
Simulate(1000)
Simulate(10000)
Simulate(100000)
