import matplotlib.pyplot as plt
import numpy as np

with open('passati.txt') as file1:
    text1 = file1.readlines()

with open('bocciati.txt') as file2:
    text2 = file2.readlines()

#print(text1)
#print(text2)

list_backup1 = []
list_backup2 = []

for i in text1:
    list_backup1.append(i.split(' '))

for i in text2:
    list_backup2.append(i.split(' '))

#print(list_backup1)
#print(list_backup2)

list_promossi = []
list_bocciati = []

for i in list_backup1:
    for j in i:
        list_promossi.append(int(j))

for i in list_backup2:
    for j in i:
        list_bocciati.append(int(j))

print(list_promossi)
print(list_bocciati)


#Creazione del grafico a partire dai dati raccolti:
labels = ['2019', '2020', '2021', '2022']

y = np.arange(len(labels))
height = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.barh(y - height / 2, list_promossi, height, label = 'Promossi', color = 'navajowhite')
rects2 = ax.barh(y + height / 2, list_bocciati, height, label = 'Bocciati', color = 'lightskyblue')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Numero di studenti')
ax.set_ylabel('Anno Accademico')
ax.set_xlim([0, 200])
ax.set_title('Istogramma confronto dei promossi e bocciati')
ax.set_yticks(y, labels)
ax.legend()

ax.bar_label(rects1, padding = 3)
ax.bar_label(rects2, padding = 3)

fig.tight_layout()

plt.show()