import matplotlib.pyplot as plt

""""
ANNO 2019
"""

y = [17,60, 34, 8, 3, 6]
y2 = [8,35, 27, 15, 7, 12] 
x = ["Gennaio","Gennaio*","Febbraio","Giugno","Luglio","Settembre"]
  
fig = plt.figure()
fig.patch.set_facecolor("#f6faf9")
ax = fig.add_subplot(1, 1, 1)

plt.grid(color='#d3d3d3', linestyle='-', linewidth=0.3)
plt.ylim(-10,100)
plt.plot(x, y,linestyle='--', marker='o', color='#e87000',label = "Esami Ceselli")
plt.plot(x, y2,linestyle='-', marker='s',color='#05898f',label = "Esami Boldi")
    
print("ciao")
plt.legend()
ax = plt.gca()
ax.set_facecolor("#f6faf9")
plt.ylabel('Studenti Passati')  
plt.xlabel('Mesi')

plt.show()
plt.savefig("ma.png") 