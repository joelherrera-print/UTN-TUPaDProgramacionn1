##ACTIVIDAD1
contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña: ").lower()
if contrasena_usuario == contrasena_correcta:
 print("Contraseña correcta. Bienvenido.")
else:
 print("Contraseña incorrecta. Intenta de nuevo.")

##ACTIVIDAD2
letra=input("introduce una letra:").lower()
vocales="a","e","i","o","u"

if len(letra)== 1 and letra in vocales:
 print("La letra ingresada es vocal!")
else:
 print("La letra ingresada no es vocal!") 

 ##ACTIVIDAD 3
num=float(input("Ingrese un numero:"))
if num > 0:
  print("El numero en positivo")
elif num < 0:
   print("El numero es negativo")
else:
   print("El numero es cero")
##ACTIVIDAD 4

num1=float(input("Ingrese un numero:"))
num2=float(input("Ingrese un numero:"))

if num1 > num2:
  print("El primer numero ingresado es mayor")
elif num1 < num2:
  print("El primer numero ingresado es menor")
else:
  print("Los números ingresados son iguales")

##ACTIVIDAD 5

temperatura=float(input("Introduce la temperatura actualmente en celcius:"))

if temperatura <= 10:
  print("Hace frio!")
elif 10 < temperatura <= 25:
  print("Esta templado!")
else:
  print("Hace calor!")

##ACTIVIDAD 6
Anio= int(input("Introduce un año: "))
if anio <= 0:
        print("Error: Ingresa un año positivo")
elif (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
 print("Se ingresó un año bisiesto")
else:
 print("Se ingresó un año no bisiesto")

#ACTIVIDAD 7
frase = input("Introduce una frase o palabra: ").rstrip()
if not frase.endswith('.'):
    frase += '.'
print(frase)
#ACTIVIDAD 8
contrasena = input("Crea una contraseña: ")
es_segura = (8 <= len(contrasena) <= 20 and
             any(c.isupper() for c in contrasena) and
             any(c.isdigit() for c in contrasena))
print("¡Felicitaciones! Creaste tu contraseña." if es_segura else "La contraseña no es segura.")
#ACTIVIDAD 9
contrasena = input("Crea una contraseña: ")
errores = []
if len(contrasena) < 8:
    errores.append("Debe tener al menos 8 caracteres.")
if len(contrasena) > 20:
    errores.append("No más de 20 caracteres.")
if not any(c.isupper() for c in contrasena):
    errores.append("Al menos una mayúscula.")
if not any(c.isdigit() for c in contrasena):
    errores.append("Al menos un número.")
if errores:
    print("La contraseña no es segura:", ", ".join(errores))
else:
    print("¡Felicitaciones! Creaste tu contraseña.")
#ACTIVIDAD 10
jugadas_validas = {'piedra', 'papel', 'tijera'}
jugador1 = input("Jugador 1 (piedra, papel, tijera): ").lower()
jugador2 = input("Jugador 2 (piedra, papel, tijera): ").lower()

if jugador1 not in jugadas_validas or jugador2 not in jugadas_validas:
    print("Error: Ingresa jugadas válidas (piedra, papel, tijera)")
elif jugador1 == jugador2:
    print("EMPATE")
elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
     (jugador1 == 'papel' and jugador2 == 'piedra') or \
     (jugador1 == 'tijera' and jugador2 == 'papel'):
    print("GANA JUGADOR 1")
else:
    print("GANA JUGADOR 2")



