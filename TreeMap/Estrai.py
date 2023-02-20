import pandas as pd
import csv

def scriviPromossi(promossi,bocciati,anno):
    campi = ["Matricola","Voto","Anno","Mese","Linguaggio","MeseNum"]
    with open('promossi.csv', 'a') as f:
        w = csv.writer(f,campi)
        cur = [anno,promossi,bocciati]
        w.writerow(cur)

def promossibocciati():
    
    links = ["https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloFebbraio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGiugno2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloLuglio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloSettembre2022/riassu.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGennaio2021-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloFebbraio2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGiugno2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloLuglio2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloSettembre2021/riassu.php"] 
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloFebbraio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGennaio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloFebbraio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGiugno2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloLuglio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloSettembre2019/riassu.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGennaio2018/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloFebbraio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGiugno2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloLuglio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloSettembre2018/riass.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2016/AppelloGennaio2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloFebbraio2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloGiugno2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloLuglio2017/riass.php","https://boldi.di.unimi.it/Corsi/Inf2016/AppelloSettembre2017/riass.php"]
    
    matricole = {}
    anno = "2022"
    mesi = ["Gennaio","Febbario","Giugno","Luglio","Settembre"]
    cont = 0
    #linguaggi = "Java"
    
    for att in links :
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        for i in range(0, len(tabella)):
            voto = tabella["Voto"][i]
            if voto == "30L" or voto == "30 e lode":
                voto = "30"   
            key = str(tabella["Matricola"][i]) 
            matricole[key] = [voto,mesi[cont],anno]
        
        cont+=1
    
    promossi = 0
    boccciati = 0
    for key,value in matricole.items():
        if value[0] != "Insuff.":
            promossi+=1
        else:
            boccciati+=1
            
    print("anno :",anno,"promossi: ",promossi," bocciati: ",boccciati)
    scriviPromossi(promossi,boccciati,anno)

promossibocciati()