"Hay que hacer un programa que "

from cmd import PROMPT
import math
import sys 

while True:
    lenguaje_1 = int((input("> ¿Cual es el lenguaje que vas a introducir, introduce el número correspondiente? ((1)dec, (2)bin, (3)octa,(4)hex)\n> ")))
    lenguaje_2 = int((input("> ¿A que lenguaje quieres traducir, introduce el número correspondiente? ((1)dec, (2)bin, (3)octa, (4)hex)\n> ")))

    if lenguaje_1>0 and lenguaje_1 < 5 and lenguaje_2 > 0 and lenguaje_2 < 5:
        break
    else:
        print("No ha introducido un valor valido")

n_decimal,n_entero = (math.modf(float(input(">¿Qué numero quieres traducir?\n> "))))


n_decimal = round(n_decimal,5)


"Entonces una vez se haya elegido los lenguajes, utilizamos sentencias de if anidadas para mostrar "
if lenguaje_1 == "bin" :
    print("El lenguaje con el que vas a introducir el lenguaje es binario")
    if lenguaje_2 == "dec":
        print("El lenguaje resultante va a ser decimal")
        


        


