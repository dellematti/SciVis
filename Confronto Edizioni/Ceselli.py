import matplotlib.pyplot as plt

""""
ceselli:  [60, 34, 8, 3, 6] [37, 27, 8, 6, 12]
boldi [35, 27, 15, 7, 12] [51, 78, 27, 21, 25]
tot studenti ceselli : 173
tot studenti boldi : 210
"""

y = [17,60, 34, 8, 3, 6]
x = ["Gennaio","Gennaio*","Febbraio","Giugno","Luglio","Settembre"]
  
fig = plt.figure()
fig.patch.set_facecolor("#f6faf9")
ax = fig.add_subplot(1, 1, 1)

#plt.grid(color='#d3d3d3', linestyle='-', linewidth=0.3)
plt.ylim(-10,100)
plt.plot(x, y,linestyle='--', marker='o', color='#e87000',label = "Esami Ceselli")

totPassati = 0
for val in y :
    totPassati+=val

for tmpx,tmpy in zip(x,y):
    label = str(int((tmpy/totPassati)*100))+"%"
    plt.annotate(label,
                 (tmpx,tmpy),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='green'))

spazio = 0.400
fig.subplots_adjust(bottom=spazio)

plt.legend()
ax = plt.gca()
ax.set_facecolor("#f6faf9")
plt.ylabel('Studenti Passati')  
plt.xlabel('Mesi')

plt.show()
plt.savefig("ce.svg") 