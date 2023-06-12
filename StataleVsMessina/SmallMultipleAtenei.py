
import pandas as pd
import matplotlib.pyplot as plt
"""" 
anno 2019 = [63,38,10,5,9]
anno 2020 = [52,33,18,5,7]
anno 2021 = [30,62,9,2,5]
anno 2022 = [71,29,7,4,3]
"""
""""
Statle : 
    2019 = {'Gennaio': 30, 'Febbraio': 38, 'Giugno': 13, 'Luglio': 13, 'Settembre': 15}
    anno 2020 = {'Gennaio': 33, 'Febbraio': 27, 'Giugno': 12, 'Luglio': 7, 'Settembre': 11}
    anno 2021 = {'Gennaio': 38, 'Febbraio': 25, 'Giugno': 38, 'Luglio': 11, 'Settembre': 10}
    anno= 2022 {'Gennaio': 9, 'Febbraio': 44, 'Giugno': 13, 'Luglio': 7, 'Settembre': 7}}
"""
y = [30,38,13,13,15]
tot=0
for i in y :
    tot+=i
    
for i in range (0,len(y)):
    y[i]= round((y[i]/tot)*100)
    
print(y)
x= ["Gennaio","Febbraio","Giugno","Luglio","Settembre"]
fig = plt.figure()
fig.patch.set_facecolor("#f6faf9")


#plt.fill_between(x, y, color="lightpink",alpha=0.5,label='Messina')
plt.fill_between(x, y, color="skyblue",alpha=0.5, label='Statle')
plt.ylim(-4,90)
#plt.plot(x, y,linestyle='-', marker='.', color="lightpink")
plt.plot(x, y,linestyle='-', marker='.', color="skyblue")

#spazio = 0.600
#fig.subplots_adjust(bottom=spazio)
ax = plt.gca()
ax.set_facecolor("#f6faf9")
plt.ylabel('Passati %')
plt.xlabel('Mesi')

ax = plt.gca()
#ax.axes.xaxis.set_ticklabels([]) #rimuovono le lables sull'asse delle x o y
#ax.axes.yaxis.set_ticklabels([])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#plt.title("Messina 2019")
plt.title("Statale 2019")

for tmpx,tmpy in zip(x,y):
    print(tmpy)
    label = str(tmpy)+"%"
    plt.annotate(label,
                (tmpx,tmpy),
                textcoords="offset points",
                xytext=(0,10),
                ha='center',
                #skyblue
                arrowprops=dict(arrowstyle="->", color='skyblue'))

plt.show()
plt.savefig("smallMultiple.svg") 