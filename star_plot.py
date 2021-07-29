# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
import sys

#入力は
# 0 HIP番号
# 1 赤経時
# 2 赤経分
# 3 赤経秒
# 4 赤緯符号
# 5 赤緯度
# 6 赤緯分
# 7 赤緯秒
# 8 等級


#星の数
N = 3215
plot_data = []

with open('star_plot.txt', 'r', encoding='utf-8') as star:
    star_data = star.readlines()
    for i in range(N):
        star_data[i] = star_data[i].split(',')
        a = float(float(star_data[i][1])*15 + float(star_data[i][2])*0.25 + float(star_data[i][3])*0.0042)
        b = float(float(star_data[i][5]) + float(star_data[i][6])/60 + float(star_data[i][7])/3600)
        c = int(round(float(star_data[i][8]), 0))
        # d = str(star_data[i][16])
        if star_data[i][4] == "0":
            b = -b
        if c <= 5:
            plot_data.append([a,b,c,i])
star.close()

x = []
y = []
blt = []

for i in range(len(plot_data)):
    x_ = round(float(plot_data[i][0]), 1)
    y_ = round(float(plot_data[i][1]), 1)
    blt_ = plot_data[i][2]

    x.append(x_)
    y.append(y_)
    blt.append(blt_)

plt.figure(figsize=(36, 9), dpi=300)
plt.xlim(0, 360)
plt.ylim(-90, 90)
plt.axis("on")


for i in range(len(plot_data)):
    s_ = (6 - blt[i])**3
    print(s_)
    plt.scatter(x[i], y[i], s=s_, c=s_, cmap='spring', vmin=-50, vmax=343)
plt.savefig("star_fig.png")
# plt.show()
