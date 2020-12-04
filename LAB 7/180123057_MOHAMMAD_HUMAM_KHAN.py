##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN.py

import math
import numpy as np
import pandas as pd
import statistics


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



#Function that simulates Stock price using Geometric Brownian Motion
def Estimate_Stock_Price(mu,sigma,S0,T):
	S = []
	for i in range(1000):
		W = 0
		for j in range(T):
			W += np.random.normal(0,1)
		drift = T * (mu - (sigma**2)/2)
		diffusion = sigma*W
		S.append(S0 * math.exp(drift + diffusion))

	Sk = statistics.mean(S)
	return Sk


# Reading data from csv file
StockPrices = Read_Data()

# Calculate mu and sigma
n,mu,sigma = Analyze_Data(StockPrices)

# Initial Stock Price is closing stock price on Sep 30 i.e. S0 = Stock price on 30 Sep
S0 = StockPrices[n]


# T denotes number of working day after 30 September for which stock price needs to be estimated
# i.e. t0 = 30 Sep and value of "dt = 1 working day" 
# So for 7th Oct , T = 4
#    for 14th Oct, T = 9
#    for 21st Oct, T = 14



# Estimating Stock Price for 7th October 2020
T = 4
Actual_S1 = 190.70
Estimated_S1 = Estimate_Stock_Price(mu,sigma,S0,T)
print("Estimated Stock Price on 7th October 2020 = %s " % Estimated_S1)
print("Percentage Error = %s \n" % ((Estimated_S1 - Actual_S1)/Actual_S1 * 100))


# Estimating Stock Price for 14th October 2020
T = 9
Actual_S2 = 200.05
Estimated_S2 = Estimate_Stock_Price(mu,sigma,S0,T)
print("Estimated Stock Price on 14th October 2020 = %s " % Estimated_S2)
print("Percentage Error = %s \n" % ((Estimated_S2 - Actual_S2)/Actual_S2 * 100))


# Estimating Stock Price for 21st October 2020
T = 14
Actual_S3 = 203.75
Estimated_S3 = Estimate_Stock_Price(mu,sigma,S0,T)
print("Estimated Stock Price on 21st October 2020 = %s " % Estimated_S3)
print("Percentage Error = %s \n" % ((Estimated_S3 - Actual_S3)/Actual_S3 * 100))