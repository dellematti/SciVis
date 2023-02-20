import pandas as pd
import math

#Script per prendere i dati (voti, passati, bocciati) per quanto riguarda gli anni dal 2018 al 2022
def main():
    
    links = ["https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloFebbraio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGiugno2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloLuglio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloSettembre2022/riassu.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGennaio2021-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloFebbraio2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGiugno2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloLuglio2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloSettembre2021/riassu.php"] 
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloFebbraio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGennaio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloFebbraio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGiugno2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloLuglio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloSettembre2019/riassu.php"]
    #links = ["https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGennaio2018/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloFebbraio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGiugno2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloLuglio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloSettembre2018/riass.php"]
    
    matricole = {}
    creaMatricola(matricole,links)
    c1,c2,totale = creaRange(matricole)
    print(len(matricole))
    print("bocciati: ",c1)
    print("promossi: ",c2)
    print(totale)


def creaMatricola(matricole,links):
    for att in links:
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        for i in range(0,len(tabella)):
            
            if tabella["Laboratorio"][i]=="A" or tabella["Voto"][i]=="Insuff.":
                matricole[tabella["Matricola"][i]] = "Insuff."
            else:
                if tabella["Voto"][i] == "30L" or tabella["Voto"][i] == "30 e lode":
                    matricole[tabella["Matricola"][i]] = "30" 
                else:
                    matricole[tabella["Matricola"][i]] = tabella["Voto"][i]
                    
def creaRange(matricole):
    totBocciati = 0
    totPromossi = 0
    totale = dict.fromkeys(["18-21","22-25", "26-28", "29-30"],0)
    for key in matricole:
        if matricole[key] !="Insuff.":
            voto = int(matricole[key])
            votoRange(totale,voto)
            totPromossi+=1
        else:
            totBocciati+=1
            
    return totBocciati,totPromossi,totale

def votoRange(totale,cf):
    if cf >= 18 and cf <= 21 :
        totale["18-21"] += 1
    if cf >= 22 and cf <= 25 :
        totale["22-25"] += 1 
    if cf >= 26 and cf <= 28 :
        totale["26-28"] += 1 
    if cf >= 29 and cf <= 30 :
        totale["29-30"] += 1 
                    
main()