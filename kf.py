import numpy as np
f = open(r"x.txt")
line = f.readline()
data = np.zeros((100,4))
i = 0
while line:
    num = np.array([float(x) for x in line.split()])
    data[i,:] = num
    line = f.readline()
    i = i+1
f.close()