#Pas de bug ici, mais quelle est la valeur affichée
a = 2
b = a * a
a = a + 1
b = a * b
b = b + a
print(b)