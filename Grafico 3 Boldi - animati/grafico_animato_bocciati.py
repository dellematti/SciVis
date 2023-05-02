import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

with open('bocciati.txt') as file:
    text = file.readlines()

with open('iscritti.txt') as file2:
    text2 = file2.readlines()

file.close()
file2.close()
#Creazione lista (list_somme) di promossi dal 2019 al 2022:
list_somme = [] #lista finale da passare per comporre il grafico animato

list_somme_str = []

for i in text:
    list_somme_str.append(i.split(' '))

for i in list_somme_str:
    for j in i:
        list_somme.append(int(j))

print(list_somme)

#Creazione lista (list_iscritti) di iscritti dal 2019 al 2022:
list_iscritti = []

list_iscritti_str = []

for i in text2:
    list_iscritti_str.append(i.split(' '))

for i in list_iscritti_str:
    for j in i:
        list_iscritti.append(int(j))

print(list_iscritti)

#Creazione lista (list_percentuali) di % dei bocciati dal 2019 al 2022:
#Sarà la lista che compone il grafico.

list_percentuali = []

for i in range(len(list_iscritti)):
    list_percentuali.append(int((list_somme[i] / list_iscritti[i]) * 100))

print(list_percentuali)

#Creazione del grafico a partire dai dati estratti:

# create empty lists for the x and y data
x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots()
plt.margins(x = 2)

# function that draws each frame of the animation
def animate(i):
    if i > list_percentuali.__len__():
        return
    if i == list_percentuali.__len__():
        plt.fill_between(x, y, color="skyblue", alpha=0.8)
        plt.plot(x, y, color="skyblue")
        return
    pt = list_percentuali[i] # grab a random integer to be the next y-value in the animation
    #print(i)
    print(pt)
    x.append(i)
    y.append(pt)

    ax.clear()
    #ax.margins(x = 0)
    ax.plot(x, y)
    ax.set_xlim([-0.2, 3.2])
    ax.set_ylim([0, 100])
    ax.set_ylabel('Percentuale di studenti promossi')
    ax.set_xlabel('Anno Accademico')
    ax.set_title('Grafico degli studenti bocciati per ogni A.A.')

# run the animation
ani = FuncAnimation(fig, animate, frames=5, interval=500, repeat=False)

plt.show()