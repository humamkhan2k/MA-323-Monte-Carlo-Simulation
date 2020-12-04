def LCG(a,b,m,seed,file):
	xi = seed
	for i in range (100):
		file.write("%s, " % xi)
		xi = (a * xi + b) % m



## PART 1 : a = 6, b = 0, m = 11    
		
file = open('q1_part1.csv', 'a')
for i in range (100):
	file.write("X%s, " % i)
file.write("\n")

for i in range (0,11):
	LCG(6,0,11,i, file)
	file.write("\n")

file.close()



## PART 2 : a = 3, b = 0, m = 11

file = open('q1_part2.csv', 'a')
for i in range (100):
	file.write("X%s, " % i)
file.write("\n")

for i in range (0,11):
	LCG(3,0,11,i, file)
	file.write("\n")
file.close()