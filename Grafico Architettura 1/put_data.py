def somma(el1, el2, el3, el4, el5):
    return el1 + el2 + el3 + el4 + el5

with open("dati1.txt") as file:
    str1 = file.readline()

with open("dati2.txt") as file:
    str2 = file.readline()

with open("dati3.txt") as file:
    str3 = file.readline()

with open("dati4.txt") as file:
    str4 = file.readline()

with open("dati5.txt") as file:
    str5 = file.readline()

str_new1 = str1.split(' ')
data_list1 = []
str_new2 = str2.split(' ')
data_list2 = []
str_new3 = str3.split(' ')
data_list3 = []
str_new4 = str4.split(' ')
data_list4 = []
str_new5 = str5.split(' ')
data_list5 = []

for i in str_new1:
    data_list1.append(int(i))

for i in str_new2:
    data_list2.append(int(i))

for i in str_new3:
    data_list3.append(int(i))

for i in str_new4:
    data_list4.append(int(i))

for i in str_new5:
    data_list5.append(int(i))

'''
print(data_list1)
print(data_list2)
print(data_list3)
print(data_list4)
print(data_list5)
'''

final_list = []
final_list.append(somma(data_list1[0], data_list2[0], data_list3[0], data_list4[0], data_list5[0]))
final_list.append(somma(data_list1[1], data_list2[1], data_list3[1], data_list4[1], data_list5[1]))
final_list.append(somma(data_list1[2], data_list2[2], data_list3[2], data_list4[2], data_list5[2]))
final_list.append(somma(data_list1[3], data_list2[3], data_list3[3], data_list4[3], data_list5[3]))
final_list.append(somma(data_list1[4], data_list2[4], data_list3[4], data_list4[4], data_list5[4]))
final_list.append(somma(data_list1[5], data_list2[5], data_list3[5], data_list4[5], data_list5[5]))
final_list.append(somma(data_list1[6], data_list2[6], data_list3[6], data_list4[6], data_list5[6]))

#print(final_list)

str_finale = str(final_list[0]) + ' ' + str(final_list[1]) + ' ' + str(final_list[2]) + ' ' + str(final_list[3]) + ' ' + str(final_list[4]) + ' ' + str(final_list[5]) + ' ' + str(final_list[6])
with open("dati.txt", "w") as file:
    file.write(str_finale)