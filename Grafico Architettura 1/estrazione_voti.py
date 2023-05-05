from pdfminer.high_level import extract_pages, extract_text


text = extract_text("Risultati 10-11.pdf")
#print(text)

str_new = text.split("\n")

'''
for i in str_new:
    print(i)
'''

stringa_voti = ""

#Per avere tutti i voti delle 3 colonne:
for i in str_new:
    if i.isnumeric() or i == "Insuff" or i == "R" or i == "RP" or i.__contains__('R') or i.__contains__("RP") or i.__contains__(',') or i.__contains__("Insuff"):
        #print(i)
        stringa_voti += i
        stringa_voti += '-'

vettore_voti = stringa_voti.split('-')
vettore_voti.remove('')
#print(vettore_voti)

stringa_voti_da_splittare = ""

for i in vettore_voti:
    if len(i) == 1 or len(i) == 2 or i == "Insuff" or i == "R" or i == "RP" or i.__contains__('R') and len(i) == 1 or len(i) == 2 or len(i) == 4 or i.__contains__("RP") or i.__contains__(',') or i.__contains__("Insuff"):
        stringa_voti_da_splittare += i
        stringa_voti_da_splittare += '-'

vettore_voti_finale = stringa_voti_da_splittare.split('-')
vettore_voti_finale.remove('')

'''
for i in vettore_voti_finale:
    print(i)
'''

#Per avere il numero totali di studenti che hanno partecipato alle prove in itinere, partendo dalla variabile str_new:

conta = 0 #variabile intera che contiene il numero totali di iscritti all'esame

for i in str_new:
    if i.isnumeric() and len(i) > 2 or i.__contains__('R') and len(i) > 5:
        #print(i)
        conta += 1

conta += 1 #Perché c'è un ritirato senza numero di matricola
#print(conta)

#I seguenti dati sono estratti a partire dalla variabile vettore_voti_finale
#Per avere il numero di persone insufficienti:
contaInsuff = 0
for i in vettore_voti_finale:
    if i == "Insuff" or i.__contains__("Insuff"):
        contaInsuff += 1

print("Studenti insufficienti:", contaInsuff)

#Per avere il numero di persone ritirate:
#Per il numero esatto è necessario scorrere vettore_voti
contaRitirati = 0
for i in vettore_voti:
    if i == 'R' or i.__contains__('R'):
        contaRitirati += 1

#La R viene ripetuta 2 volte quindi è necessario dividere per 2 la quantità trovata:
contaRitirati /= 2
contaRitirati = int(contaRitirati)
print("Studenti ritirati:", contaRitirati)

#Per avere il numero di persone dal 18 al 20:
conta1 = 0
for i in vettore_voti_finale:
    if i.__contains__("17") or i.__contains__("18") or i.__contains__("19") or i.__contains__("20"):
        conta1 += 1

print("Studenti che hanno avuto un voto da 18 a 20:", conta1)

#Per avere il numero di persone dal 21 al 24:
conta2 = 0
for i in vettore_voti_finale:
    if i.__contains__("21") or i.__contains__("22") or i.__contains__("23") or i.__contains__("24"):
        conta2 += 1

print("Studenti che hanno avuto un voto da 21 a 24:", conta2)

#Per avere il numero di persone dal 25 al 27:
conta3 = 0
for i in vettore_voti_finale:
    if i.__contains__("25") or i.__contains__("26") or i.__contains__("27"):
        conta3 += 1

print("Studenti che hanno avuto un voto da 25 a 27:", conta3)

#Per avere il numero di persone dal 28 al 30:
conta4 = 0
for i in vettore_voti_finale:
    if i.__contains__("28") or i.__contains__("29") or i.__contains__("30"):
        conta4 += 1

print("Studenti che hanno avuto un voto da 28 a 30:", conta4)

#Per avere il numero di persone con 30L:
conta5 = 0
for i in vettore_voti_finale:
    if i.__contains__("31") or i.__contains__("32"):
        conta5 += 1

print("Studenti che hanno avuto 30L:", conta5)

#Studenti promossi:
contaPromossi = conta1 + conta2 + conta3 + conta4 + conta5
print("Studenti che hanno passato l'esame:", contaPromossi)

#Scrittura su file dei dati trovati:
str_finale = ""
str_finale = str(contaInsuff) + ' ' + str(contaRitirati) + ' ' + str(contaPromossi) + ' ' + str(conta1) + ' ' + str(conta2) + ' ' + str(conta3) + ' ' + str(conta4) + ' ' + str(conta5)

with open("dati1.txt", "w") as file:
    file.write(str_finale)