##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN.py

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
from scipy.stats import multivariate_normal
import random
import math
import numpy as np
import statistics





#Function to calculate Normal density at a point x
def normal_density(mu, sigma, x):
	y = (1/math.sqrt(2 * math.pi * sigma)) * math.exp(-0.5 * ((x-mu)/sigma)**2)
	return y



#Calculating Frequencies for different intervals
def calculate_frequency(results, intervals, freq, sigma,rounds):
	for i in results:
		for j in range(len(intervals)):
			if (i <= intervals[j]):
				freq[j] = freq[j] + 1
				break
	for i in range(len(intervals)):
		freq[i] = freq[i]*math.sqrt(sigma)/(2*rounds/10)



##Plotting the results
def plot_result(intervals,freq,mu,sigma,a,var,name):
	
	plt.figure(figsize=(20,12))
	plt.title("Marginal Density Plot of %s \n a = %s" % (var,a),fontsize=20)
	plt.ylabel("Scaled frequency Values", fontsize=15)
	plt.xlabel("Intervals", fontsize=15)
	plt.plot(intervals[1:], freq[1:])
	plt.scatter(intervals[1:], freq[1:])

	r = np.linspace(mu-4*sigma,mu+4*sigma,5000,endpoint=True)
	y = []
	for i in range(5000):
		y.append(normal_density(mu, sigma, r[i]))
	plt.plot(r, y, color='r')
	plt.savefig(name)
	plt.clf()



#Function to Plot 3D density for different values of a
def plot3D_density(X1,X2,mu1,mu2,sigma1,sigma2,a,rounds,name):
	
	X_start = mu1 - 4*sigma1
	X_end = mu1 + 4*sigma1
	Y_start = mu2 - 4*sigma2
	Y_end = mu2 + 4*sigma2
	X_intervals = np.linspace(X_start,X_end,100,endpoint=True)
	Y_intervals = np.linspace(Y_start,Y_end,100,endpoint=True)
	XY_freq = np.array([[0]*100]*100)


	X_interval_size = (X_end-X_start)/100
	Y_interval_size = (Y_end-Y_start)/100

	#Calculating frequency of intervals
	for i in range(rounds):
		j = math.floor((X1[i]-X_start)/X_interval_size)
		k = math.floor((X2[i]-Y_start)/Y_interval_size)
		if j>=100 or k>=100:
			continue
		XY_freq[j][k] = XY_freq[j][k] + 1


	#Plotting Simulated Density 

	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.set_title("Bivariate Density of Simulated Points (X) in 3D \n a = %s" % a)
	ax.set_xlabel('X axis')
	ax.set_ylabel('Y axis')
	ax.set_zlabel('Z axis')

	X_intervals, Y_intervals = np.meshgrid(X_intervals, Y_intervals)
	ax.plot_surface(X_intervals, Y_intervals, XY_freq,cmap=cm.coolwarm)
	plt.savefig(name+"_3")
	plt.clf()


	##Plotting Actual Bivariate Normal density 

	X = np.linspace(X_start,X_end, 1000,endpoint=True)
	Y = np.linspace(Y_start,Y_end, 1000,endpoint=True)
	X, Y = np.meshgrid(X, Y)

	mu = np.array([5, 8])

	#Handling Corner Case for a = 1
	if a!=1:
		Sigma = np.array([[ 1. , 2.0*a], [2.0*a,  4.]])
	
	if a==1:
		Sigma = np.array([[ 1. , 2.0*0.99999], [2.0*0.99999,  4.]])

	pos = np.empty(X.shape + (2,))
	pos[:, :, 0] = X
	pos[:, :, 1] = Y

	F = multivariate_normal(mu, Sigma)
	Z = F.pdf(pos)

	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.set_title("Actual Bivariate Density of X in 3D \n a = %s" % a)
	ax.set_xlabel('X axis')
	ax.set_ylabel('Y axis')
	ax.set_zlabel('Z axis')
	ax.plot_surface(X,Y,Z,cmap=cm.coolwarm,linewidth=0, antialiased=True)
	plt.savefig(name+"_4")
	plt.clf()





#Function to Simulate Bivariate Normal
def Simulate(a,name):

	mu1 = 5
	mu2 = 8

	sigma1 = 1
	sigma2 = 2

	rho = a

	rounds = 1000
	Z1 = np.random.normal(0,1,rounds)
	Z2 = np.random.normal(0,1,rounds)

	X1 = mu1 + sigma1*Z1
	X2 = mu2 + (rho * sigma2 * Z1) + (math.sqrt(1 - rho**2) * sigma2 * Z2) 


	intervals = []
	val = mu1-5
	for i in range(50):
		intervals.append(round(val,2))
		val += 0.2	


	freq = [0]*50
	calculate_frequency(X1, intervals, freq, sigma1,rounds)
	plot_result(intervals, freq, mu1, sigma1,a,"X1",name+"_1")


	intervals.clear()
	val = mu2-8
	for i in range(80):
		intervals.append(round(val,2))
		val += 0.2	


	freq = [0]*80
	calculate_frequency(X2, intervals, freq, sigma2,rounds)
	plot_result(intervals, freq, mu2, sigma2,a,"X2",name+"_2")


	plot3D_density(X1,X2,mu1,mu2,sigma1,sigma2,a,rounds,name)








#Calling function to simulate for different values of a
Simulate(-0.5,"plot1")
Simulate(0,"plot2")
Simulate(0.5,"plot3")
Simulate(1,"plot4")


