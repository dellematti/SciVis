from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd

def modello():

    df = pd.read_csv("Ris/prova2.csv", sep='\t',encoding='utf8') #leggo csv pulito.
    x = df["text"].fillna(' ') #input
    y = df["polarity"].fillna(' ')#output

    vect = TfidfVectorizer()
    #vect = CountVectorizer() #costruttore
    x = vect.fit_transform(x) #uso modello bag of words.

    x_train, x_test, y_train, y_test = train_test_split(x.toarray(),y,test_size=0.30, random_state=0) #divido il data set in 2 una parte per l'addestramento una per il test
    model = DecisionTreeClassifier(max_depth=15) #creo il modello vuoto non addestrato
    model.fit(x_train, y_train)

    predizioneTrain = model.predict(x_train)
    predizioneTest = model.predict(x_test)
    risTrain = accuracy_score(y_train,predizioneTrain)
    risTest = accuracy_score(y_test,predizioneTest)

    print(f'Train acc. {risTrain}, Test acc.{risTest}')
    
    plt.figure()
    tree.plot_tree(model,filled=True)  
    plt.savefig('tree.svg',format='svg',bbox_inches = "tight")
    

modello()
