import matplotlib.pyplot as plt
import numpy as np

def f(x,theta):
    return 1 - np.exp(((-1)*x)/theta)

def X(u,theta):
    return (-1)*theta*(np.log(1-u))

def actualMean(theta):
    return theta

def actualVariance(theta):
    return theta*theta

def expMean(x_vals):
    return np.mean(x_vals)

def expVariance(x_vals):
    return np.var(x_vals)

def update_freq(freq,x):
    if x < 10:
        index = int(np.floor(10*x))
        freq[index] += 1

def plotFunction(theta):
    x = np.linspace(0,10,5000,endpoint=True)
    plt.plot(x,f(x,theta),color = 'r')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Actual Distribution Function')
    plt.show()
    plt.clf()

def plotGraphs(n,theta,file):

    # x_vals would be 100 intervals of size 0.1 each 
    # storing the midpoint of each interval
    intervals = []
    curr_mid = 0.05
    interval_size = 0.1
    for i in range(100):
        intervals.append(curr_mid)
        curr_mid += interval_size

    # freq would be the frequency of the values in each interval
    # initially frequencies are set to 0 
    freq = [0]*100

    # stores the values of xi
    x_vals = []

    # generating n random values between 0 and 1
    # assuming that the random number generator genrates numbers uniformly
    # as the values are generated uniformly it can be assumed that the distribution is U[0,1]
    for i in range(n):
        u = np.random.rand()
        x = X(u,theta)
        x_vals.append(x)
        update_freq(freq,x)

    # stores the cumulative frequency
    cum_freq = [0]*100
    cum_freq[0] = freq[0]
    for i in range(1,100):
        cum_freq[i] = cum_freq[i-1] + freq[i]
    
    # Calculating the mean and variance
    actual_mean = actualMean(theta)
    experimental_mean = expMean(x_vals)
    actual_variance = actualVariance(theta)
    experimental_variance = expVariance(x_vals)

    file.write("Data for " + str(n) + " rounds\n")
    file.write("Actual Mean = " + str(actual_mean) + "\n")
    file.write("Experimental Mean = " + str(experimental_mean) + "\n")
    file.write("Actual Variance = " + str(actual_variance) + "\n")
    file.write("Experimental Variance = " + str(experimental_variance) + "\n")

    # Display the graphs
    plt.plot(intervals,cum_freq,color = 'b',label = 'experimental')
    plt.title('Distribution Function using genrated values (n = ' + str(n) + ')')
    plt.xlabel('values of x')
    plt.ylabel('Cumulative Frequency')
    plt.legend(loc = 'lower right')
    plt.show()
    plt.clf()

def main():
    theta = 1
    file = open("180123021_q2_data.txt","a")
    plotFunction(1)
    plotGraphs(1000,1,file)
    plotGraphs(10000,1,file)
    plotGraphs(100000,1,file)
    
if __name__ == '__main__':
    main()





#P
    if rounds==100000:
        x = np.linspace(0, 5, rounds)
        y = -x/theta
        y = np.exp(y)
        y = 1-y 
        for i in range(100):
            cum_freq[i] = cum_freq[i]/rounds

        plt.figure(figsize=(20,14)) 
        plt.plot(intervals, cum_freq, color='b', label='experimental')
        plt.plot(x,y,color='r', label='actual')
        plt.title("Comparison of Cummulative Distribution Function of \n generated numbers and actual CDF \n Sample Mean = %s ---- Actual Mean = 0.5 \n Sample Variance = %s ---- Actual Variance = 0.25 \n Number of Rounds in Simulation = %s" % (mean, variance,rounds), fontsize=20)
        plt.xlabel("Range of Intervals of xi", fontsize=20)
        plt.ylabel("Cummulative Frequencies of xi in given range", fontsize=20)
        plt.savefig("Comparison")
        plt.clf()

