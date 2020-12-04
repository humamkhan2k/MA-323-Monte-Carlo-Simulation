##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN_MarsagliaBray.py
import time
import random
import math
import numpy as np
import statistics
import matplotlib.pyplot as plt


#Function to calculate Normal density at a point x
def normal_density(mu, sigma, x):
	y = (1/math.sqrt(2 * math.pi * sigma)) * math.exp(-0.5 * ((x-mu)/sigma)**2)
	return y


#Function to sample number using Marsigla-Bray Method
def marsaglia_bray(total, rejected):
	X = 1.5
	while(X > 1):
		total = total + 1
		rejected = rejected + 1
		U1 = random.uniform(0,1)
		U2 = random.uniform(0,1)
		U1 = 2*U1 - 1
		U2 = 2*U2 - 1
		X = U1**2 + U2**2

	rejected = rejected - 1	

	Y = np.sqrt(-2*np.log(X)/X)
	Z1 = U1 * Y
	Z2 = U2 * Y	
	return Z1,Z2,total,rejected


#Calculating Frequencies for different intervals
def calculate_frequency(results, intervals, freq, sigma,rounds):
	for i in results:
		for j in range(100):
			if (i <= intervals[j]):
				freq[j] = freq[j] + 1
				break
	#scaling frequency values			
	for i in range(100):
		freq[i] = freq[i]*math.sqrt(sigma)/(2*(rounds/10))



##Plotting the results
def plot_result(intervals, freq,mu,sigma,mean,variance,exTime,fraction,name):
	
	plt.figure(figsize=(20,12))
	plt.title("Plot of numbers sampled from N(%s,%s) using Marsaglia-Bray Method \n Sample Mean = %s   ::::::   Sample Variance = %s \n Execution Time = %s \n Proportion of values rejected = %s" % (mu,math.floor(sigma**2),mean,variance, exTime,fraction), fontsize=20)
	plt.ylabel("Scaled frequency Values", fontsize=15)
	plt.xlabel("Intervals", fontsize=15)
	plt.plot(intervals[1:], freq[1:])
	plt.scatter(intervals[1:], freq[1:])

	r = np.linspace(mu-10,mu+10,5000,endpoint=True)
	y = []
	for i in range(5000):
		y.append(normal_density(mu, sigma, r[i]))
	plt.plot(r, y, color='r')
	plt.savefig(name)
	plt.clf()


#Function to simulate
def Simulate(generated_numbers,mu,sigma,rounds,time,rej_rate,name):
	intervals = []
	val = mu-10.0
	for i in range(100):
		intervals.append(round(val,2))
		val += 0.2	

	sample = []
	for i in range(len(generated_numbers)):
		sample.append(sigma*generated_numbers[i] + mu)

	mean = statistics.mean(sample)
	variance = statistics.variance(sample)
	print("Mean = %s" % mean)
	print("Variance = %s" % variance)
	print("Execution Time = %s" % time)
	print("Proportion of values rejected = %s \n" % rej_rate)

	freq = [0]*100
	calculate_frequency(sample, intervals, freq, sigma,2*rounds)
	plot_result(intervals, freq, mu, sigma, mean, variance, time, rej_rate, name)








#PART-1: 100 Rounds of Simulation

total = 0
rejected = 0	
sample = []	


# call to Marsigla-Bray function 
begin = time.time()

for i in range(50):
	[Z1,Z2,total, rejected] = marsaglia_bray(total,rejected)
	sample.append(Z1)
	sample.append(Z2)

end = time.time()	

time_taken = end-begin
rej_rate = rejected/total

Simulate(sample,0,1,50,time_taken,rej_rate,"marsaglia-bray_100_plot-1")                 #sampling from N(0,1)
Simulate(sample,0,math.sqrt(5),50,time_taken,rej_rate,"marsaglia-bray_100_plot-2")      #sampling from N(0,5)
Simulate(sample,5,math.sqrt(5),50,time_taken,rej_rate,"marsaglia-bray_100_plot-3")      #sampling from N(5,5)




#PART-2: 10000 Rounds of simulation
sample.clear()

total = 0
rejected = 0	

# call to Marsigla-Bray function 
begin = time.time()

for i in range(5000):
	[Z1,Z2,total, rejected] = marsaglia_bray(total,rejected)
	sample.append(Z1)
	sample.append(Z2)

end = time.time()	

time_taken = end-begin
rej_rate = rejected/total

Simulate(sample,0,1,5000,time_taken,rej_rate,"marsaglia-bray_10000_plot-1")                  #sampling from N(0,1)
Simulate(sample,0,math.sqrt(5),5000,time_taken,rej_rate,"marsaglia-bray_10000_plot-2")       #sampling from N(0,5)
Simulate(sample,5,math.sqrt(5),5000,time_taken,rej_rate,"marsaglia-bray_10000_plot-3")       #sampling from N(5,5)