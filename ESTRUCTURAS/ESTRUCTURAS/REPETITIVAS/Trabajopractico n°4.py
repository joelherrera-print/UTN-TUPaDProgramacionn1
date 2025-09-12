#Actividad1

for numero in range(101):
    print(numero)

#Actividad2

numero = (input("Ingrese un numero entero: "))
cantidad_digitos = len(numero)

print("El número tiene", cantidad_digitos, "dígitos.")

#Actividad3

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))
total = 0

for i in range(numero1, numero2):
    if (i> numero1):
        total = total +i

print(total)

#Actividad4

numero = int(input("Ingrese un numero entero: "))
total = numero

while (numero!=0):
    numero = int(input("Ingrese otro numero entero: "))
    total = total + numero

print (f"El total es: {total}")

#Actividad5

import random

numero_random = random.randint(0, 9)
intentos = 0
adivinanza = -1

while adivinanza != numero_random:
    adivinanza = int(input("Ingresa un número: "))
    intentos += 1

print(f"El numero era: {numero_random}.Lo adivinaste en {intentos} intentos.")

#Actividad6

for numero in range(100,-1,-2):
    print(numero)

#Actividad7

numero = int(input("Ingresa un número entero positivo: "))
suma = 0

for i in range(numero + 1):
    suma += i

print(f"La suma de los números entre 0 y {numero} es: {suma}")


#Actividad8
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range (9):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\nResultados:")
print("Cantidad de pares:", par)
print("Cantidad de impares:", impar)
print("Cantidad de positivos:", positivo)
print("Cantidad de negativos:", negativo)

#Actividad9
suma = 0
for i in range(99):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero
media = suma / 100
print("\nLa media de los números ingresados es:", media)

#Actividad10

numero = int(input("Ingrese un número: "))
invertido = 0
while numero > 0:
    digito = numero % 10       
    invertido = invertido * 10 + digito
    numero = numero // 10       
print("Número invertido:", invertido)