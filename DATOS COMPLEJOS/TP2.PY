##Trabajo Practico n°2:ESTRUCTURAS COMPLEJAS

#Ejercicio 1 – Listas básicas 
#Crea una lista llamada materias con al menos 5 materias. 
##Agrega una materia nueva con append(). 
#Elimina una materia con remove(). 
#Ordena la lista alfabéticamente y muéstrala por pantalla. 


materias = ["Matemática", "Programación", "Inglés", "Historia", "Biología"]
materias.append("Física")
materias.remove("Historia")
materias.sort()
print("Materias ordenadas:", materias)

##Ejercicio 2 – Búsqueda en listas 
#Crea una lista con los nombres de 5 alumnos. 
#Solicita al usuario un nombre y verifica si está en la lista. 
#Si está, muestra su posición en la lista. 
#Si no está, muestra un mensaje apropiado


alumnos = ["Juan", "Maria", "Pedro", "Lucia", "Sofia"]
nombre = input("Ingrese un nombre: ")
if nombre in alumnos:
    print(f"{nombre} está en la posición {alumnos.index(nombre)}")
else:
    print("El nombre no se encuentra en la lista")

#Ejercicio 3 – Contar elementos repetidos 
#Crea una lista con varios números (algunos repetidos). 
#Usa el método count() para mostrar cuántas veces aparece un número elegido por el usuario. 


numeros = [2, 5, 3, 2, 7, 5, 2, 8, 3]
num = int(input("Ingrese un número para contar: "))
print(f"El número {num} aparece {numeros.count(num)} veces")

#Ejercicio 4 – Tuplas básicas 
#Crea una tupla llamada colores con al menos 5 colores. 
#Muestra el primer y el último color usando índices. 
#Verifica si un color ingresado por el usuario está en la tupla. 
#Muestra la cantidad total de elementos con len(). 


colores = ("Rojo", "Verde", "Azul", "Amarillo", "Negro")
print("Primer color:", colores[0])
print("Último color:", colores[-1])
color = input("Ingrese un color: ")
if color in colores:
    print("El color está en la tupla")
else:
    print("El color no está en la tupla")
print("Cantidad total de colores:", len(colores))

#Ejercicio 5 – Tuplas de alimentos 
#Crea una tupla llamada alimentos con 4 comidas diferentes. 
#Muestra el segundo y el último alimento usando índices. Luego muestra cuántos elementos contiene la tupla. 


alimentos = ("Pizza", "Hamburguesa", "Ensalada", "Pasta")
print("Segundo alimento:", alimentos[1])
print("Último alimento:", alimentos[-1])
print("Total de alimentos:", len(alimentos))

#Ejercicio 6 - Crea un conjunto con los nombres de tus amigos (algunos repetidos). 
#Muestra el conjunto para observar el comportamiento con duplicados. 
#Agrega y elimina un nombre. 
#Muestra la cantidad total de elementos. 


amigos = {"Juan", "Pedro", "María", "Pedro", "Lucía"}
print("Conjunto sin duplicados:", amigos)
amigos.add("Carla")
amigos.discard("Juan")
print("Cantidad total de amigos:", len(amigos))

#Ejercicio 7 – Operaciones con conjuntos Crea dos conjuntos: 
#materias_1 = {"Programación", "Matemática", "Inglés"} materias_2 = {"Programación", "Base de Datos", "Inglés"} 
#Muestra: 
#a)	Materias comunes 
#b)	Materias exclusivas del primer conjunto 
#c)	Todas las materias sin repetir 


materias_1 = {"Programación", "Matemática", "Inglés"}
materias_2 = {"Programación", "Base de Datos", "Inglés"}
print("Materias comunes:", materias_1 & materias_2)
print("Exclusivas del primer conjunto:", materias_1 - materias_2)
print("Todas las materias sin repetir:", materias_1 | materias_2)

#Ejercicio 8 – Diccionario de alumnos 
#Crea un diccionario con 3 alumnos y sus notas. 
#Agrega un nuevo alumno. 
#Modifica la nota de uno existente. 
#Muestra todas las claves y valores. 


alumnos = {"Juan": 8, "María": 9, "Pedro": 7}
alumnos["Lucía"] = 10
alumnos["Pedro"] = 8
print("Alumnos y notas:", alumnos)

#Ejercicio 9 – Verificación de acceso 
#Crea un diccionario con las claves "usuario" y "contraseña". 
#Solicita los datos al usuario y verifica si coinciden. 
#Muestra “Acceso concedido” o “Acceso denegado”. 

login = {"usuario": "admin", "contraseña": "1234"}
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")
if usuario == login["usuario"] and contraseña == login["contraseña"]:
    print("Acceso concedido")
else:
    print("Acceso denegado")

#Ejercicio 10 – Eliminar clave de diccionario 
#Crea un diccionario con tres ciudades y su cantidad de habitantes. 
#Elimina una ciudad usando pop(). 
#Muestra el diccionario actualizado. 


ciudades = {"Mendoza": 1200000, "Córdoba": 1500000, "Rosario": 1300000}
ciudades.pop("Rosario")
print("Diccionario actualizado:", ciudades)

#Ejercicio 11 – Diccionario de precios 
#Crea un diccionario con al menos 4 productos y sus precios. Permite al usuario ingresar el nombre de un producto. 
#Muestra su precio si existe, o un mensaje si no se encuentra. 


precios = {"pan": 500, "leche": 750, "queso": 1200, "jamón": 1500}
producto = input("Ingrese el nombre de un producto: ")
if producto in precios:
    print(f"El precio de {producto} es ${precios[producto]}")
else:
    print("El producto no se encuentra en la lista")

#Ejercicio 12 – Convertir lista en conjunto 
#Crea una lista con números repetidos. 
#Convierte la lista en conjunto para eliminar los duplicados. 
#Muestra ambos (lista y conjunto) para comparar los resultados. 


numeros = [1, 2, 3, 2, 4, 1, 5, 3]
conjunto_numeros = set(numeros)
print("Lista original:", numeros)
print("Conjunto sin duplicados:", conjunto_numeros)

#Ejercicio 13 – Intersección de conjuntos 
#Crea dos conjuntos de números enteros. 
#Muestra los números que tienen en común (intersección). 


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Elementos en común:", a & b)

#Ejercicio 14 – Promedio de notas 
#Crea un diccionario con 3 alumnos y sus notas numéricas. Calcula y muestra el promedio general de todas las notas

notas = {"Juan": 8, "María": 9, "Pedro": 7}
promedio = sum(notas.values()) / len(notas)
print("Promedio general:", promedio)

#Ejercicio 15 – Agregar productos y mostrar precios 
#Crea un diccionario vacío llamado productos. 
#Permite al usuario ingresar 3 productos con su precio. Luego, muestra todos los productos con sus precios. 

productos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    productos[nombre] = precio

print("Productos y precios:")
for nombre, precio in productos.items():
    print(f"{nombre}: ${precio}")