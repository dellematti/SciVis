import matplotlib.pyplot as plt

data = {'12':2 , '11':2 ,'10':4,'9':1, '8':8, '7':14, '6':23, '5':24, '4':68,'3':123,'2':212,'1':191}
courses = list(data.keys())
values = list(data.values())

plt.barh(courses, values,  color ='blue')
plt.ylabel("numero tentativi")
plt.xlabel("numero di studenti")
plt.title("Numero di tentativi per studente prima di passare")

plt.show()




# Output dello script di numero tentativi per studente
# Passato al tentativo n.  1  :    191
# Passato al tentativo n.  2  :    212
# Passato al tentativo n.  3  :    123
# Passato al tentativo n.  4  :    68
# Passato al tentativo n.  5  :    24
# Passato al tentativo n.  6  :    23
# Passato al tentativo n.  7  :    14
# Passato al tentativo n.  8  :    8
# Passato al tentativo n.  9  :    1
# Passato al tentativo n.  10  :   4
# Passato al tentativo n.  11  :   2
# Passato al tentativo n.  12  :   2
# media: 2.64