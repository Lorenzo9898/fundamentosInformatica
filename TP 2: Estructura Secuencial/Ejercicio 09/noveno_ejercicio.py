"""
Leer un período en segundos e imprimirlo expresado en:
días, 
horas, 
minutos 
y segundos.
Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.
"""

seg = int(input("Ingrese la cantidad de segundo a convertir: "))

if seg >= 86400:
    time = int(seg * (1 / 3600) * (1 / 24))
    print("La cantidad de dias es:",time)
    seg = seg % 86400

if seg >= 3600:
    time = int(seg * (1 / 60 ) * (1 / 60))
    print("La cantidad de horas es:",time)
    seg = seg % 3600

if seg >= 60:
    time = int(seg * (1 / 60 ))
    print("La cantidad de minutos es:",time)
    seg = seg % 60

if seg >= 1:
    time = int(seg * (1 / 1))
    print("La cantidad de segundos es:",time)
    seg = seg % 1
 