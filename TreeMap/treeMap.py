import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify
import platform


df = pd.read_csv('promossi.csv')
df2 = df.sort_values(by="Percentuale", ascending=False)

mini, maxi = df2["Percentuale"].min(), df2["Percentuale"].max()
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
cmap = matplotlib.cm.plasma

colors = [cmap(norm(value)) for value in df2["Percentuale"]]
labels = []
labels = ['Anno %s\n %d Promossi\n %.2f */.' %(label) for label in zip(df2["Anno"], df2["Promossi"], df2["Percentuale"])]

print(labels)
fig = plt.figure(figsize=(12, 10))
fig.suptitle("Composizioni Passatti Prog 1", fontsize=20)
ax = fig.add_subplot(111, aspect="equal")
print(len(labels),len(colors))

ax = squarify.plot(df2["Percentuale"], color=colors, label= labels, ax=ax, alpha=.6, bar_kwargs=dict(linewidth=1, edgecolor="#222222"))

ax.set_xticks([])
ax.set_yticks([])

img = plt.imshow([df2["Percentuale"]], cmap=cmap)
img.set_visible(False)
fig.colorbar(img, orientation="vertical", shrink=.96)


plt.savefig('prova.png')

#squarify.plot(sizes=df['Percentuale'], label=df['Anno'], color = sb.color_palette("magma", len(df['Promossi'])),pad = True,alpha = 0.7)
#plt.axis('off')
#plt.show()
#plt.savefig('prova.png')

"""
import pandas as pd
import plotly.express as px

df = pd.read_csv('promossi.csv')

plt = px.treemap(df, path= [df['Anno']],values=df['Percentuale'],color=df['Promossi'])
plt.show()
plt.savefig('prova.png')

"""