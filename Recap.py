# variables
from ast import Div
from email.mime import multipart


var1 = 10 # int
var2 = 4.2 # float
var3 ="bonjour" # string
var4 = True # boolean
var5 =["Bonjour", 5, 3.5] #list

print("total est egal a :")
total = var1 + var2
print(total)

# conditions 
if var1 > var2:
    print("c'est plus grand")
elif var1 < var2:
    print("c'est plus petit")
else:
    print("c'est egal")

# boucles
while var1 > var2:
    print(var1)
    var1 = var1 - 1

for element in var5:
    print(element)

print("---------------------")
# fonctions
def add(a, b):
    resultat = a + b
    return resultat

#fonction div, multi, soust


total = add(var1,var2)
print (total)
def div(a, b):
    resultat = a / b
    return resultat


total = Div(var1,var2)
print(total)

def multip(a, b):
    resultat = a * b
    return resultat

total = multip(var1,var2)
print(total)

def soust(a, b):
    resultat = a - b
    return resultat

total = soust(var1,var2)
print(total)

