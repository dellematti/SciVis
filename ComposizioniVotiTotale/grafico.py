import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
x = ['Archi-1', 'Prog-1']

def leggiFile():
    voti={"18-21":0,"22-25":0,"26-28":0,"29-30":0}
    tot=0
    df = pd.read_csv("ris.csv", sep=";", encoding="utf-8")
    for i in range (0,len(df)):
        if not np.isnan(df["Anno"][i]):  
            voti["18-21"]+=int(df["18-21"][i])
            voti["22-25"]+=int(df["22-25"][i])
            voti["26-28"]+=int(df["26-28"][i])
            voti["29-30"]+=int(df["29-30"][i])
            tot+=int(df["Tot"][i])
    
    return voti,tot

voti,tot = leggiFile()

r4 = np.array([17, round((voti["29-30"]/tot)*100)])
r3 = np.array([13, round((voti["26-28"]/tot)*100)])
r2 = np.array([33, round((voti["22-25"]/tot)*100)])
r1 = np.array([37, round((voti["18-21"]/tot)*100)])
 
 
colori = ["#6E7B82","#4ba3c3","#175676","#BA324F"]

fig = plt.figure(facecolor="white")
ax = fig.add_subplot(1, 1, 1)
plt.bar(x, r1, color=colori[0] , width=0.4,  align='center')
plt.bar(x, r2, bottom=r1, color=colori[1], width=0.4,  align='center')
plt.bar(x, r3, bottom=r1+r2, color=colori[2], width=0.4,  align='center')
plt.bar(x, r4, bottom=r1+r2+r3, color=colori[3], width=0.4, align='center')

for bar in ax.patches:
    #print(bar.get_height())
    ax.text(
      bar.get_x()+bar.get_width()/2,
      bar.get_y()+bar.get_height()/2,
      str(round(bar.get_height()))+"%",
      ha='center',
      color='w',
      weight='bold',
      size=9
    )

plt.xlabel("Materia")
plt.ylabel("Percentuale")
plt.legend(["bocciati", "18-21", "22-25", "26-28","29-30"], bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.title("Archi1 vs Prog1")
plt.show()
plt.savefig("archivsprog.svg") 

