"""
    Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada,
     más el 5% del valor de esas ventas. Realizar un programa que imprima el número del vendedor
    y  el salario que le corresponde en un determinado mes. Se leen por teclado el número del vendedor,
    la cantidad de ventas que realizó y el valor total de las mismas.
"""
salario = 40
comision = 20

print("Ingresar el número del vendedor:")
vendedor = int(input())

print( "El vendedor:",vendedor)

print("El salario base de", vendedor ,"es de:","$", salario)

print("Ingresar la cantidad de ventas:")
ventas = int(input()) 

print("La cantidad de ventas del mes:", ventas)
incremento = int( (ventas * comision + salario ))

print("Comisión por ventas es de:", "$",incremento)

print("Ingresar el monto total de las ventas:")
monto = int(input())

print("El monto de ventas es de:", monto)
gxventas = int((monto * 5 )/ 100)

print("La ganancia por el total de ventas es de:", gxventas)
total = (incremento + gxventas)

print("La ganancia del mes es de:", "$", total)
print("Felicitaciones por este gran mes", vendedor)