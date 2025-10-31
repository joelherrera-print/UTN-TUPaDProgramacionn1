#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista

#ACTIVIDAD 1

with open("productos.txt","w") as archivo:
    archivo.write("Perfume,150,20\n")
    archivo.write("Computadora,2000,2\n")
    archivo.write("Telefono,450,34\n")

#ACTIVIDAD 2

print("Leyendo archivo y mostrando contenido")

with open("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#ACTIVIDAD 3

nombre_nuevo = input("ingrese el nombre de producto nuevo: ")
precio_nuevo = float(input("Ingrese el precio del producto nuevo: "))
cantidad = float(input("Ingrese la cantidad del prducto nuevo: "))

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad}\n")

print("✅ Producto agregado correctamente.")

#ACTIVIDAD 4

productos = []  

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad":cantidad
        }
        productos.append(producto)

for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


#ACTIVIDAD 5

buscar_nombre = input("Ingrese el nombre que dea buscar: ").strip()
encontrado = False

for p in productos:
    if p ["nombre"].lower() == buscar_nombre.lower():
        print(f"✅Producto encotrado: ")
        print(f"nombre: {p['nombre']} , Precio: ${p['precio']} , Cantidad: {p['cantidad']}")
        encontrado = True

if not encontrado:
    print("❌ El producto no existe en la lista.")

#ACTIVIDAD 6

with open("productos.txt" , "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}")

print("💾 Archivo 'productos.txt' actualizado correctamente.")



