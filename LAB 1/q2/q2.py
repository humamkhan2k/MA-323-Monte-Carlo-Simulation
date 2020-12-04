import matplotlib.pyplot as plt
import pandas as pd
import random as rand

def LCG(a,b,m,seed,intervals,freq,plot_name):
	xi = seed
	ui = seed
	u_values = []
	for i in range (100000):
		xi = (a * xi + b) % m
		ui = xi / m
		u_values.append(ui)
		l = 0.00
		u = 0.05
		for i in range(20):
			if (l <= ui) and (ui < u):
				freq[i] = freq[i] + 1
				break	
			l = round(l + 0.05, 2)
			u = round(u + 0.05, 2)	

	num_bars = 20
	plt.figure(figsize=(10,8))
	plt.title("Bar Diagram representing frequencies of generated numbers \n in given intervals \n\n a = %s, b = %s, m = %s, seed = %s" % (a,b,m,seed), fontsize=15)
	plt.xlabel("Range of Intervals", fontsize=15)
	plt.ylabel("Frequencies of ui in given range", fontsize=15)
	plt.xticks(intervals, rotation='vertical')
	plt.hist(u_values, num_bars, edgecolor='black')
	plt.savefig(plot_name)
	plt.clf()		



    
# Opening the file		
file1 = open('q2_Part1_Table.csv', 'w')
file2 = open('q2_Part2_Table.csv', 'w')

# Creating Header columns in csv file
file1.write("Intervals, ")
file2.write("Intervals, ")
l = 0.00
u = 0.05
for i in range (20):
	file1.write("%s - %s, " % (l,u))
	file2.write("%s - %s, " % (l,u))
	l = round(l + 0.05, 2)
	u = round(u + 0.05, 2)
file1.write("\n")
file2.write("\n")


#Generating Intervals for u values
intervals = []
val = 0.00
for i in range(21):
	intervals.append(val)
	val += 0.05




# PART-1 : a = 1597, b = 36781, m = 244944

a = 1597
m = 244944
b = 36781
seed_array = rand.sample(range(m), 5)

img = 1;
for seed in seed_array:
	freq = []
	for i in range(20):
		freq.append(0)
	plot_name = "q2_plot_part1_" + str(img) + ".png"
	LCG(a,b,m,seed,intervals,freq,plot_name)
	img += 1

	file1.write("seed = %s," % seed)
	for i in range(20):
		file1.write("%s, " % freq[i])
	file1.write("\n")	

file1.close()





# PART-2 : a = 51749, b = 36781, m = 244944

a = 51749

img = 1;
for seed in seed_array:
	freq = []
	for i in range (20):
		freq.append(0)
	plot_name = "q2_plot_part2_" + str(img) + ".png"
	LCG(a,b,m,seed,intervals,freq,plot_name)
	img += 1

	file2.write("seed = %s," % seed)
	for i in range(20):
		file2.write("%s, " % freq[i])
	file2.write("\n")

file2.close()	