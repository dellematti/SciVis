import pandas as pd
import requests
import pprint      #per stampare il dizionario


# QUESTO SERVE PER SAPERE I VOTI DEGLI ESAMI IN OGNI SINGOLO APPELLO
def riempiValori(voti, df):
    for x in df.index :
        voto = ""
        for i in df.iloc[[x]]['Laboratorio'] :
            voto += str(i) 
            if voto == "R" or voto == "S" or voto == "A" or len(voto) > 5 :    
                voti[0] += 1
            else :
                votoFloat = float(voto)
                votoInt = int(votoFloat)
                if votoInt > 30 :
                    voti[len(voti) -1] += 1
                else:
                    voti[ votoInt -17] += 1




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
    print ("totale studenti promossi : ",totalePromossi )
    print ("totale studenti non promossi in quell appello : ",voti[0] )
    print("percentuale di promossi : " ,"{:.2f}".format((totalePromossi/totaleStudenti)*100) )  
    percentualePromossi = (totalePromossi / totaleStudenti) * 100
    percentualeBocciati = (voti[0] / totaleStudenti) * 100
    return percentualePromossi, percentualeBocciati




#devo usare gli anni prima del 2018 per i risultati in java, e dopo il 2018 per quelli in go


appelli = []

# file = open(r"C:\\Users\delle\Desktop\\Informatica\\Programmi\\programmiPython\ScrapingTentativi\\linkAppelli.txt","r")
file = open(r"linkAppelli.txt","r")
righe = file.readlines()  
for riga in righe:
    if riga != '\n' :
        appelli.append(riga.strip())   #strip toglie lo \n da fine riga
file.close()

#print(appelli)

# nelle mappe associo ad ogni studente tutti i suoi risultati
voti18_19Gennaio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti18_19Febbraio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti18_19Giugno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti18_19Luglio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti18_19Settembre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

voti19_20Gennaio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti19_20Febbraio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti19_20Giugno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti19_20Luglio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti19_20Settembre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

voti20_21Gennaio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti20_21Febbraio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti20_21Giugno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti20_21Luglio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti20_21Settembre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

voti21_22Gennaio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti21_22Febbraio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti21_22Giugno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti21_22Luglio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti21_22Settembre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# per ogni appello riempio la mappa, so che ogni mappa tiene conto dei 5 appelli di ogni anno, quindi decido che mappa riempire
# in base al numero dell appello che sto guardando
for idx, url in enumerate (appelli) :
    dfs = pd.read_html(appelli[idx])
    table_MN = pd.read_html(appelli[idx])     # guardo quante tabelle ci sono nella pagina
    num_tabelle = len(table_MN)               
    df = dfs[num_tabelle - 1]                 # perchè tanto so che la tabella che mi serve è l ultima

    print(idx)
    #idx è il numero dell appello, 0 è gennaio del 2016, 5 gennaio del 2017, 6 febbraio del 17 e cosi via

    if idx == 0 :                   
        riempiValori(voti18_19Gennaio, df) 
    if idx == 1 :
        riempiValori(voti18_19Febbraio, df) 
    if idx == 2 :
        riempiValori(voti18_19Giugno, df) 
    if idx == 3 :
        riempiValori(voti18_19Luglio, df) 
    if idx == 4 :
        riempiValori(voti18_19Settembre, df) 
    if idx == 5 :                   
        riempiValori(voti19_20Gennaio, df) 
    if idx == 6 :
        riempiValori(voti19_20Febbraio, df) 
    if idx == 7 :
        riempiValori(voti19_20Giugno, df) 
    if idx == 8 :
        riempiValori(voti19_20Luglio, df) 
    if idx == 9 :
        riempiValori(voti19_20Settembre, df) 
    if idx == 10 :                   
        riempiValori(voti20_21Gennaio, df) 
    if idx == 11 :
        riempiValori(voti20_21Febbraio, df) 
    if idx == 12 :
        riempiValori(voti20_21Giugno, df) 
    if idx == 13 :
        riempiValori(voti20_21Luglio, df) 
    if idx == 14 :
        riempiValori(voti20_21Settembre, df) 
    if idx == 15 :                   
        riempiValori(voti21_22Gennaio, df) 
    if idx == 16 :
        riempiValori(voti21_22Febbraio, df) 
    if idx == 17 :
        riempiValori(voti21_22Giugno, df) 
    if idx == 18 :
        riempiValori(voti21_22Luglio, df) 
    if idx == 19 :
        riempiValori(voti21_22Settembre, df) 



strOutPr = ""
strOutBo = ""

print("\nRisultati degli studenti del 2018 2019 gennaio :\n")   
percPromossi, percBocciati = stampaDati(voti18_19Gennaio)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)

#2018-19:
print("\nRisultati degli studenti del 2018 2019 Febbraio :\n")   
percPromossi, percBocciati = stampaDati(voti18_19Febbraio)    
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '                               #stampa il numero di studenti per ogni risultato ( di un certo anno)
print("\nRisultati degli studenti del 2018 2019 giugno :\n")   
percPromossi, percBocciati = stampaDati(voti18_19Giugno)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2018 2019 luglio :\n")   
percPromossi, percBocciati = stampaDati(voti18_19Luglio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2018 2019 settembre :\n")   
percPromossi, percBocciati = stampaDati(voti18_19Settembre)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + '\n'
strOutBo += str(int(percBocciati)) + '\n'

#2019-20:
print("\nRisultati degli studenti del 2019 2020 gennaio :\n")   
percPromossi, percBocciati = stampaDati(voti19_20Gennaio)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2019 2020 Febbraio :\n")   
percPromossi, percBocciati = stampaDati(voti19_20Febbraio)    
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '                               #stampa il numero di studenti per ogni risultato ( di un certo anno)
print("\nRisultati degli studenti del 2019 2020 giugno :\n")   
percPromossi, percBocciati = stampaDati(voti19_20Giugno)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2019 2020 luglio :\n")   
percPromossi, percBocciati = stampaDati(voti19_20Luglio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2019 2020 settembre :\n")   
percPromossi, percBocciati = stampaDati(voti19_20Settembre)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + '\n'
strOutBo += str(int(percBocciati)) + '\n'

#2020-21:
print("\nRisultati degli studenti del 2019 2020 gennaio :\n")   
percPromossi, percBocciati = stampaDati(voti20_21Gennaio)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2020 2021 Febbraio :\n")   
percPromossi, percBocciati = stampaDati(voti20_21Febbraio)    
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '                               #stampa il numero di studenti per ogni risultato ( di un certo anno)
print("\nRisultati degli studenti del 2020 2021 giugno :\n")   
percPromossi, percBocciati = stampaDati(voti20_21Giugno)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2020 2021 luglio :\n")   
percPromossi, percBocciati = stampaDati(voti20_21Luglio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2020 2021 settembre :\n")   
percPromossi, percBocciati = stampaDati(voti20_21Settembre)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + '\n'
strOutBo += str(int(percBocciati)) + '\n'

#2021-22:
print("\nRisultati degli studenti del 2021 2022 gennaio :\n")   
percPromossi, percBocciati = stampaDati(voti21_22Gennaio)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2021 2022 Febbraio :\n")   
percPromossi, percBocciati = stampaDati(voti21_22Febbraio)    
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '                               #stampa il numero di studenti per ogni risultato ( di un certo anno)
print("\nRisultati degli studenti del 2021 2022 giugno :\n")   
percPromossi, percBocciati = stampaDati(voti21_22Giugno)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2021 2022 luglio :\n")   
percPromossi, percBocciati = stampaDati(voti21_22Luglio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi)) + ' '
strOutBo += str(int(percBocciati)) + ' '
print("\nRisultati degli studenti del 2021 2022 settembre :\n")   
percPromossi, percBocciati = stampaDati(voti21_22Settembre)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
strOutPr += str(int(percPromossi))
strOutBo += str(int(percBocciati))


with open('percentuali_promossi.txt', 'w') as fileOut1:
    fileOut1.write(strOutPr)

with open('percentuali_bocciati.txt', 'w') as fileOut2:
    fileOut2.write(strOutBo)
