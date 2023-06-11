import numpy as np
import matplotlib.pyplot as plt
 
x = ['2016-2018', '2018-2020']
r1 = np.array([56, 51])
r2 = np.array([8, 5])
r3 = np.array([18, 15])
r4 = np.array([13, 17])
r5 = np.array([6, 12])
 
 
colori = ["#6E7B82","#d59475","#c4a574","#b2b774","#a0c873"]

fig = plt.figure(facecolor="white")
ax = fig.add_subplot(1, 1, 1)
plt.bar(x, r1, color=colori[0] , width=0.3,  align='center')
plt.bar(x, r2, bottom=r1, color=colori[1], width=0.3,  align='center')
plt.bar(x, r3, bottom=r1+r2, color=colori[2], width=0.3,  align='center')
plt.bar(x, r4, bottom=r1+r2+r3, color=colori[3], width=0.3, align='center')
plt.bar(x, r5, bottom=r1+r2+r3+r4, color=colori[4], width=0.3,  align='center')

for bar in ax.patches:
    print(bar.get_height())
    ax.text(
      bar.get_x()+bar.get_width()/2,
      bar.get_y()+bar.get_height()/2,
      str(round(bar.get_height()))+"%",
      ha='center',
      color='w',
      weight='bold',
      size=9
    )

plt.xlabel("Anni")
plt.ylabel("Percentuale")
plt.legend(["bocciati", "18-21", "22-25", "26-28","29-30"], bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.title("Java vs Go")
plt.show()
plt.savefig("javavsgo2016-2022.svg") 

