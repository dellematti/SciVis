import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


links = {"2022-2021":[
            "https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022-Bis/riassu.php",
            "https://boldi.di.unimi.it/Corsi/Inf2021/AppelloFebbraio2022/riassu.php",
            "https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGiugno2022/riassu.php",
            "https://boldi.di.unimi.it/Corsi/Inf2021/AppelloLuglio2022/riassu.php",
            "https://boldi.di.unimi.it/Corsi/Inf2021/AppelloSettembre2022/riassu.php"
            ],
         "2021-2020":[
             "https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGennaio2021-Bis/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2020/AppelloFebbraio2021/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGiugno2021/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2020/AppelloLuglio2021/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2020/AppelloSettembre2021/riassu.php"
            ],
         "2020-2019":[
             "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloFebbraio2020/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php"
            ],
         "2019-2018":[
             "https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGennaio2019/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2018/AppelloFebbraio2019/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGiugno2019/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2018/AppelloLuglio2019/riassu.php",
             "https://boldi.di.unimi.it/Corsi/Inf2018/AppelloSettembre2019/riassu.php"
            ],
        }


def estraiPassati():

    #aggiungere altro for 
    mappa = {"2022-2021":{"Entrambi":0,"Lab":0},"2021-2020":{"Entrambi":0,"Lab":0},"2020-2019":{"Entrambi":0,"Lab":0},"2019-2018":{"Entrambi":0,"Lab":0}}
    cont = 0
    for index in links:
        print(index)
        utenti = {}  
        for anni in links[index]:
            tabellePagina = pd.read_html(anni,match='Laboratorio')
            tabella = tabellePagina[0]
    
            for i in range(0,len(tabella)) : 
                matricola = str(tabella["Matricola"][i] )
                if anni == "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php":
                    lab = str(tabella["Laboratorio"][i])
                    if lab !="R" and lab != "A" and "S" not in lab :
                        if int(float(tabella["Laboratorio"][i])) >= 18 : 
                            if not(matricola in utenti):
                                utenti[matricola] = True
                                mappa[index]["Entrambi"] +=1
                else:
                    if 	str(tabella["Voto"][i]) != "Insuff." :
                        if not(matricola in utenti):
                            utenti[matricola] = True
                            mappa[index]["Entrambi"] +=1
                    else:
                        if cont>=2 and anni !="https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php" and anni != "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php" and anni != "https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php" :
                            if not(pd.isna(tabella["Scritto"][i])) and int(tabella["Scritto"][i]) < 16:
                                mappa[index]["Lab"]+=1
                        else:
                            if not(pd.isna(tabella["Orale"][i])): 
                                mappa[index]["Lab"]+=1     
        cont+=1 
    return mappa          

def main():
    ris = estraiPassati()
    x1 = ris['2022-2021']["Entrambi"]
    x2 = ris['2021-2020']["Entrambi"]
    x3 = ris['2020-2019']["Entrambi"]
    x4 = ris['2019-2018']["Entrambi"]
    df = pd.DataFrame(dict(graph=['2021-2022', '2020-2021', '2019-2020','2018-2019'],
         n=[ris['2022-2021']["Entrambi"], ris['2021-2020']["Entrambi"], ris['2020-2019']["Entrambi"],ris['2019-2018']["Entrambi"]], 
         m=[x1-ris['2022-2021']["Lab"], x2-ris['2021-2020']["Lab"], x3- ris['2020-2019']["Lab"],x4-ris['2019-2018']["Lab"]]
         )) 

    ind = np.arange(len(df))
    width = 0.4

    fig, ax = plt.subplots()
    l1 = ax.barh(ind, df.n, width, color='#615959', label='Promossi')
    l2 = ax.barh(ind + width, df.m, width, color='#35B6BA', label='Promossi solo lab')
    ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
    ax.legend()
    plt.title("Promossi vs Promossi al Lab")
    ax.bar_label(l1, fmt='%.0f')
    ax.bar_label(l2, fmt='%.0f')

    plt.show()
    plt.savefig('oralevslab.svg')
    print(ris)
    
main()


