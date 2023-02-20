import pandas as pd

#Script per prendere il numero di passati e bocciati dal voto di ceselli a quello di boldi
def votiCe():
    path = ["20-01-2020.xlsx","18-02-2020.xlsx","18-06-2020.xlsx","08-07-2020.xlsx","14-09-2020.xlsx"]
    matricole = {}
    cont = 0
    passati = [0,0,0,0,0]
    bocciati = [0,0,0,0,0]
    
    for file in path :
        voto = "Range"
        if file == "20-01-2020.xlsx":
            voto = "Valutazione"
            
        tmp = {}
        df = pd.read_excel('Voti2020/'+file) 
        for i in range(0,len(df)-1):
            key = df["Cognome"][i].replace(" ", "")+df["Nome"][i].replace(" ", "")
            matricole[key] = df[voto][i]
            tmp[key] = df[voto][i]
            
        for key,value in tmp.items():
            if value == 'A' or value == 'B' or value=='C' or value=='D':
                passati[cont] +=1
            else:
                bocciati[cont] +=1 
        
        cont+=1
    
    print("tot studenti ceselli :", len(matricole))
    return passati, bocciati

def votiBo():
    links = ["https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGennaio2020-Bis/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloFebbraio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloGiugno2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloLuglio2020/riassu.php","https://boldi.di.unimi.it/Corsi/Inf2019/AppelloSettembre2020/riassu.php"]
    matricole = {}
    passati = [0,0,0,0,0]
    bocciati = [0,0,0,0,0]
    cont = 0
    
    for att in links:
        tmp = {}
        tabellePagina = pd.read_html(att,match='Laboratorio')
        tabella = tabellePagina[0]
        
        for i in range(0,len(tabella)):
            if tabella["Laboratorio"][i]=="A" or tabella["Voto"][i]=="Insuff.":
                    matricole[tabella["Matricola"][i]] = "Insuff."
                    tmp[tabella["Matricola"][i]] = "Insuff."
            else:
                if tabella["Voto"][i] == "30L" or tabella["Voto"][i] == "30 e lode":
                    matricole[tabella["Matricola"][i]] = "30"
                    tmp[tabella["Matricola"][i]] = "30"
                else:
                    matricole[tabella["Matricola"][i]] = tabella["Voto"][i]
                    tmp[tabella["Matricola"][i]] = tabella["Voto"][i]

        for key,value in tmp.items():
            if value != "Insuff.":
                passati[cont]+=1
            else:
                bocciati[cont]+=1
        cont+=1
     
    print("tot studenti boldi :", len(matricole))   
    return passati,bocciati

def main():
    passatiCe, bocciatiCe = votiCe()
    print("ceselli: ",passatiCe,bocciatiCe)
    passatiBo, bocciatiBo = votiBo()
    print("boldi",passatiBo,bocciatiBo)  
    
main()