import pandas as pd
import requests
import pprint      #per stampare il dizionario


# QUESTO SERVE PER SAPERE I VOTI CHE LE MATRICOLE HANNO OTTENUTO DURANTE L ANNO ACCADEMICO, PER L ESAME DI PROG 1, 
# IL PROGRAMMA DARA' IN OUTPUT SIA LE PERCENTUALI TOTALI DEI RISULTATI OTTENUTI NEGLI ANNI IN CUI SI USAVA 
# JAVA, SIA LE PERCENTUALI TOTALI DEGLI ANNI IN CUI SI USA GO



# riempie la mappa che collega ad ogni studente tutti i voti che ha preso
def riempiMappa(mappa, df):
    for x in df.index :
        voto = ""
        for i in df.iloc[[x]]['Voto'] :
            voto += str(i) 

        matricola = ""
        for i in df.iloc[[x]]['Matricola'] :
            matricola += str(i) 
        # tengo conto solo di go perchè tengo conto solo delle matricole, e nell anno in cui era possibile scegliere tra
        # i due linguaggi, go era per le matricole (se c è la colonna Ling. tengo solo le righe con Go)
        if 'Ling.' in df.columns:   
            linguaggio = ""
            for i in df.iloc[[x]]['Ling.'] :
                linguaggio += i 
            if linguaggio == "Go" :            
                mappa.setdefault(matricola, []).append(voto)
        else :
            mappa.setdefault(matricola, []).append(voto)




# restituisce un array di voti, il voto in prima posizione è insufficiente gli altri sono da 18 a 30, l ultima posizione 
# equiavale al 30 e lode
def ottieniVoti(mappa, ):
    voti = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for matr in mappa :                                     #guardo solo l ultimo voto preso dallo studente
        if mappa[matr][len(mappa[matr])-1] == "Insuff.":    
            voti[0] += 1
        elif mappa[matr][len(mappa[matr])-1] == "30 e lode" or mappa[matr][len(mappa[matr])-1] == "30L" :
            voti[len(voti) -1] += 1
        else:
            voti[int (mappa[matr][len(mappa[matr])-1]) -17] += 1
    return voti




# restituisce un array di percentuali. La percentuale equivale al numero di studenti passati con un certo risultato, rispetto al
# numero totale di studenti immatricolati quell anno   
def ottieniVotiPercentuale(voti):
    percentuali = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
    totaleStudenti = 0                                 
    for voto, quantiConQuelVoto in enumerate (voti) :
        totaleStudenti += quantiConQuelVoto
    for voto, quantiConQuelVoto in enumerate (voti) :
        percentuali[voto] = voti[voto] / totaleStudenti
    return percentuali




# stampa in base all anno: il numero di studenti per ogni voto, il numero totale di studenti, il numero di
# studenti promossi e il numero di studenti non promossi
def stampaDati(voti):
    totaleStudenti = 0                                 
    # print("\nRisultati degli studenti del 2018 2019 :\n")
    for voto, quantiConQuelVoto in enumerate (voti) :
        print("Passati col ", voto+17 , " :\t", quantiConQuelVoto)
        totaleStudenti += quantiConQuelVoto
    print ("totale studenti : ",totaleStudenti )
    totalePromossi = totaleStudenti - voti[0]
    print ("totale studenti promossi : ", totalePromossi)
    print ("totale studenti non promossi in quell'anno : ", voti[0])
    return voti[0]


#devo usare gli anni prima del 2018 per i risultati in java, e dopo il 2018 per quelli in go
appelli = []

with open('input.txt') as file:
    righe = file.readlines()

#file = open("C:\\Users\Andrea\Desktop\\Prova estrazioni\\input.txt", "r")
#righe = file.readlines()

for riga in righe:
    if riga != '\n' :
        appelli.append(riga.strip())   #strip toglie lo \n da fine riga
file.close()




# nelle mappe associo ad ogni studente tutti i suoi risultati
mappa16_17 = dict()
mappa17_18 = dict()

mappa18_19 = dict()
mappa19_20 = dict()

mappa20_21 = dict()
mappa21_22 = dict()



# per ogni appello riempio la mappa, so che ogni mappa tiene conto dei 5 appelli di ogni anno, quindi decido che mappa riempire
# in base al numero dell appello che sto guardando
for idx, url in enumerate (appelli) :
    dfs = pd.read_html(appelli[idx])
    table_MN = pd.read_html(appelli[idx])     # guardo quante tabelle ci sono nella pagina
    num_tabelle = len(table_MN)               
    df = dfs[num_tabelle - 1]                 # perchè tanto so che la tabella che mi serve è l ultima

    if idx < 5 :
        riempiMappa(mappa16_17, df)   
    elif idx >= 5 and idx < 10 : 
        riempiMappa(mappa17_18, df)   
    elif idx >= 10 and idx < 15 :
        riempiMappa(mappa18_19, df)   
    elif idx >= 15 and idx < 20 :
        riempiMappa(mappa19_20, df)   
    elif idx >= 20 and idx < 25 :
        riempiMappa(mappa20_21, df)   
    elif idx >= 25 and idx < 30 :
        riempiMappa(mappa21_22, df)   



# voti è un array in cui ho il numero di studenti per ogni risultato (conto solo l ultimo risultato di ogni studente)
voti16_17 = ottieniVoti(mappa16_17)  
voti17_18 = ottieniVoti(mappa17_18)
voti18_19 = ottieniVoti(mappa18_19) 
voti19_20 = ottieniVoti(mappa19_20) 

voti20_21 = ottieniVoti(mappa20_21) 
voto21_22 = ottieniVoti(mappa21_22)

strOutput = ""

print("\nRisultati degli studenti del 2018 2019 :\n")   
bocciati = stampaDati(voti16_17)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutput += str(bocciati)
strOutput += ' '
print("\nRisultati degli studenti del 2019 2020 :\n")   
bocciati = stampaDati(voti17_18)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutput += str(bocciati)
strOutput += ' '
print("\nRisultati degli studenti del 2020 2021 :\n")   
bocciati = stampaDati(voti18_19)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutput += str(bocciati)
strOutput += ' '
print("\nRisultati degli studenti del 2021 2022 :\n")   
bocciati = stampaDati(voti19_20)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutput += str(bocciati)
#print("\nRisultati degli studenti del 2020 2021 :\n")   
#stampaDati(voti20_21)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
#print("\nRisultati degli studenti del 2021 2022 :\n")   
#stampaDati(voto21_22)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)



percentuali16_17 = ottieniVotiPercentuale(voti16_17)
percentuali17_18 = ottieniVotiPercentuale(voti17_18)
percentuali18_19 = ottieniVotiPercentuale(voti18_19)
percentuali19_20 = ottieniVotiPercentuale(voti19_20)
# for idx, percentuale in enumerate (percentuali16_17) :      #questo stampa le percentuali
#     print(idx+17, "{:.2f}".format(percentuale*100))




# gli anni 16-17 e 17-18 sono i risultati in Java, invece 18-19 e 19-20 sono in Golang
percentualiGeneraliJava = [0.0] * 15
for idx, percentuale in enumerate (percentualiGeneraliJava) :
    # percentualiGeneraliJava[idx] = (percentuali16_17[idx] + percentuali17_18[idx]) / 2
    percentualiGeneraliJava[idx] = ((percentuali16_17[idx] + percentuali17_18[idx]) / 2) * 100

percentualiGeneraliGolang = [0.0] * 15
for idx, percentuale in enumerate (percentualiGeneraliGolang) :
    # percentualiGeneraliGolang[idx] = (percentuali18_19[idx] + percentuali19_20[idx]) / 2
    percentualiGeneraliGolang[idx] =( (percentuali18_19[idx] + percentuali19_20[idx]) / 2) * 100




# print("Percentuale per risultato di tutti gli esami in java: ")  #percentuale totale Java
# for idx, percentuale in enumerate (percentualiGeneraliJava) :
#     print(idx+17, "{:.2f}".format(percentuale*100))
# print("Percentuale per risultato di tutti gli esami in Golang: ")  #percentuale totale Go
# for idx, percentuale in enumerate (percentualiGeneraliGolang) :
#     print(idx+17, "{:.2f}".format(percentuale*100))




# ORA POSSO USARE  percentualiGeneraliJava  E  percentualiGeneraliGolang   PER FARE IL GRAFICO




votiGeneraliJava = [0]*15
for idx, percentuale in enumerate (votiGeneraliJava) :
    votiGeneraliJava[idx] = voti16_17[idx] + voti17_18[idx]

with open('bocciati.txt', 'w') as fileOut:
    fileOut.write(strOutput)