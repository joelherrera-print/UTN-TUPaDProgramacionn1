##Práctico 6: Estructuras de datos complejas

##Actividad 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

##Actividad 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'naranja':1200, 'Manzana':1500, 'pera':2300}

precios_frutas['Banana']= 1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800

print(precios_frutas)

##Actividad 3

frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(frutas)

##Actividad 4

contactos = {} 

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero

nombre_buscar = input("Ingrese el nombre del contacto que desea buscar: ")

if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
else:
    print("Ese contacto no existe.")

##Actividad 5

frase = input("Ingrese una frase: ").lower()

palabras = frase.split()


palabras_unicas = set(palabras)


recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)

##Actividad 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)


print("Promedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

##Actividad 7

parcial1 = {"Ana", "Luis", "Pedro", "María"}
parcial2 = {"Luis", "María", "José"}


ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

##Actividad 8

productos = {
    "harina": 10,
    "azúcar": 5,
    "yerba": 8
}

while True:
    print("\nMenú:")
    print("1. Consultar stock")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ").lower()
        if nombre in productos:
            print(f"Stock de {nombre}: {productos[nombre]}")
        else:
            print("El producto no existe.")
    elif opcion == "2":
        nombre = input("Producto a actualizar: ").lower()
        if nombre in productos:
            cantidad = int(input("Ingrese cantidad a agregar: "))
            productos[nombre] += cantidad
            print(f"Nuevo stock de {nombre}: {productos[nombre]}")
        else:
            print("El producto no existe.")
    elif opcion == "3":
        nombre = input("Ingrese el nuevo producto: ").lower()
        cantidad = int(input("Ingrese stock inicial: "))
        productos[nombre] = cantidad
        print("Producto agregado correctamente.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

