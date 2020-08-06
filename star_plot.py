# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
import sys

# 標準入力は
# 赤経,赤緯,等級

N = 3009 #5.5等級までの星の数


with open('star_plot.txt', 'r', encoding='utf-8') as star:
    star_data = star.readlines()
    for i in range(N):
        star_data[i] = star_data[i].split(',')
        star_data[i][2] = int(round(float(star_data[i][2]), 0))
star.close()

x = []
y = []
blt = []

for i in range(N):
    x_ = round(float(star_data[i][0]), 1)
    y_ = round(float(star_data[i][1]), 1)
    blt_ = star_data[i][2]

    x.append(x_)
    y.append(y_)
    blt.append(blt_)

plt.figure(figsize=(36, 9), dpi=300)
plt.xlim(0, 360)
plt.ylim(0, 90)
plt.axis("off")

for i in range(N):
    s_ = (6 - blt[i])**2
    plt.scatter(x[i], y[i], s = s_)

plt.savefig("star_fig.png")
# plt.show()
