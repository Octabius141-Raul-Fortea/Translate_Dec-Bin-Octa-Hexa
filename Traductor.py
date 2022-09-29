"Hay que hacer un programa que traduzca"


from fileinput import close
import math
import sys
from this import d
from tkinter import N 


array_números = ["1","2","3","4"]
lenguaje_1_asignado = False
lenguaje_2_asignado = False


while True:
    lenguaje_1 = (input("> ¿Cual es el lenguaje que vas a introducir, introduce el número correspondiente?\n    (1)dec, (2)bin, (3)octa,(4)hex\n> "))
    lenguaje_2 = (input("> ¿A que lenguaje quieres traducir, introduce el número correspondiente? \n     (1)dec, (2)bin, (3)octa, (4)hex\n> "))

    for x in range (len(array_números)-1):
        if lenguaje_1 == array_números[x]:
            lenguaje_1_asignado = True
        if lenguaje_2 == array_números[x]:
            lenguaje_2_asignado = True
        if lenguaje_1_asignado == True and lenguaje_2_asignado == True:
            break
    if lenguaje_1_asignado == True and lenguaje_2_asignado ==  True:
        break
    else:
        print("""
                > Has introducido valores erroneos, introduce de nuevo los valores

    =============================================================================================
        
        """)

n_decimal,n_entero = (math.modf(float(input(">¿Qué numero quieres traducir?\n> "))))
n_decimal = round(n_decimal,5)

      

def decimal_binario (decimal,fraccionario):
    binario = ""
    binario_fraccionario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    while fraccionario != 0 :
        fraccionario_nuevo, entero_nuevo  = (math.modf( fraccionario * 2))
        fraccionario_nuevo = round(fraccionario_nuevo,3)
        binario_fraccionario =  binario_fraccionario + str(entero_nuevo)
        fraccionario = (fraccionario_nuevo)
    return (binario + str(decimal) + "." + binario_fraccionario)

print (decimal_binario(123,0.5))
"Entonces una vez se haya elegido los lenguajes, utilizamos sentencias de if anidadas para mostrar "
if lenguaje_1 == "1":
    print("El lenguaje con el que vas a introducir el mensaje es decimal")
    if lenguaje_2 == "2":
        print("El lenguaje resultante va a ser binario")
        print(decimal_binario(n_entero, n_decimal))
if lenguaje_1 == "2" :
    print("El lenguaje con el que vas a introducir el mensaje es binario")
    if lenguaje_2 == "1":
        print("El lenguaje resultante va a ser decimal")
        n_ent_separado = [int(a) for a  in str(n_entero)]
        n_dec_separado = [int(a) for a in str(n_decimal)]




