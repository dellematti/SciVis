import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data2 = pd.read_csv('genfebrraio.csv')
colori = {'Go': "#66c2ff", 'Java': "#ff6666"}
g = sns.swarmplot(data=data2, x="Mese", y="Voto",hue="Linguaggio",palette= colori)
plt.legend(bbox_to_anchor=(0.93, 1), loc='upper left', borderaxespad= 0)
plt.title("confronti  2017 - 2018")
plt.savefig('prova.png')