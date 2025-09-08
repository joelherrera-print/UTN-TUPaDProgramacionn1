# actividad 1
print("Hola Mundo!")

# actividad 2
nombre = input("Cual es tu nombre?")
print (f"Hola {nombre} !")

#Activiadad 3
nombre= input("Cual es tu nombre? ")
apellido= input("Cual es tu apellido? " )
edad = int(input("Cual es tu edad?"))
pais= input ("Cual es su pais de residencia? " )

print (f"Soy {nombre} {apellido},tengo {edad} años y vivo en {pais}.")

#Actividad 4
radio = float(input("Ingrese el radio del circulo: "))
area = 3,14 * radio * radio
perimetro = 2 * 3,14 * radio

print (f"El area del circulo es: {area}")
print (f"El perimetro del circulo es: {perimetro}")

#Actividad 5
segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = segundos/60
horas = minutos/60

print (f"Equivale a {horas} horas")

#Actividad 6

num = int(input("Ingrese un numero: "))
print(f"""
         {num} x 0 ={num * 0}
         {num} x 1 ={num * 1}
         {num} x 2 ={num * 2}
         {num} x 3 ={num * 3}
         {num} x 4 ={num * 4}
         {num} x 5 ={num * 5}
         {num} x 6 ={num * 6}
         {num} x 7 ={num * 7}
         {num} x 8 ={num * 8}
         {num} x 9 ={num * 9}
         {num} x 10 ={num * 10} 
        """)

#activdad 7

num1 = int (input("Ingrese el primer numero: "))
num2 = int (input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
divicion = num1 / num2
multiplicacion = num1 * num2

print(f"la suma es:{suma} ")
print(f"la resta es:{resta} ")
print(f"la divicion es:{divicion}")
print(f"la multiplicacion es: {multiplicacion}")

#actividad 8 

altura= float(input("Cual es tu altura? "))
peso= float (input("Cual es su peso? (ingresar en kilogramo)"))
masa_corporal= peso / (altura**2)

print(f"Su masa corporal es {masa_corporal} ")

#Actividad 9

grados_C = float(input ("Ingrese la temperatura en grados Celsius: "))
grados_F = 9/5 * grados_C + 32 

print (f"El equivalente en grados Fahrenheit es: {grados_F}")

#Actividad 10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) /3

print(f"El promedio total es: {promedio}")