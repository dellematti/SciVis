import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def totAnni(df, linguaggio):
     i=0
     if linguaggio !="Java":
        i = 2
          
     mappa = {"0-17":0,"18-21":0,"22-25":0,"26-28":0,"29-30":0}
     tot = 0 
     for column, item in df.items():
          if column in mappa:
               mappa[column] = item[i]+item[i+1]  
          if column == "Tot":
              tot =  item[i]+item[i+1]  
         
     #print(mappa)     
     for key,value in mappa.items():
          mappa[key] = round(value/tot*100)
          
     return mappa    
          
def main():
     df = pd.read_csv("javavsgo.csv", sep = ";", encoding = "utf-8")
     java = totAnni(df,"Java")
     golang = totAnni(df,"Golang")
     print(java)
     print(golang)
     
     
     
main()


