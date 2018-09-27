# type() permet de connaitre le type d'une variable
# print() permet d'afficher quelque chose dans un terminal

print("hello world")
print( type("5") )

nombreEntier = 5
nombreVirgule = 5.6
texte = "yolooo !"
boolean = True
liste = ["1er element", "2eme element"]

print(type(nombreEntier)) #entier : int pour integer
print(type(nombreVirgule)) #virgule : float
print(type(texte)) # texte : str pour string
print(type(boolean)) # boolean : bool
print(type(liste)) # liste : list

print(liste[0]) # affiche le 1er element
print(liste[1]) # affiche le 2eme element


# les différents opérateurs arithmetique
# * multiplication
# / division
# // division entière
# - soustraction
# + addition
# % modulo
# ** exposant


print (5*3)
result = nombreEntier * nombreVirgule
print(result)

print(10%3)

print(5**2)

# pour modifier le type d'une variable, on utilise le cast
variable = "5"
print(type(variable)) # ici, c'est un str

variable = int(variable) # on change son type en int

print(type(variable))

variable = float(variable) # on change son type en float

print(type(variable))

variable = str(variable) # on rechange son type en str

print(type(variable))



