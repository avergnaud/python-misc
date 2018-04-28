# "à la main"
n = 100
print(n)

ma_liste_de_nombre_premiers = [2,3,5,7,11,13,17]
print(ma_liste_de_nombre_premiers)

# on décompose "à la main" :
# https://fr.wikipedia.org/wiki/D%C3%A9composition_en_produit_de_facteurs_premiers
#
# ITERATIONS AVEC LE PREMIER ELEMENT DE ma_liste_de_nombre_premiers : 2
# 100/2 = 50
# 50 est un nombre entier, autrement dit : "100 est divisible par 2 (au sens de la division entière)"
# autrement dit : le reste de la division euclidienne de 100 par 2 est 0
# donc je conserve 2 dans ma liste de facteurs
# liste de facteurs : [2]
# 50/2 = 25
# 25 est un nombre entier, autrement dit : "50 est divisible par 2 (au sens de la division entière)"
# autrement dit : le reste de la division euclidienne de 50 par 2 est 0
# donc je conserve 2 dans ma liste de facteurs
# liste de facteurs : [2,2]
# 25/2 = 12.5
# 12.5 n'est pas entier, autrement dit : "25 n'est pas divisible par 2 (au sens de la division entière)"
# le reste de la division euclidienne de 25 par 2 est 1 (25 = 2*12 + 1)
# donc je ne rajoute pas 2 à la liste de facteurs
# liste de facteurs : [2,2]
# 
# ITERATIONS AVEC LE DEUXIEME ELEMENT DE ma_liste_de_nombre_premiers : 3
# 25/3 = pas un entier
# liste de facteurs : [2,2]
# 
# ITERATIONS AVEC LE TROISIEME ELEMENT DE ma_liste_de_nombre_premiers : 5
# 25/5 = 5
# liste de facteurs : [2,2,5]
# 5/5 = 1
# liste de facteurs : [2,2,5,5]
#
# RESULTAT, décomposition en produit de facteurs premiers du nombre 100 :
# 100 = 2*2*5*5