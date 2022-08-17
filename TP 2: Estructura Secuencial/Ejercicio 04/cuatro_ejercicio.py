print("Nombre de la empresa:")

empresa = input()

print("Bievenido al espacio de inversión de", empresa)

print("Ingrese su nombre: ")

nombre_uno = input()

print ( nombre_uno,"ingrese cuánto desea invertir en", empresa)
i_uno = int(input())


print("Ingrese su nombre:")
nombre_dos = input()

print (nombre_dos,"ingrese cuánto desea invertir en", empresa)
i_dos = int(input())

print("Ingrese su nombre:")
nombre_tres = input()

print (nombre_tres,"ingrese cuánto desea invertir en", empresa)
i_tres = int(input())

total = (i_uno + i_dos + i_tres)

print(" El total de la inversión que han realizado en", empresa, "es de: $",total)

print(" El porcentaje de inversión de", nombre_uno, "es de un:", int((i_uno / total)* 100), "%") 
print(" El porcentaje de inversión de", nombre_dos, "es de un:", int((i_dos / total)* 100), "%")
print(" El porcentaje de inversión de", nombre_tres, int((i_tres / total)* 100), "%")  

print("Muchas gracias por confiar en", empresa) 