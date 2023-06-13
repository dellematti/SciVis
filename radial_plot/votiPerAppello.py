import pandas as pd
import requests
import pprint      #per stampare il dizionario




def riempiValori(voti, df):
    for x in df.index :
        voto = ""
        for i in df.iloc[[x]]['Laboratorio'] :
            voto += str(i) 
            # print("\n" +voto)
            if voto == "R" or voto == "S" or voto == "A" or len(voto) > 5  :    # or int(voto) < 18   !!!!
                voti[0] += 1
                # print("bocciato")
            elif int(float (voto)) < 18:
                voti[0] += 1
                # print("bocciato")
            else :
                # print("promosso")
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
    for voto, quantiConQuelVoto in enumerate (voti) :
        # print("Passati col ", voto+17 , " :\t", quantiConQuelVoto)
        totaleStudenti += quantiConQuelVoto
    totalePromossi = totaleStudenti - voti[0]
    # print ("totale studenti promossi : ",totalePromossi )
    # print ("totale studenti non promossi in quell appello : ",voti[0] )
    # print ("totale studenti : ",totaleStudenti )
    print("percentuale di promossi : " ,"{:.2f}".format((totalePromossi/totaleStudenti)*100), "\t","totale studenti : ",totaleStudenti   )  





#devo usare gli anni prima del 2018 per i risultati in java, e dopo il 2018 per quelli in go


appelli = []

# file = open(r"C:\\Users\\delle\\Desktop\\Informatica\\Programmi\\programmiPython\\ScrapingTentativi\\linkAppelli.txt","r")
file = open(r"linkAppelli.txt","r")
righe = file.readlines()  
for riga in righe:
    if riga != '\n' :
        appelli.append(riga.strip())   #strip toglie lo \n da fine riga
file.close()



# nelle mappe associo ad ogni studente tutti i suoi risultati
voti16_17Gennaio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti16_17Febbraio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti16_17Giugno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti16_17Luglio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti16_17Settembre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

voti17_18Gennaio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti17_18Febbraio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti17_18Giugno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti17_18Luglio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
voti17_18Settembre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# da qua
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

    if idx == 10 :                   
        riempiValori(voti18_19Gennaio, df)     
    if idx == 11 :
        riempiValori(voti18_19Febbraio, df) 
    if idx == 12 :
        riempiValori(voti18_19Giugno, df) 
    if idx == 13 :
        riempiValori(voti18_19Luglio, df) 
    if idx == 14 :
        riempiValori(voti18_19Settembre, df) 
    if idx == 15 :                   
        riempiValori(voti19_20Gennaio, df)     
    if idx == 16 :
        riempiValori(voti19_20Febbraio, df) 
    if idx == 17 :
        riempiValori(voti19_20Giugno, df) 
    if idx == 18 :
        riempiValori(voti19_20Luglio, df) 
    if idx == 19 :
        riempiValori(voti19_20Settembre, df) 
    if idx == 20 :
        riempiValori(voti20_21Gennaio, df) 
    if idx == 21 :
        riempiValori(voti20_21Febbraio, df) 
    if idx == 22 :
        riempiValori(voti20_21Giugno, df) 
    if idx == 23 :
        riempiValori(voti20_21Luglio, df) 
    if idx == 24 :
        riempiValori(voti20_21Settembre, df) 
    if idx == 25 :
        riempiValori(voti21_22Gennaio, df) 
    if idx == 26 :
        riempiValori(voti21_22Febbraio, df) 
    if idx == 27 :
        riempiValori(voti21_22Giugno, df) 
    if idx == 28 :
        riempiValori(voti21_22Luglio, df) 
    if idx == 29 :
        riempiValori(voti21_22Settembre, df) 






# print("\nRisultati degli studenti del 2016 2017 gennaio :\n")   
# print("\nRisultati degli studenti del 2016 2017 Febbraio :\n")   
# stampaDati(voti16_17Febbraio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
# print("\nRisultati degli studenti del 2016 2017 giugno :\n")   
# stampaDati(voti16_17Giugno)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
# print("\nRisultati degli studenti del 2016 2017 luglio :\n")   
# stampaDati(voti16_17Luglio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
# print("\nRisultati degli studenti del 2016 2017 settembre :\n")   

print("\n18 19")                             
stampaDati(voti18_19Gennaio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti18_19Febbraio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti18_19Giugno)                                 
stampaDati(voti18_19Luglio)                                 
stampaDati(voti18_19Settembre)    

print("\n19 20")                             
stampaDati(voti19_20Gennaio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti19_20Febbraio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti19_20Giugno)                                 
stampaDati(voti19_20Luglio)                                 
stampaDati(voti19_20Settembre)                                 

print("\n20 21")                             
stampaDati(voti20_21Gennaio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti20_21Febbraio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti20_21Giugno)                                 
stampaDati(voti20_21Luglio)                                 
stampaDati(voti20_21Settembre)                                 

print("\n21 22")                             
stampaDati(voti21_22Gennaio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti21_22Febbraio)                                   #stampa il numero di studenti per ogni risultato ( di un certo anno)
stampaDati(voti21_22Giugno)                                 
stampaDati(voti21_22Luglio)                                 
stampaDati(voti21_22Settembre)                                 



