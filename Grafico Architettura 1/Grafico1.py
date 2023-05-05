import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

#Extract from file:
with open("dati.txt") as file:
    str_from_file = file.readline()

#print(str_from_file)

str_new = str_from_file.split(' ')
data_list = []

for i in str_new:
    data_list.append(int(i))

print(data_list)

#Create graphic:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

overall_ratios = [data_list[0], data_list[1], data_list[2]]
labels = ['Insufficienti', 'Ritirati', 'Promossi']
explode = [0, 0, 0.1]
colors = ['silver', 'peru', 'royalblue']

angle = 298 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode, colors=colors)

age_ratios = [data_list[3], data_list[4], data_list[5], data_list[6]]
age_labels = ['Inferiore a 20', 'Da 20 a 24', 'Da 25 a 27', 'Da 28 a 30L']
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='royalblue', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, label_type='center')

ax2.set_title('Quantità di voti sufficienti')
ax2.legend(loc='lower right')
ax2.axis('off')
ax2.set_xlim(-2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[2].theta1, wedges[2].theta2
center, r = wedges[2].center, wedges[2].r
bar_height = sum(age_ratios)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 2), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(2)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, -447), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(2)

plt.show()