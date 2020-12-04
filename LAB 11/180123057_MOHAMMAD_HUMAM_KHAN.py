##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN.py

import math
import random
import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt





# Function to generate random sequence using Linear Congruence Generators
def LCG(a,b,m,seed,n):
	x = []
	xi = seed
	for i in range(n):
		x.append(xi/m)
		xi = (a*xi + b)%m
	return x


#Count Elements in a given set
def Count_Elements_in_Set(X,N,i):
	count = 0
	low = i*(1/N)
	high = (i+1)*(1/N)
	for x in X:
		if low<=x and x<high:
			count += 1
	return count		


#Function to generate Discrepancy
def Calculate_Discrepancy(X,n,N):
	currDisc = 0
	volA = 1/N
	for i in range(N):
		disc = abs(Count_Elements_in_Set(X,N,i)/n - volA)
		currDisc = max(currDisc, disc)
	return currDisc	




N = [10,20,50,100]

#****** LCG Parameters *******
a = 1229
b = 1
m = 2048
seed = 213
n = m-1

# ********* Generating Point set ********
X = LCG(a,b,m,seed,n)


# ********* Calculating Discrepancies ********
for i in N:
	discrepancy = Calculate_Discrepancy(X,n,i)
	print("Discrepancy of point set for N = %s is : %0.8f" % (i,discrepancy))




