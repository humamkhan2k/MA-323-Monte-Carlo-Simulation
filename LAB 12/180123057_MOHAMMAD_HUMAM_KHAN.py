##To run the code type in terminal: python3 180123057_MOHAMMAD_HUMAM_KHAN.py

import math
import random
from fractions import Fraction
import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt




# Function to generate random sequence using Linear Congruence Generators
def LCG(n):
	#****** LCG Parameters *******
	a = 1229
	b = 1
	m = 2048
	seed = 213

	x = []
	xi = seed
	for i in range(n):
		x.append(xi/m)
		xi = (a*xi + b)%m
	return x


# Function to convert binary number "k" to "phi(k)"
def Radical_Inverse_Function(n, base):
	radical_inverse = 0
	dr = 1
	while n:
		dr *= base
		n, remainder = divmod(n, base)
		radical_inverse += remainder/dr
	return radical_inverse


# Function to generate van-der-corput sequence after taking n and base as inputs
def Van_der_Corput(n, base):
	Van_der_corput_sequence = []
	for i in range(n):
		phi_k = Radical_Inverse_Function(i, base)
		Van_der_corput_sequence.append(phi_k)	
	return Van_der_corput_sequence



def Plot_Distribution(x,n,name):

	lcg_sequence = LCG(n)
	fig, ax = plt.subplots(1,2,figsize=(20,12))
	
	ax[0].set_title("Frequency Distribution Plot of van-der-corput Sequence \n for n = %s values" % n,fontsize=15)
	ax[0].set_xlabel("Generated Sequence values",fontsize=15)
	ax[0].set_ylabel("Frequency of intervals",fontsize=15)
	ax[0].hist(x,bins = 20,range = [0,1],edgecolor='black')

	ax[1].set_title("Frequency Distribution Plot of LCG Sequence \n for n = %s values" % n,fontsize=15)
	ax[1].set_xlabel("Generated Sequence values",fontsize=15)
	ax[1].set_ylabel("Frequency of intervals",fontsize=15)
	ax[1].hist(lcg_sequence,bins = 20,range = [0,1],color='green',edgecolor='black')

	plt.savefig(name)
	plt.clf()



def Plot_Pair(x,n,name):
	plt.figure(figsize=(15,12))
	plt.scatter(x[:-1] , x[1:],s=0.5,color='green')
	plt.title("Plot of (x[i], x[i+1]) of van-der-corput Sequence for n = %s values" % n, fontsize=20)
	plt.xlabel("x[i] values",fontsize=15)
	plt.ylabel("x[i+1] values",fontsize=15)
	plt.savefig(name)
	plt.clf()




#******************* QUESTION - 1 ****************************


# ****** PART-1********
Van_der_corput_sequence = Van_der_Corput(25,2)
print("First 25 numbers in Van-der-Corput Sequence are : \n")
print(Van_der_corput_sequence)


# ****** PART-2********		
Van_der_corput_sequence = Van_der_Corput(1000,2)
Plot_Pair(Van_der_corput_sequence,1000,"q1_PairPlot")


# ****** PART-3********
Van_der_corput_sequence = Van_der_Corput(100,2)
Plot_Distribution(Van_der_corput_sequence, 100, "q1_Distribution1")


# ****** PART-4********
Van_der_corput_sequence = Van_der_Corput(100000,2)
Plot_Distribution(Van_der_corput_sequence, 100000, "q1_Distribution2")






#******************* QUESTION - 2 ****************************



# Function to generate Halton Sequence
def Halton_Sequence(n):
	vdc_2 = Van_der_Corput(n,2)
	vdc_3 = Van_der_Corput(n,3)

	plt.figure(figsize=(10,10))
	plt.title("Plot of phi_2(i) and phi_3(i) for n = %s" % n, fontsize=20)
	plt.xlabel("Values of phi_2(i)", fontsize=15)
	plt.ylabel("Values of phi_3(i)", fontsize=15)
	if n==100:
		plt.scatter(vdc_2, vdc_3,color='green')
	else:
		plt.scatter(vdc_2, vdc_3,s=0.5,color='green')	
	plt.savefig("Halton_%s" % n)


Halton_Sequence(100)
Halton_Sequence(100000)	