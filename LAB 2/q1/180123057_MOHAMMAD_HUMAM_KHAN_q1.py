## The dependencies needed are : python3, numpy, matplotlib
## To run the code type following command in terminal : python3 180123057_MOHAMMAD_HUMAM_KHAN_q1.py


import matplotlib.pyplot as plt
import pandas as pd
import random as rand


#Function to generate sequence of numbers
def LFG(a,b,m,seed,rounds,plot_name_scatter,plot_name_bar):
	x_values = []
	y_values = []
	xi = (a*seed + b)%m
	ui = xi/m
	for i in range (17):
		x_values.append(ui)
		xi = (a * xi + b) % m
		ui = xi / m
		y_values.append(ui)

	for i in range (rounds):
		x_values.append(ui)
		ui = x_values[i-17] - x_values[i-5]
		if ui<0:
			ui = ui+1
		y_values.append(ui)		

	#Plotting x-y scatter plot
	plt.figure(figsize=(10,8))
	plt.title(" Plot of Ui and Ui+1 for %s rounds" % rounds, fontsize=15)
	plt.xlabel("Ui Values", fontsize=15)
	plt.ylabel("Ui+1 Values", fontsize=15)
	plt.scatter(x_values, y_values)
	plt.savefig(plot_name_scatter)
	plt.clf()	

	#Plotting the Bar Diagram
	plt.figure(figsize=(10,8))
	plt.title(" Bar Diagram of Frequency of Ui values for %s rounds" % rounds, fontsize=15)
	plt.xlabel("Intervals of Ui values", fontsize=15)
	plt.ylabel("Frequency of Ui Values", fontsize=15)
	plt.hist(x_values, edgecolor='black')
	plt.savefig(plot_name_bar)
	plt.clf()	


a = 1229
b = 1
m = 2048
seed = 295
plot_name1 = "Q1_Plot_1"
plot_name2 = "Q1_Bar_Diagram_1"
LFG(a,b,m,seed,1000,plot_name1,plot_name2)

plot_name1 = "Q1_Plot_2"
plot_name2 = "Q1_Bar_Diagram_2"
LFG(a,b,m,seed,10000,plot_name1,plot_name2)


plot_name1 = "Q1_Plot_3"
plot_name2 = "Q1_Bar_Diagram_3"
LFG(a,b,m,seed,100000,plot_name1,plot_name2)