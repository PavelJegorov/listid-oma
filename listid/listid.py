#6
#from random import *
#from string import *

#nimekirja1=[]
#nimekirja=[]
#n=int(input("Nimekirja suurus: "))
#for i in range(n):
#    arv=randint(10,100)
#    nimekirja1.append(arv)
#    nimekirja.append(arv)
#maksimum=nimekirja[0]
#for arv in nimekirja:
#    if arv>maksimum:
#        maksimum=arv
#vajavarv=maksimum/len(nimekirja)
#for i in range(len(nimekirja)):
#    if nimekirja[i]==maksimum:
#        nimekirja[i]=vajavarv
#print(nimekirja1)
#print(nimekirja)
 

#9
#name = input("Sisestage oma nimi")
#if name.isalpha():
#    print("Tere {}!".format(name.capitalize()))
#    letter_count = len(name)
#    print("tähtede arv nimes:", letter_count)
#else:
#    print("nimi peab sisaldama ainult tähti")




#12 
#import random

#numbers = [random.randint(1, 100) for _ in range(10)]
#print("nimekirja:", numbers)

#min_index = numbers.index(min(numbers))
#max_index = numbers.index(max(numbers))
#numbers[min_index], numbers[max_index] 
#numbers[max_index], numbers[min_index]

#print("loend pärast min ja max väärtuste muutmist:", numbers)


#15
# Lihtsa sõnaraamatu järjendid
#arvud = [1, 2, 3, 4,]
#eesti = ["üks", "kaks", "kolm", "neli"]
#inglise = ["one", "two", "three", "four"]
#itaalia = ["uno", "due", "tre", "quattro"]

## Väljastamine tabelina
#print("Arv - Eesti - Inglise - Itaalia")
#for i in range(len(arvud)):
#    print(f"{arvud[i]} - {eesti[i]} - {inglise[i]} - {itaalia[i]}")

## Väljastame kõikide järjendite elemendid tähestikulises järjekorras kasvavalt
#print("\nKõikide järjendite elemendid tähestikulises järjekorras:")
#print("Arvud:", sorted(arvud))
#print("Eesti sõnad:", sorted(eesti))
#print("Inglise sõnad:", sorted(inglise))
#print("Itaalia sõnad:", sorted(itaalia))



#18

import random 

print("Tere tulemast mängule 21, kui näitad vähem või rohkem kui 21")
koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4 #список повторяется 4 раза 
random.shuffle(koloda) #перемешивать колоду
arv = 0 #начальное число

while arv != 21: #если число НЕ равно
    while True:
        choice = input("Kas võtad kaardi? jah/ei: ")
        if choice == "jah":
            number = koloda.pop() #убирает и возравщает последнее значение из списка
            print("Sul on kaardi number %d" % number) #выбирается случайная карта из колоды 
            arv += number 
            if arv > 21: 
                print("Vabandust, aga sa kaotasid.")
                break 
            elif arv == 21: 
                print("Palju õnne, tabasite numbrit 21!")
                break 
            else:
                print("Teil on %d punkti." % arv) # показывает какое число выпало 
        elif choice == "ei": #если выбор нет
            print("Teil on %d punkti ja olete mängu lõpetanud." % arv) #конечное число игра окончена
            break  # Завершаем игру
        else:
            print("Vigane valik. Palun sisestage 'jah' või 'ei'.") # чтобы сделать правильный выбор
    break  # Завершаем

