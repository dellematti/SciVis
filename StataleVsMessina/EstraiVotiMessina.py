import pandas as pd

#altri dati presi da file condivisi simili al seguente https://docs.google.com/spreadsheets/d/1VI9SZtInuU2x2KZMb5S4jmzLh-VVo-1j/edit#gid=1613162
#in fondo c'è gia numero di passati e media voti
def main():
    
    matricole = {}
    df = pd.read_excel("2022/Gennaio.xlsx") 
    
    totPassati = 0
    totBocciati = 0
    for i in range (0,len(df["Voto"])):
        v = df["Voto"][i] 
        matricole[df["Matricola"][i]] = v
        if v >=18:
            totPassati+=1
        else:
            totBocciati+=1
            
    print("totPassati: ",totPassati,"totBocciati: ",totBocciati)

main()
