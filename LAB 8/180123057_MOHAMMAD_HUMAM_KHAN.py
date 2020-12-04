##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN.py

import math
import random
import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt


# Function to read adjusted closing price from csv file
def Read_Data():
	df = pd.read_csv('SBIN.NS.csv',usecols=['Adj Close'])
	StockPrices = []
	for i in df.index:
	    StockPrices.append(df['Adj Close'][i])
	return StockPrices    


# Function which returns value of mu and sigma calculated using given formulas
def Analyze_Data(StockPrices):
	# Calculating the log-return array
	u = []
	for i in range(1, len(StockPrices)):
		u.append(math.log(StockPrices[i]/StockPrices[i-1]))

	n = len(u)
	Eu = statistics.mean(u)

	sigma_square = 0
	for x in u:
		sigma_square += (x - Eu)**2

	sigma_square = sigma_square/(n-1)

	sigma = math.sqrt(sigma_square)
	mu = Eu + (sigma_square/2)

	print("mu = %s " % mu)
	print("sigma = %s \n" % sigma)

	return n,mu,sigma



#Function that simulates Stock price using Jump-Diffusion Process
def Estimate_Stock_Price(mu,sigma,S0,lamda,delta_t):
	EstimatedStockPrices = []
	EstimatedStockPrices.append(S0)
	Xk = math.log(S0)
	for i in range(1000):
		Z = np.random.normal(0,1)
		N = np.random.poisson(lamda*delta_t)
		if N == 0:
			M = 0
		else:	
			M = 0
			for i in range(N):
				Y = np.random.lognormal(mu, sigma)
				M += math.log(Y)

		drift = delta_t*(mu - (sigma**2)/2)
		diffusion = sigma*math.sqrt(delta_t)*Z
		jump = M
		Sk = math.exp(Xk + drift + diffusion + jump)
		EstimatedStockPrices.append(Sk)
		Xk = math.log(Sk)
		
	return EstimatedStockPrices


def PlotResults(EstimatedStockPrices,lamda,name):
	x = np.linspace(0,1001, 1001)	
	plt.figure(figsize = (30,10))
	plt.title("Sample Path of Simulated Stock Prices using Jump-Diffusion Process \n lambda = %s" % lamda, fontsize=20)
	plt.ylabel("Simulated Stock Prices", fontsize=15)
	plt.xlabel("Time Points", fontsize=15)
	plt.plot(x, EstimatedStockPrices)
	plt.savefig(name)
	plt.clf()



# Reading data from csv file
StockPrices = Read_Data()

# Calculate mu and sigma
n,mu,sigma = Analyze_Data(StockPrices)

# Initial Stock Price is closing stock price on Sep 30 i.e. S0 = Stock price on 30 Sep
S0 = StockPrices[n]
delta_t = 2


lamda = 0.01
EstimatedStockPrices = Estimate_Stock_Price(mu, sigma, S0, lamda, delta_t)
PlotResults(EstimatedStockPrices,lamda,"plot1")



lamda = 0.05
EstimatedStockPrices = Estimate_Stock_Price(mu, sigma, S0, lamda, delta_t)
PlotResults(EstimatedStockPrices,lamda,"plot2")



lamda = 0.1
EstimatedStockPrices = Estimate_Stock_Price(mu, sigma, S0, lamda, delta_t)
PlotResults(EstimatedStockPrices,lamda,"plot3")



lamda = 0.2
EstimatedStockPrices = Estimate_Stock_Price(mu, sigma, S0, lamda, delta_t)
PlotResults(EstimatedStockPrices,lamda,"plot4")
