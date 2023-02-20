import pandas as pd
import re
import nltk
from nltk.corpus import stopwords


def unisciPolarity(fileName):

    df = pd.read_csv(fileName, on_bad_lines='skip')
    df.drop(columns=["subj", "iro", "lpos", "lneg", "top"],axis=1, inplace=True)
    """"
    Descrizione dataset :
    • 10: positive polarity
    • 01: negative polarity
    • 11: mixed polarity
    • 00: no polarity
    """
    polarity=[]
    cont=0
    for pos in df["opos"]:
        neg = df["oneg"][cont]
        if pos == 1 and neg == 0:
            polarity.append("positive")
        if pos == 0 and neg == 1:
            polarity.append("negative")
       # if pos == 1 and neg == 1:
          # polarity.append("mixed")
        #if pos == 0 and neg == 0:
         #  polarity.append("neutral")
        cont+=1

    df.drop(columns=["oneg","opos"], axis=1, inplace=True)
    df["polarity"] = pd.Series(polarity)

    return df

def pulisciTesto(messaggi):

    messaggiPuliti = []
    stops = set(stopwords.words('italian'))
    stopword = [' ' + x + ' ' for x in stops] #In questo modo non toglie stop word all'intenro di una parola.

    for messaggio in messaggi:

        messaggio = messaggio.lower()
        messaggio = re.sub(r'http\S+', '', messaggio) #rimuovo i link contenuti nei messaggi
        messaggio = re.sub('@[\w]*[_-]*[\w]*', '', messaggio) #rimuovo le menzioni presenti nei tweet
        messaggio = re.sub(r'[^\w\s]', '', messaggio) #rimuovo punteggiatura
        messaggio = re.sub('\s+', ' ', messaggio)  # rimuovo spazi in eccesso

        for tmp in stopword:
           messaggio = messaggio.replace(tmp, ' ')

        messaggio = re.sub('^ ', '', messaggio)  # rimuovo spazio inizio
        messaggio = re.sub(' $', '', messaggio)  # rimuovo spazio alla fine
        messaggiPuliti.append(messaggio)

    return messaggiPuliti

def main():
    #training_set_sentipolc.csv
    #test_set_sentipolc16_gold2000.csv
    fileName ="training_set_sentipolc.csv"
    df = unisciPolarity(fileName)
    df["text"] = pulisciTesto(df["text"])
    df.to_csv("Ris/prova2.csv", sep='\t', encoding='utf-8')

    print(df.sample(10))
    #print(df["polarity"].value_counts())


main()