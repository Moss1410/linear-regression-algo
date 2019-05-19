import csv
import numpy as np
import matplotlib.pyplot as plt

datax = []
datay = []
xHeading = ''
yHeading = ''
title = ''

with open('Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 1:
            #column headings
            xHeading = row[0]
            yHeading = row[1]
        elif line_count == 0:
            #titles
            title = row[0]
        else:
            datax.append(row[0])
            datay.append(row[1])
        line_count += 1

x = np.array(datax, dtype=float)
y = np.array(datay, dtype=float)
A = np.vstack([x, np.ones(len(x))]).T
mc = np.linalg.solve(np.dot(A.T,A), np.dot(A.T,y))
plt.plot(x, y, 'o', label = 'Data', markersize= 2)
plt.plot(x, mc[0]*x + mc[1], 'r', label= 'Linear Regression')
plt.legend()
plt.xlabel(xHeading)
plt.ylabel(yHeading)
plt.title(title)
plt.show()