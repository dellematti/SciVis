import matplotlib.pyplot as plt
import pandas as pd

#Anno2022
def votiStatale():
    links = ["https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloFebbraio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGiugno2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloLuglio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloSettembre2022/riassu.php"]    
    passati={"Gennaio":0,"Febbraio":0,"Giugno":0,"Luglio":0,"Settembre":0}
    keys=[]
    keys.extend(list(passati.keys()))
    cont = 0
    
    for att in links:
        matricole = {}
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        for i in range(0,len(tabella)):
            matricole[tabella["Matricola"][i]] = tabella["Voto"][i]
        
        for key,value in matricole.items():
            if value != "Insuff.":
                passati[keys[cont]] +=1
        cont+=1

    return passati.values()

def grafo():#Anno 2021-2022
    Messina = [0,71, 29, 7, 4, 3] #ottenute da scripit EstraiMessian
    totMessina = 0 
    totStatale = 0
    for i in Messina : 
        totMessina+=i

    statale = votiStatale()
    statale =  [i for i in statale]
    for i in statale : 
        totStatale+=i
    
    for i in range (1,len(Messina)):
        Messina[i]=round((Messina[i]/totMessina)*100)
        
    for i in range (0,len(statale)):
        statale[i]=round((statale[i]/totStatale)*100)
    
    statale.insert(0,0)
    statale[1]+=1
    print(statale)
    print(Messina)
    
    x = ["0","Gennaio","Febbraio","Giugno","Luglio","Settembre"]
    
    fig = plt.figure()
    fig.patch.set_facecolor("#f6faf9")
    ax = fig.add_subplot(1, 1, 1)
    ax.grid(axis='y',color = '#d9d9d9', linestyle = '-', linewidth = 0.5)

    plt.fill_between(x, Messina, color="lightpink",alpha=0.5,label='Messina')
    plt.fill_between(x, statale, color="skyblue",alpha=0.5, label='Statle')
    plt.ylim(-10,100)
    plt.plot(x, Messina,linestyle='-', marker='.', color="lightpink")
    plt.plot(x, statale,linestyle='-', marker='.', color="skyblue")
    
    for tmpx,tmpy in zip(x,Messina):
        print(tmpy)
        label = str(tmpy)+"%"
        plt.annotate(label,
                 (tmpx,tmpy),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='lightpink'))
        
    for tmpx,tmpy in zip(x,statale):
        label = str(tmpy)+"%"
        plt.annotate(label,
                 (tmpx,tmpy),
                 textcoords="offset points",
                 xytext=(0,20),
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='skyblue'))

    #spazio = 0.400
    #fig.subplots_adjust(bottom=spazio)

    plt.legend()
    ax = plt.gca()
    ax.set_facecolor("#f6faf9")
    plt.ylabel('Percentuale')

    plt.show()
    plt.savefig("anno2020.svg") 
   

grafo()
    