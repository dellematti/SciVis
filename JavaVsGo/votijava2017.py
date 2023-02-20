import pandas as pd

def estraivoti():
    matricole = {}
    links = ["https://boldi.di.unimi.it/Corsi/Inf2016/AppelloGennaio2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloFebbraio2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloGiugno2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloLuglio2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloSettembre2017/riass.php"]
    anno = "2017"
    mesi = ["Gennaio","Febbario","Giugno","Luglio","Settembre"]
    cont = 0
    linguaggi = "Java"
    
    for att in links :
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        for i in range(0, len(tabella)):
            voto = tabella["Voto"][i]
            if voto == "30L" or voto == "30 e lode":
                voto = "30"   
            key = str(tabella["Matricola"][i]) 
            if  not pd.isna(tabella["Voto verbalizzato"][i]) :
                matricole[key] = [tabella["Media"][i],mesi[cont],anno,linguaggi]
        
        cont+=1
        
    promossi ={"Gennaio":0,"Febbario":0,"Giugno":0,"Luglio":0,"Settembre":0}
    for key,value in matricole.items() :
        promossi[value[1]]+=1
    print(promossi)
    
estraivoti()