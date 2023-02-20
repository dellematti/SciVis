import matplotlib.pyplot as plt

y = [8,35, 27, 15, 7, 12] 
x = ["Gennaio","Gennaio*","Febbraio","Giugno","Luglio","Settembre"]
  
fig = plt.figure()
fig.patch.set_facecolor("#f6faf9")
ax = fig.add_subplot(1, 1, 1)

#plt.grid(color='#d3d3d3', linestyle='-', linewidth=0.3)
plt.ylim(-10,100)
fog = plt.plot(x, y,linestyle='--', marker='o', color='#05898f',label = "Esami Boldi")

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
plt.savefig("bo.svg") 