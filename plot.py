import matplotlib.pyplot as plt
import csv

filename="sheet.csv"

x = []
y = []

with open("sheet.csv",'r') as csvfile:
	csvreader=csv.reader(csvfile)
	for row in csvreader:
		x.append(int(row[0]))
		y.append(int(row[1]))

print(x)
print(y)
plt.plot(x,y)
plt.show()