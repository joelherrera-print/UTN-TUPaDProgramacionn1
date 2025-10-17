##actividad1
print("hola mundo!") 

##actividad2
nombre= input("como te llamas?") 
print(f"hola"+ nombre +",mucho gusto" )

##actividad3

nombre= input("ingresa tu nombre:") 
apellido= input("ingresa tu apellido:")
edad= input("ingresa tu edad:")
residencia= input("ingresa tu lugar de residencia:")

print(f"soy, {nombre}{apellido}, tengo {edad} años y vivo en {residencia}.")

##actividad4

radio= float(input("ingresa el radio del circulo:")) 
area= 3.14159 * (radio ** 2)
perimetro= 2 * 3.14159 * radio

print(f"el area del circulo es:{area:}") 
print(f"el perimetro del circulo es:{perimetro:}")

##actividad5

segundos= int(input("ingresa la cantidad de segundos:")) 
horas= segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f}horas")

##actividad6

numero= int(input("ingresa un numero para ver su tabla de multiplicar:")) 
for x in range(11):
        print(f"8 * {x} = {8*x}")
##actividad7

def operaciones_basicas(a,b):
        suma = a + b
        resta = a - b
        multiplicacion = a * b 
        division = a / b

        return (suma,resta,multiplicacion,division)
a = int(input("ingrese un numero entero"))
b = int(input("ingrese un numero entero"))
resultados = operaciones_basicas(a,b)
print("suma: resultado [0]")
print("resta: resultado [1]")
print("multiplicacion: resultado [2]")
print("division: resultado [3]")

##actividad8

def calcular_imc(peso,altura):
        imc = peso / altura*altura
        return imc
peso = float(input("ingrese el peso en kilogramos"))
altura = float(input("ingrese la altura en metros"))

if peso <= 0 or altura <= 0 :
        print("el peso y la altura tienen que ser numeros positivos")
else: 
        resultado = calcular_imc(peso,altura)
        print(f"su imc es de: {resultado:.2f}") 

##actividad9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {resultado:.2f}°F")

##actividad10

def calcular_promedio(a,b,c):
       return(a+b+c) / 3
a = float(input("ingresa el primer numero:"))
b = float(input("ingresa el segundo numero:"))
c = float(input("ingresa el tercer valor:"))

promedio = calcular_promedio(a,b,c)
print("el promedio es:", round(promedio, 2))


 








