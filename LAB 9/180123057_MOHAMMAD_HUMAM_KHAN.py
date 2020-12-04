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


	

#Function that simulates Stock price using Geometric Brownian Motion
def EstimateStockPrice(mu,sigma,S0,n,delta_t):
	W = 0
	for j in range(n):
		W += np.random.normal(0,1)
	drift = n * delta_t * (mu - (sigma**2)/2)
	diffusion = sigma*W*math.sqrt(delta_t)
	Sk = S0 * math.exp(drift + diffusion)
	return Sk



##Function to calculate Payoff of Average Price Put Option
def AvgPriceOptionPayoff(mu,sigma,K,S0,delta_t,N):
	Sk = S0
	Sum = 0
	for i in range(1,N+1):
		Sk = EstimateStockPrice(mu,sigma,Sk,1,delta_t)
		Sum += Sk
	meanStockPrice = Sum/(N+1)	
	payoff = max(K - meanStockPrice, 0)
	return payoff



# Function to calculate mu and sigma of Price of Put Option
def CalculateOptionPrice(mu,sigma,K,S0,M,N,r,T):
	Payoff = []
	delta_t = T/N
	for i in range(M):
		payoff = AvgPriceOptionPayoff(mu,sigma,K,S0,delta_t,N)
		Payoff.append(payoff)
	Payoff = np.array(Payoff)
	OptionPrice = Payoff * math.exp(-r*T/365)
	mu_hat = statistics.mean(OptionPrice)
	sigma_hat = math.sqrt(statistics.variance(OptionPrice))
	return Payoff, mu_hat, sigma_hat	


# Function to estimate b for control variate method
def Estimate_b(X,Payoff):
	Nr = 0
	Dr = 0
	Mean_X = statistics.mean(X)
	Mean_Payoff = statistics.mean(Payoff)
	for i in range(M):
		Nr += (X[i]-Mean_X)*(Payoff[i]-Mean_Payoff)
		Dr += (X[i]-Mean_X)**2
	b = Nr/Dr	
	return b








# Reading data from csv file
StockPrices = Read_Data()

# Calculate mu and sigma
n,mu,sigma = Analyze_Data(StockPrices)

# Initial Stock Price is closing stock price on Sep 30 i.e. S0 = Stock price on 30 Sep
S0 = StockPrices[n]
K = 1.1*S0
T = 30
N = 300
M = 1000
r = 0.04      ##Prevailing Interest Rate




## *************  PART - 1  **************** ##

Payoff, mu_hat, sigma_hat = CalculateOptionPrice(mu,sigma,K,S0,M,N,r,T)

low = mu_hat - (1.96*sigma_hat/math.sqrt(M))
high = mu_hat + (1.96*sigma_hat/math.sqrt(M))

print("********************  PART - 1  ************************ \n")
print("Mean Option Price (mu_hat) = %s " % mu_hat)
print("Standard Deviation of Option Price (sigma_hat) = %s " % sigma_hat)
print("95%% Confidence Interval = [%s, %s] \n\n" % (low, high))






## ***************  PART - 2  ***************** ##

print("**********  PART - 2 (USING CONTROL VARIATES)  ********* \n")

## Here X is Price Standard Europen Put option payoff 
## Here Y is Price of Avg Price Put Option

X = []
for i in range(M):
	payoff = max(K - EstimateStockPrice(mu,sigma,S0,N,0.1), 0)
	X.append(payoff)
Mean_X = statistics.mean(X)



## Here using the payoff array obtained in Part-1 in line 124
b = Estimate_b(X,Payoff)
print("Value of b = %s" % b)


#Calculating Y i.e. Price of Average Price Put Option using control variate Technique
Y = []
for i in range(M):
	Y.append(Payoff[i] - b*(X[i]-Mean_X))

Y = np.array(Y)
Y = math.exp(-r*T/365)*Y


mu_hat = statistics.mean(Y)
sigma_hat = math.sqrt(statistics.variance(Y))

low = mu_hat - (1.96*sigma_hat/math.sqrt(M))
high = mu_hat + (1.96*sigma_hat/math.sqrt(M))

print("Mean Option Price (mu_hat) = %s " % mu_hat)
print("Standard Deviation of Option Price (sigma_hat) = %s " % sigma_hat)
print("95%% Confidence Interval = [%s, %s] \n\n" % (low, high))
 		