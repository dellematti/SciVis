import matplotlib as  plt
import pandas as pd


def anniNumeroPassati():
    links = ["https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGennaio2022-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloFebbraio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloGiugno2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloLuglio2022/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2021/AppelloSettembre2022/riassu.php"]
    links.extend(["https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGennaio2021-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloFebbraio2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloGiugno2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloLuglio2021/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2020/AppelloSettembre2021/riassu.php"])
    links.extend(["https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloFebbraio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php"])
    links.extend(["https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGennaio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloFebbraio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloGiugno2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloLuglio2019/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2018/AppelloSettembre2019/riassu.php"])
    links.extend (["https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGennaio2018/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloFebbraio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloGiugno2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloLuglio2018/riass.php","https://boldi.di.unimi.it/Corsi/Inf2017/AppelloSettembre2018/riass.php"])

    anni = {"2018":{"Gennaio":0,"Febbraio":0,"Giugno":0,"Luglio":0,"Settembre":0},"2019":{"Gennaio":0,"Febbraio":0,"Giugno":0,"Luglio":0,"Settembre":0},"2020":{"Gennaio":0,"Febbraio":0,"Giugno":0,"Luglio":0,"Settembre":0},"2021":{"Gennaio":0,"Febbraio":0,"Giugno":0,"Luglio":0,"Settembre":0},"2022":{"Gennaio":0,"Febbraio":0,"Giugno":0,"Luglio":0,"Settembre":0}}
    matricole={}
    keys = ["2022","2021","2020","2019","2018"]
    mesi = list(anni["2018"].keys())
    contAnni = 0
    contMesi = 0
    
    for att in links:
        if contMesi == 5:
            contMesi = 0
            contAnni +=1
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        for i in range(0,len(tabella)):
            matricole[tabella["Matricola"][i]] = [tabella["Voto"][i],mesi[contMesi],keys[contAnni]]  

        contMesi+=1
        
    for key,value in matricole.items():
        if value[0] != "Insuff.":
            anni[value[2]][value[1]]+=1
    
    return anni


def main():
    anni = anniNumeroPassati()
    print(anni)

main()