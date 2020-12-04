import matplotlib.pyplot as plt
import pandas as pd
import random as rand

def LCG(a,b,m,seed,plot_name):
	x_values = []
	y_values = []
	xi = (a*seed + b)%m
	ui = xi/m
	for i in range (m+1):
		x_values.append(ui)
		xi = (a * xi + b) % m
		ui = xi / m
		y_values.append(ui)	

	plt.title(" Plot of Ui-1 and Ui ", fontsize=15)
	plt.xlabel("Ui-1 Values", fontsize=15)
	plt.ylabel("Ui Values", fontsize=15)
	plt.scatter(x_values, y_values)
	plt.savefig(plot_name)
	plt.clf()		


a = 1229
b = 1
m = 2048
seed = 295
plot_name = "180123057_Q3_Plot"
LCG(a,b,m,seed,plot_name)