#Actividad 1
palabra = input("Ingrese una palabra: ")
for i in range(9):
    print(palabra)

#Actividad 2
edad = int(input("Ingrese su edad: "))
for i in range(edad):
    print(i+1)

#Actividad 3
numero = int(input("Ingrese un numero: "))
for i in range(1,numero+1):
    print("*"*i)

#Actividad 4
for i in range(11):
    print(f"10 * {i} = {i*10}")

#Actividad 5
contraseña = input("Ingrese su contraseña para guardarla: ")
contraseña1 = input("Ingrese su contraseña: ")
while(contraseña!=contraseña1):
    contraseña1 = input("Ingreso mal su contraseña. Intente de vuelta: ")
print("Ingreso bien la contraseña")

#Actividad 6
palabra = input("Ingrese un palabra: ")
salir = "salir"
while (palabra!=salir):
    print(palabra)
    palabra = input("Ingrese otra palabra: ")

#Actividad 7
for i in range(2,21):
    print(i)

#Actividad 8
for i in range(1,101):
    if i % 3==0 and i % 5==0:
        print("FizzBuzz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Buzz")
    else:
        print(i)

#Actividad 9
suma = 0
for i in range(9):
    numero = input("Cargue un numero: ")
    if i==5:
        suma = suma+i
print(f"La suma de los ultimos 5 numeros son: {suma}")

#Actividad 10
cantidad_triangulos = int(input("Ingrese la cantidad de triangulos: "))
for i in range (cantidad_triangulos):
    lado1 = int(input("Ingrese el primer lado: "))
    lado2 = int(input("Ingrese el segundo lado: "))
    lado3 = int(input("Ingrese el tercer lado: "))
    if lado1 == lado2 and lado2 == lado3:
        print(f"El triangulo N° {i+1} es equilatero")
    elif lado1==lado2 or lado1 == lado3 or lado2 == lado3:
        print(f"El triangulo N° {i+1} es equilatero")
    else:
        print(f"El triangulo N° {i+1} es escaleno")
