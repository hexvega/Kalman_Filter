import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号


f = open(r"roll.txt")
title="翻转角roll："



line = f.readline()
data_list = []
while line:
    # num = list(map(float,line.split()))
    # num = float(line)
    f_list = [float(i) for i in line.split("\r\n")]
    data_list.append(float(f_list[0]))
    line = f.readline()
f.close()
# data_array = np.array(data_list)

data_array = np.random.rand(len(data_list))
for i in range(len(data_array)):
    data_array[i] = float(data_list[i])


plt.plot(data_array,color="b")

# Q 过程噪声，Q增大，动态响应变快，收敛稳定性变坏
# R 测量噪声，R增大，动态响应变慢，收敛稳定性变好

# Q 参数调滤波后的曲线平滑程度，Q越小越平滑。
# R 参数调整滤波后的曲线与实测曲线的相近程度，R越小越接近。

# 加速度
# Q = 0.01
# R = 0.9

# 陀螺仪
# Q = 0.1
# R = 3.9

# 磁力计
# Q = 0.06
# R = 15.4

# pitch
# Q = 0.07
# R = 0.8

# yaw
# Q = 0.06
# R = 0.9

# roll
Q = 0.06
R = 0.9

Now_P = 1
Kg = 0
LastP = 1
x_k_k1 = 0
ADC_OLD_Value = 0

out = 0


def kalman(input):
    global out
    global LastP

    Now_P = LastP + Q

    Kg = Now_P / (Now_P + R)

    out = out + Kg * (input - out)

    LastP = (1 - Kg) * Now_P

    return out


plt.plot(data_array)
kalmanFilter_array = []
for i in range(len(data_array)):
    kalmanFilter_array.append(kalman(data_array[i]))

plt.title(title)
plt.plot(kalmanFilter_array)

plt.show()
