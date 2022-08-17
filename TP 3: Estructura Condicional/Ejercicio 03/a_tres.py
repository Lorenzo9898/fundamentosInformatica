""" 
Crear un programa que pida un número de mes (ejemplo 4) 
y escriba el nombre del mes en letras ("abril").
Verificar que el mes sea válido e informar en caso que no lo sea.
"""

mes = int(input("Ingresar el numero de mes: "))

if mes == 1:
    print("Enero")
if mes == 2:
    print("Febrero")
if mes == 3:
    print("Marzo")
if mes == 4:
    print("Abril")
if mes == 5:
    print("Mayo")
if mes == 6:
    print("Junio")
if mes == 7:
    print("Julio")
if mes == 8:
    print("Agosto")
if mes == 9:
    print("Septiembre")
if mes == 10:
    print("Octubre")
if mes == 11:
    print("Nomviembre")
if mes == 12:
    print("Diciembre")
if mes >= 13: 
    print("El numero no corresponde a un mes")
    