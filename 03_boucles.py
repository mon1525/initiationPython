# while : "tant que" la condition est vrai, tu fais...
# for : "pour chaque" element dans une liste, tu fais...

# Exemple 1 --------------------------------------------
fin = 10
debut = 1

while debut < fin:
    print("mon compteur = ",debut)
    debut = debut +1 # est quivalent a : debut +=1 

# Exemple 2 --------------------------------------------
texte = "coucou"

for lettre in texte :
    print(lettre)

# Exemple 3 --------------------------------------------

texte = "Bonjour"
nbVoyelles = 0
nbConsonnes = 0

for lettre in texte :
    if lettre in "aeiouy" :
        nbVoyelles +=1
    else :
        nbConsonnes +=1

print("j'ai", nbVoyelles, "voyelles dans", texte)