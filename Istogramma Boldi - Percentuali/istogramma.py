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

#Estrazione degli iscritti per comporre le liste di percentuali per l'istogramma:
with open('iscritti.txt') as file3:
    text3 = file3.readlines()

list_backup3 = []

for i in text3:
    list_backup3.append(i.split(' '))

list_iscritti = []

for i in list_backup3:
    for j in i:
        list_iscritti.append(int(j))

print(list_iscritti)

#Liste definitive per istogramma:
list_percentuali_promossi = []
list_percentuali_bocciati = []

for i in range(len(list_iscritti)):
    list_percentuali_promossi.append(int((list_promossi[i] / list_iscritti[i]) * 100))
    list_percentuali_bocciati.append(100 - int((list_promossi[i] / list_iscritti[i]) * 100))

print('\n')
print(list_percentuali_promossi)
print(list_percentuali_bocciati)

#Creazione del grafico a partire dai dati raccolti:
labels = ['2019', '2020', '2021', '2022']

y = np.arange(len(labels))
height = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.barh(y - height / 2, list_percentuali_promossi, height, label = 'Promossi', color = 'navajowhite')
rects2 = ax.barh(y + height / 2, list_percentuali_bocciati, height, label = 'Bocciati', color = 'lightskyblue')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Percentuale')
ax.set_ylabel('Anno Accademico')
ax.set_xlim([0, 100])
ax.set_title('Istogramma confronto delle percentuali promossi-bocciati')
ax.set_yticks(y, labels)
ax.legend()

ax.bar_label(rects1, padding = 3)
ax.bar_label(rects2, padding = 3)

fig.tight_layout()

plt.show()