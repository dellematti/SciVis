import pandas as pd
import csv


def scriviFile(matricole):
    campi = ["Matricola","Voto","Anno","Mese","Linguaggio"]
    with open('mycsvfile.csv', 'w') as f:
        w = csv.writer(f,campi)
        for key,value in matricole.items():
            cur = []
            cur.append(key)
            for att in value:
                cur.append(att)
            if cur[1] != "Insuff.":
                if cur[1] == '30 e lode':
                    cur[1] = 30
                cur[1] = int(cur[1])
                w.writerow(cur)
                
def scriviFile2(matricole):
    campi = ["Matricola","Voto","Anno","Mese","Linguaggio","MeseNum"]
    with open('genfebrraio.csv', 'w') as f:
        w = csv.writer(f,campi)
        for key,value in matricole.items():
            cur = []
            cur.append(key)
            for att in value:
                cur.append(att)
            #if cur[1] != "Insuff.":
               # if cur[1] == '30 e lode':
                    #cur[1] = 30
            cur[1] = float(cur[1])
            w.writerow(cur)
            
    
def estariVoti():
    links = ["https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGennaio2018/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloFebbraio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGiugno2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloLuglio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloSettembre2018/riass.php"]
    matricole = {}
    mesi = ["Gennaio","Febbraio","Giugno","Luglio","Settembre"]
    anno = "2018"
    linguaggi = "Java"
    cont = 0
    
    for att in links :
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        for i in range(0, len(tabella)):
            voto = tabella["Voto"][i]
            if voto == "30L" or voto == "30 e lode":
                voto = "30"   
            key = str(tabella["Matricola"][i]) 
           # if mesi[cont]=="Gennaio" or mesi[cont]=="Febbraio":
            if  tabella["Voto"][i] !=  "Insuff.":
                matricole[key] = [tabella["Media"][i],mesi[cont],anno,linguaggi]

        cont+=1
        #print(len(matricole))
        
    print(matricole,len(matricole))
    #scriviFile(matricole)
    #scriviFile2(matricole)
    
def main():
    estariVoti()

main()