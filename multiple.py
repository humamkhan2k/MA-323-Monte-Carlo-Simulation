import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readData():
    data = pd.read_csv('SBIN.NS.csv',usecols=['Date','Adj Close'])
    prices = []
    dates = []
    for ind in data.index:
        dates.append(data['Date'][ind])
        prices.append(data['Adj Close'][ind])
    return dates,prices

def computeMuSigma(s):
    u = []
    for i in range(1,len(s)):
        u.append(np.log(s[i]/s[i-1]))

    E = np.mean(u)
    n = len(u)

    var = 0
    for i in range(n):
        var += (u[i]-E)*(u[i]-E)
    var /= (n-1)

    sigma = np.sqrt(var)
    mu = var/2 + E

    return mu,sigma

def nextTerm(lamb,mu,sigma,St):
    Xt = np.log(St)
    Z = np.random.normal(0,1)
    
    # deltaT is taken > 1 as for deltaT <= 1 most values of jumps (M) are equal to 0 
    deltaT = 3
    N = np.random.poisson(lamb*deltaT)

    # calculating the value of jump
    M = 0
    if N != 0:
        for i in range(N):
            Y = np.random.lognormal(mu,sigma)
            M += np.log(Y)
 
    Xt1 = Xt + (mu - (sigma**2)/2)*deltaT + sigma*Z*np.sqrt(deltaT) + M
    St1 = np.exp(Xt1)

    return St1

def generateDistribution(lamb,mu,sigma,S0):
    prices = []
    currPrice = S0
    for i in range(1000):
        nextPrice = nextTerm(lamb,mu,sigma,currPrice)
        prices.append(nextPrice)
        currPrice = nextPrice

    plt.plot(prices)
    
def main():
    dates,prices = readData()
    mu,sigma = computeMuSigma(prices)
    print("mu = %f, sigma = %f\n"%(mu,sigma))

    S0 = prices[len(prices)-1]
    print("S0 (Price on September 30) = %.2f\n"%(S0))

    lambdas = [0.01, 0.05, 0.1, 0.2]
    for lamb in lambdas:
        generateDistribution(lamb,mu,sigma,S0)

    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.title('Stock Prices for lambda = %s'%(lamb))
    plt.show()

if __name__ == "__main__":
    main()