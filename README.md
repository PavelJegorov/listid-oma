#6
from random import *
from string import *

nimekirja1=[]
nimekirja=[]
n=int(input("Nimekirja suurus: "))
for i in range(n):
    arv=randint(10,100)
    nimekirja1.append(arv)
    nimekirja.append(arv)
maksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
vajavarv=maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=vajavarv
print(nimekirja1)
print(nimekirja)
