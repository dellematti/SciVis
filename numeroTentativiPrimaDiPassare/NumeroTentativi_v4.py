import pandas as pd
import requests
import pprint      #per stampare il dizionario


def riempiMappa(mappa, df):
  for x in df.index :
    voto = ""
    for i in df.iloc[[x]]['Voto'] :
        voto += str(i) 

    matricola = ""
    for i in df.iloc[[x]]['Matricola'] :
        matricola += str(i) 

    
    mappa.setdefault(matricola, []).append(voto)




    
mappa = dict()
appelli = []


# li metto scritti qua e non in un file per comodità, per non dover riscrivere il path per aprire il file in base al computer

#2016/2017
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2016/AppelloGennaio2017/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2016/AppelloFebbraio2017/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2016/AppelloGiugno2017/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2016/AppelloLuglio2017/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2016/AppelloSettembre2017/riass.php' )

#2017/2018
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGennaio2018/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2017/AppelloFebbraio2018/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGiugno2018/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2017/AppelloLuglio2018/riass.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2017/AppelloSettembre2018/riass.php' )

#2018/2019
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGennaio2019/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2018/AppelloFebbraio2019/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGiugno2019/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2018/AppelloLuglio2019/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2018/AppelloSettembre2019/riassu.php')

# 2019 / 2020
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2019/AppelloFebbraio2020/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php')
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php')

# 2020 / 2021
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGennaio2021/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGennaio2021-Bis/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2020/AppelloFebbraio2021/riassu.php' )
appelli.append( 'https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGiugno2021/riassu.php')
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2020/AppelloLuglio2021/riassu.php')
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2020/AppelloSettembre2021/riassu.php')

# 2021 / 2022
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022-Bis/riassu.php' )
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2021/AppelloFebbraio2022/riassu.php' )
appelli.append( 'https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGiugno2022/riassu.php')
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2021/AppelloLuglio2022/riassu.php')
appelli.append('https://boldi.di.unimi.it/Corsi/Inf2021/AppelloSettembre2022/riassu.php')



for idx, url in enumerate (appelli) :
    dfs = pd.read_html(appelli[idx])
    table_MN = pd.read_html(appelli[idx])     # guardo quante tabelle ci sono nella pagina
    num_tabelle = len(table_MN)               
    df = dfs[num_tabelle - 1]               # perchè tanto so che la tabella che mi serve è l ultima
    riempiMappa(mappa, df)    


pprint.pprint(mappa)                      #così me la stampa andando a capo ogni riga

tentativi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for matr in mappa :
    if (mappa[matr][len(mappa[matr]) - 1] != "Insuff."):
        tentativi[len(mappa[matr]) - 1] += 1

totale = 0
divisore = 0
for appello, studenti in enumerate (tentativi) :
    totale += ((appello+1) * studenti)
    divisore += studenti 
    print("Passato al tentativo n. ", appello+1 , " :\t", studenti)

print("media tentativi per persona : ")
print(totale/divisore)