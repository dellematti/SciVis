import matplotlib.pyplot as plt
import matplotlib.pyplot as secondo
import matplotlib
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt 

#Estrazione dei dati dal file di testo:
with open('percentuali_promossi.txt') as file:
    file_str = file.readlines()

print(file_str)

list_2019 = []
list_2020 = []
list_2021 = []
list_2022 = []

list_2019.append(file_str[0])
#print(list_2019)

list_2020.append(file_str[1])
#print(list_2020)

list_2021.append(file_str[2])
#print(list_2021)

list_2022.append(file_str[3])
#print(list_2022)

list_2019_int = []
list_2020_int = []
list_2021_int = []
list_2022_int = []

for i in list_2019:
    valori = i.split()
    for num in valori:    
        list_2019_int.append(int(num))

print(list_2019_int)

for i in list_2020:
    valori = i.split()
    for num in valori:    
        list_2020_int.append(int(num))

print(list_2020_int)

for i in list_2021:
    valori = i.split()
    for num in valori:    
        list_2021_int.append(int(num))

print(list_2021_int)

for i in list_2022:
    valori = i.split()
    for num in valori:    
        list_2022_int.append(int(num))

print(list_2022_int)


#Creazione del grafico a partire dai dati estratti:
mesi = ["Gennaio", "Febbraio", "Giugno",  "Luglio", "Settembre"]

#L'ultimo numero deve essere uguale al primo per "ricongiungere" il grafico:
nove = [list_2019_int[0], list_2019_int[1], list_2019_int[2], list_2019_int[3], list_2019_int[4], list_2019_int[0]]    
venti = [list_2020_int[0], list_2020_int[1], list_2020_int[2], list_2020_int[3], list_2020_int[4], list_2020_int[0]]
ventuno = [list_2021_int[0], list_2021_int[1], list_2021_int[2], list_2021_int[3], list_2021_int[4], list_2021_int[0]]
ventidue = [list_2022_int[0], list_2022_int[1], list_2022_int[2], list_2022_int[3], list_2022_int[4], list_2022_int[0]]


plt.figure(figsize =(7, 6))   
plt.subplot(polar = True)

plt.rcParams['axes.facecolor'] = 'white'   #cambia il colore della legenda

theta = np.linspace(0, 2 * np.pi, len(venti))

lines, labels = plt.thetagrids(range(0, 360, int(360/len(mesi))), (mesi))

#linea 2019    
plt.plot(theta, nove, marker='o', linewidth= 1.5, color = 'green', alpha=0.8)

# linea 2020
plt.plot(theta, venti, marker='o' , linewidth= 1.5, color = 'orange',alpha=0.8 )
#plt.fill(theta, venti, 'g', alpha = 0.1)

# linea 2021
plt.plot(theta, ventuno, marker='o'  , linewidth=1.5, color = 'c', alpha=0.8)
#plt.fill(theta, ventuno, 'r', alpha = 0.1)   

# linea 2002
plt.plot(theta, ventidue, marker='o', linewidth=1.5, color='red', alpha=0.8)

ax = plt.gca()
ax.set_facecolor('whitesmoke')     # ora che ho ax posso modificare il colore del grafico
ax.set_ylim(0, 100)

y_tick_labels = [1, 2, 3, 4, 5]                         #cambia colore e dimensione di una singola linea ( ma non funziona con la più esterna)                    
ind = y_tick_labels.index(5)                            #dato che ho messo (5) ora queste istruzioni non stanno facendo niente
gridlines = ax.yaxis.get_gridlines()
gridlines[ind].set_color('grey')
gridlines[ind].set_linewidth(0.5)

matplotlib.rc('axes',edgecolor='lightgrey')                              #cambia colore di quella esterna
#matplotlib.rc('axes',edgecolor='white') 

#Cambia i colori delle linee di sfondo del grafico
#plt.rcParams.update({"axes.grid" : True, "grid.color": 'dimgrey'})
#plt.rcParams.update({"axes.grid" : True, "grid.color": 'gainsboro'})
plt.rcParams.update({"axes.grid" : True, "grid.color": 'lightgrey'})
    
#Legenda:
plt.legend(labels =('2019', '2020', '2021', '2022'), loc = 4)


#Sposto le scritte (non il titolo):
plt.xticks()                                             
ax.tick_params(axis='x', which='major', pad=15)

#ax.set_theta_zero_location("E")                      #ruotano il grafico
ax.set_theta_offset(62.5)                             #più aumento più si sposta in senso antiorario

#plt.title("Promossi anni 2019 2020 2021")
# csfont = {'fontname':'Trebuchet MS'}
csfont = {'fontname':'Times New Roman'}
#plt.title('title',**csfont)
plt.title(label="Percentuali di studenti promossi per ogni appello ", fontsize= 18,**csfont, fontweight="bold", color="black", pad='26.0')  #,fontweight=102,  pad è lo spazio sotto


#Stampa del grafico finale:
plt.show()