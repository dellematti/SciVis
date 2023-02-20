import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
"""" 
anno 2019 = [83,58,10,5,9]
anno 2020 = [52,33,18,5,7]
anno 2021 = [35,62,9,2,5]
anno 2022 = [71,29,7,4,3]
"""

""""
Statle : 
    anno 2020 = {'Gennaio': 33, 'Febbraio': 27, 'Giugno': 12, 'Luglio': 7, 'Settembre': 11}
    anno 2021 = {'Gennaio': 38, 'Febbraio': 25, 'Giugno': 38, 'Luglio': 11, 'Settembre': 10}
    anno= 2022 {'Gennaio': 9, 'Febbraio': 44, 'Giugno': 13, 'Luglio': 7, 'Settembre': 7}}
"""
# Create a datase
y = [71,29,7,4,3]
x= ["Gennaio","Febbraio","Giugno","Luglio","Settembre"]
fig = plt.figure()
fig.patch.set_facecolor("#f6faf9")


plt.fill_between(x, y, color="lightpink",alpha=0.5,label='Insubria')
#plt.fill_between(x, y, color="skyblue",alpha=0.5, label='Statle')
plt.ylim(-4,90)
plt.plot(x, y,linestyle='-', marker='.', color="lightpink")
#plt.plot(x, y,linestyle='-', marker='.', color="skyblue")

#spazio = 0.600
#fig.subplots_adjust(bottom=spazio)
ax = plt.gca()
ax.set_facecolor("#f6faf9")
#plt.ylabel('Passati')
plt.xlabel('Mesi')

ax = plt.gca()
#ax.axes.xaxis.set_ticklabels([]) #rimuovono le lables sull'asse delle x o y
ax.axes.yaxis.set_ticklabels([])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#plt.title("Statale 2022")
plt.title("Messina 2022")

plt.show()
plt.savefig("smallMultiple.svg") 