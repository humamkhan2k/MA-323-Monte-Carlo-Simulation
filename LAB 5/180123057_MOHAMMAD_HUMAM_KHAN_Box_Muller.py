##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN_BoxMuller.py
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


#Function to sample number using Box-Muller Method
def box_muller():
	u1 = random.uniform(0,1)
	u2 = random.uniform(0,1)
	R = -2 * np.log(u1)
	V = 2 * math.pi * u2
	z1 = np.sqrt(R) * np.cos(V)
	z2 = np.sqrt(R) * np.sin(V)
	return z1,z2



#Calculating Frequencies for different intervals
def calculate_frequency(results, intervals, freq, sigma,rounds):
	for i in results:
		for j in range(100):
			if (i <= intervals[j]):
				freq[j] = freq[j] + 1
				break
	for i in range(100):
		freq[i] = freq[i]*math.sqrt(sigma)/(2*(rounds/10))




##Plotting the results
def plot_result(intervals, freq,mu,sigma,mean,variance,exTime,name):
	
	plt.figure(figsize=(20,12))
	plt.title("Plot of numbers sampled from N(%s,%s) using Box-Muller Method \n Sample Mean = %s   ::::::   Sample Variance = %s \n Execution Time = %s" % (mu,math.floor(sigma**2),mean,variance, exTime), fontsize=20)
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
def Simulate(generated_numbers,mu,sigma,rounds,time,name):
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
	print("Execution Time = %s \n" % time)

	freq = [0]*100
	calculate_frequency(sample, intervals, freq, sigma,2*rounds)
	plot_result(intervals, freq, mu, sigma, mean, variance, time, name)





#100 Rounds of Simulation

sample = []	

begin = time.time()

for i in range(50):
	[z1,z2] = box_muller()
	sample.append(z1)
	sample.append(z2)

end = time.time()

time_taken = end - begin

Simulate(sample,0,1,50,time_taken,"box-muller_100_plot-1")                  #sampling from N(0,1)
Simulate(sample,0,math.sqrt(5),50,time_taken,"box-muller_100_plot-2")       #sampling from N(0,5)
Simulate(sample,5,math.sqrt(5),50,time_taken,"box-muller_100_plot-3")       #sampling from N(5,5)





#10000 Rounds of simulation
sample.clear()
begin = 0
end = 0

begin = time.time()

for i in range(5000):
	[z1,z2] = box_muller()
	sample.append(z1)
	sample.append(z2)

end = time.time()

time_taken = end - begin

Simulate(sample,0,1,5000,time_taken,"box-muller_10000_plot-1")                #sampling from N(0,1)
Simulate(sample,0,math.sqrt(5),5000,time_taken,"box-muller_10000_plot-2")     #sampling from N(0,5)
Simulate(sample,5,math.sqrt(5),5000,time_taken,"box-muller_10000_plot-3")     #sampling from N(5,5)