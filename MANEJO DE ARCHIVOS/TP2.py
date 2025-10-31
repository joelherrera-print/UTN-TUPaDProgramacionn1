#TRABAJO PRÁCTICO – MANEJO DE ARCHIVOS EN PYTHON
#1.	
#•	Crear un archivo llamado “notas.txt” que contenga tres líneas con el nombre de un alumno y su nota, separados por una coma.
#Ejemplo del contenido esperado:
#Sofía,9
#Marcos,7
#Ana,10
#•	Abrir el archivo en modo lectura y mostrar su contenido línea por línea, eliminando los saltos de línea.
#•	Leer el archivo y mostrar los datos con el siguiente formato:
#Alumno: Sofía | Nota: 9
#Alumno: Marcos | Nota: 7
#Alumno: Ana | Nota: 10
#•	Abrir el archivo en modo 'a' y permitir agregar más alumnos con sus notas desde teclado.
#El usuario puede ingresar varios hasta escribir “n”.
#•	Reescribir el archivo desde cero con una nueva lista de tres alumnos distintos.
#•	Mostrar un mensaje que indique que el contenido anterior fue reemplazado.

with open("notas.txt", "w") as archivo:
    archivo.write("Sofia , 9\n")
    archivo.write("Marcos, 7\n")
    archivo.write("Ana , 10\n")

print("Leyendo archivo y mostrando contenido")

with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

with open("notas.txt","r") as archivo:
    for linea in archivo:
        nombre , nota = linea.strip().split(",")
        print(f"ALUMNO: {nombre} | NOTA: {nota}")

with open("notas.txt" , "a") as archive:
    while True:
        ingresar_alumnos = input("Ingrese alumno nuevo (o 'n' para terminar): ")
        if ingresar_alumnos.lower() == "n":
            break
        nota_nueva = input("Ingrese su respectiva nota: ")
        archive.write(f"{ingresar_alumnos}.{nota_nueva}\n")
        print("✅Alumno agregado correctamente.")

with open("notas.txt", "w") as archivo:
    archivo.write("Pedro,8\n")
    archivo.write("Lucia,9\n")
    archivo.write("Santi,6\n")

print("✅ El contenido anterior fue reemplazado por una nueva lista de alumnos.")



#2.	
#•	Crear un archivo llamado heladeria.csv con tres sabores de ejemplo.
#•	Abrir el archivo en modo lectura lectura y mostrar su contenido línea por línea en el siguiente formato:
#Sabor: Chocolate | Precio: $1200 | Disponible: si
#Agregar un nuevo sabor
#Pedir al usuario que ingrese:
#•	El nombre del sabor
#•	El precio
#•	Si está disponible ("si" o "no")
#Luego abrir el archivo en modo 'a' (agregar) y escribir la nueva línea sin borrar el contenido anterior.
#•	Confirmar la actualización

with open("heladeria.csv" , "w") as archivo:
    archivo.write("Frutilla , 300 , SI\n")
    archivo.write("Chocolate , 400 , SI\n")
    archivo.write("Tramontana , 500 , SI\n")

print("Leyendo archivo y mostrando contenido")

with open("heladeria.csv","r") as archivo:
    for linea in archivo:
        sabor, precio, disponibilidad = linea.strip().split(",")
        print(f"SABOR:{sabor} | PRECIO:{precio} | DISPONIBILIDAD:{disponibilidad}\n" )

sabor_nuevo = input("Agregar sabor nuevo: ")
precio_nuevo = float(input("Agregar su precio: "))
esta_dispo = input("Si está disponible (si o no): ")

with open("heladeria.csv" , "a") as archivo:
     archivo.write(f"{sabor_nuevo} , {precio_nuevo} , {esta_dispo}\n")

print("✅ Producto agregado correctamente.")

#3.	
#•	Crear un archivo llamado cine.csv con tres películas.
#•	Mostrar el contenido del archivo
#•	Leer el archivo completo y mostrar su contenido tal cual está (sin procesar línea por línea todavía).
#•	Agregar una nueva película-Pedir al usuario los datos y agregarlos sin borrar el contenido anterior
#•	Mostrar confirmación final
#•	Reabrir el archivo y mostrar su contenido actualizado.

with open("cine.csv", "w") as archivo:
    archivo.write("La momia\n")
    archivo.write("IT\n")
    archivo.write("Casablanca\n")

with open ("cine.csv" , "r") as archivo:
        print(archivo.read())

with open("cine.csv","r") as f:
    contenido = f.read()
    print(contenido)

peli_new = input("Agregar una pelicula nueva:")
with open("cine.csv" , "a")as archivo:
    archivo.write(f"{peli_new}\n")

print("Película agregada con éxito!")

with open("cine.csv", "r") as archivo:
    print(archivo.read())
  
#4.	
#•	Crear un archivo llamado pacientes.csv con los siguientes datos:
#nombre,edad,turno
#•	Abrir el archivo en modo lectura y mostrar el contenido 
#•	Permitir al usuario agregar un nuevo paciente, pidiendo:
#Nombre
#Edad
#Si tiene turno (“si” / “no”)
#Luego escribir esa línea al final del archivo.
#•	Reabrir el archivo y mostrar el contenido actualizado.



#5.	
#•	Crear un archivo llamado excursiones.csv con el siguiente contenido:
#destino,precio,disponible
#•	Abrir el archivo en modo lectura y mostrar los destinos.
#•	Agregar una nueva excursión.
#Pedir al usuario:
#El nombre del destino
#El precio
#Si está disponible (“si” o “no”)
#•	Luego abrir el archivo en modo 'a' y escribir la nueva línea sin borrar el contenido anterior.
#•	Reabrir el archivo y mostrar su contenido actualizado.

