from time import time

input("Lancement des 5 battements : appuyer sur entrée 6 fois, espacés de une seconde à chaque fois...")
tDebut = time()
for i in range(5):
    debut = time()
    input(str(i+1) + "/5 appuyer sur entrée dans (exactement) 1 seconde")
    fin = time()
    print(i+1 , "/5 ", fin - debut, "s")
tFin = time()
print("Temps de réaction moyen :", (tFin - tDebut)/5)

print("BPM effectif : " , 5*60/(tFin - tDebut))








