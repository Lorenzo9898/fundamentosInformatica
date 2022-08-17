"""
Un banco necesita para sus cajeros de la sucursal un programa que
 lea una cantidad de dinero que desea retirar el cliente
 e imprima a cuántos billetes equivale, 
considerando que existen billetes de $1000, $500, $200, $100, $50, $20 y el resto en monedas de $10, $5, $2 y $1. 
Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
"""

dinero = int(input("Ingrese monto a retirar: "))


if dinero >= 1000:
    sobrante = dinero // 1000
    print("Existen " + str(sobrante) + " billetes de mil pesos ARG")
    dinero = dinero % 1000

if dinero >= 500:
    sobrante = dinero // 500
    print("Existen " + str(sobrante) + " billetes de quinientos pesos ARG")
    dinero = dinero % 500

if dinero >= 200:
    sobrante = dinero // 200
    print("Existen " + str(sobrante) + " billetes de doscientos pesos ARG")
    dinero = dinero % 200

if dinero >= 100:
    sobrante = dinero // 100
    print("Existen " + str(sobrante) + " billetes de cien pesos ARG")
    dinero = dinero % 100

if dinero >= 50:
    sobrante = dinero // 50
    print("Existen " + str(sobrante) + " billetes de cincuenta pesos ARG")
    dinero = dinero % 50

if dinero >= 20:
    sobrante = dinero // 20
    print("Existen " + str(sobrante) + " billetes de veinte pesos ARG")
    dinero = dinero % 20

if dinero >= 10:
    sobrante = dinero // 10
    print("Existen " + str(sobrante) + " monedas de diez pesos ARG")
    dinero = dinero % 10

if dinero >= 5:
    sobrante = dinero // 5
    print("Existen " + str(sobrante) + " monedas de cinco pesos ARG")
    dinero = dinero % 5

if dinero >= 2:
    sobrante = dinero // 2
    print("Existen " + str(sobrante) + " monedas de dos pesos ARG")
    dinero = dinero % 2

if dinero >= 1:
    sobrante = dinero // 1
    print("Existen " + str(sobrante) + " monedas de un pesos ARG")
    dinero = dinero % 1





