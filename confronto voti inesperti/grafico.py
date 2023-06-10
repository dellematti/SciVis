import csv
import matplotlib.pyplot as plt

def leggi_csv(file_csv):
    dati = []
    with open(file_csv) as fileInput:
        csv_reader = csv.reader(fileInput)
        for i in csv_reader:
            dati.append(i)
    
    return dati

def put_dati(dati):
    conta = 0
    list_dati = []
    for i in dati:
        if conta != 0:
            #print(i)
            list_dati.append(i)
        conta += 1
    
    return list_dati

file_name = 'Sondaggio sul corso di Programmazione 1 (Risposte) - Risposte del modulo 1 (2).csv'

dati = leggi_csv(file_name)
list_dati = put_dati(dati)

#print(list_dati)

conta_passati = 0
conta_bocciati = 0
conta_esperti = 0
conta_inesperti = 0
it = 0

for i in range(len(list_dati)):
    for j in list_dati[i]:
        if 'S' in j and it == 0:
            #print(j)
            conta_passati += 1
            it += 1
        elif 'N' in j and it == 0:
            conta_bocciati += 1
            it += 1
        elif it == 1 and 'S'in j:
            conta_esperti += 1
            it = 0
        elif it == 1 and 'N' in j:
            conta_inesperti += 1
            it = 0

'''
print('Passati:', conta_passati)
print('Bocciati', conta_bocciati)
print('Esperti:', conta_esperti)
print('Inesperti:', conta_inesperti)
'''

conta_voto_alto = 0
flag1 = False
flag2 = False

it = 0

for i in range(len(list_dati)):
    for j in list_dati[i]:
        if 'S' in j and it == 0:
            #print(it)
            flag1 = True
            it += 1
        elif 'S' in j and flag1 and it == 1:
            flag2 = True
            it += 1
        elif 'L' in j and flag2 and it == 2:
            conta_voto_alto += 1
        else:
            flag1 = False
    it = 0

#print('Voti alti:', conta_voto_alto)

conta_alto_generico = 0

for i in range(len(list_dati)):
    for j in list_dati[i]:
        if 'L' in j:
            conta_alto_generico += 1

#print('Tutti i voti alti:', conta_alto_generico)

voto_alto_inesperti = conta_alto_generico - conta_voto_alto

it = 0
flag1 = False
flag2 = False
conta_voto_semi_alto = 0
conta_voto_mezzano = 0

for i in range(len(list_dati)):
    for j in list_dati[i]:
        if 'S' in j and it == 0:
            #print(it)
            flag1 = True
            it += 1
        elif 'N' in j and flag1 and it == 1:
            flag2 = True
            it += 1
        elif '27' in j and flag2 and it == 2:
            conta_voto_semi_alto += 1
            it = 0
        elif '18' in j and flag2 and it == 2:
            conta_voto_mezzano += 1
            it = 0
        else:
            flag1 = False
            it = 0

print('Voti alti inesperti:', voto_alto_inesperti)
print('Voti semi-alti inesperti:', conta_voto_semi_alto)
print('Voti mezzani inesperti:', conta_voto_mezzano)


#Creazione del grafico a partire dai dati raccolti:
labels = ['Inesperti con voti alti', 'Inesperti con voti medi', 'Inesperti con voti bassi']
sizes = [voto_alto_inesperti, conta_voto_semi_alto, conta_voto_mezzano]

colors = ['#ff7f0e', '#2ca02c', '#d62728']

explode = (0, 0, 0)

plt.pie(sizes, explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Confronto fra voti alti tra esperti e inesperti della programmazione')

plt.show()
