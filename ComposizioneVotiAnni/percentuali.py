import matplotlib.pyplot as plt
import numpy as np

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'right')
        
year = [2018, 2019, 2020, 2021, 2022] #dati presi tramite script apposito
anno2018 = [18,16,15,15,20]
anno2019 = [48,41,30,42,28]
anno2020 = [47,48,30,44,16]
anno2021 = [30,37,19,27,22]

bar_width = 0.5

fig = plt.figure(facecolor="white")
ax = fig.add_subplot(1, 1, 1)

u1 = list(np.add(anno2018,anno2019))
u2 = list(np.add(u1,anno2020))
u3 = list(np.add(u2,anno2021))

ax1 = plt.barh(year, anno2018,bar_width,label="18-21",color="#6E7B82")  
ax2 = plt.barh(year, anno2019,bar_width,left=anno2018,label="22-25", color="#4ba3c3")
ax3 = plt.barh(year, anno2020,bar_width,left=u1,label="26-28",color="#175676")
ax4 = plt.barh(year, anno2021,bar_width,left=u2,label="29-30",color="#BA324F")
addlabels(year,[150,150,150,150,150] )
ax.bar_label(ax.containers[3])



totali = [143,142,94,128,86]
cont = 0

for bar in ax.patches:
    if cont == 4:
      cont = -1    
    ax.text(
      bar.get_x()+bar.get_width()/2,
      bar.get_y()+bar.get_height()/2,
      str(round((bar.get_width()/totali[cont])*100))+"%",
      ha='center',
      color='w',
      weight='bold',
      size=10
    )
    cont +=1
    

#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.xlabel('TotPassati')  
plt.ylabel('Anni')

plt.show()  
plt.savefig("matplotlib.svg") 