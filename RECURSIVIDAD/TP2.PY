##TRABAJO PRACTICO DE RECURSIVIDAD



# 1. Crear una función recursiva suma_pares(n) que calcule la suma de todos
#los números pares desde 2 hasta n

def suma_pares(n):
    if n < 2:
        return 0
    if n % 2 != 0:
        return suma_pares(n - 1)
    return n + suma_pares(n - 2)


#2. Crear una función recursiva contar_letra(palabra, letra) que cuente cuántas
#veces aparece una letra dentro de una cadena de texto

def contar_letra(palabra, letra):
    if palabra == "":
        return 0
    return (1 if palabra[0] == letra else 0) + contar_letra(palabra[1:], letra)


# 3. Definir una función recursiva invertir_cadena(texto) que devuelva el texto
#invertido.

def invertir_cadena(texto):
    if texto == "":
        return ""
    return invertir_cadena(texto[1:]) + texto[0]


#4. Diseñar una función recursiva contar_elementos(lista) que cuente la
#cantidad total de elementos en una lista, sin usar len().

def contar_elementos(lista):
    if lista == []:
        return 0
    return 1 + contar_elementos(lista[1:])


# 5. Crear una función recursiva contiene_letra(palabra, letra) que indique si
#una letra está presente en la palabra.



def contiene_letra(palabra, letra):
    if palabra == "":
        return False
    if palabra[0] == letra:
        return True
    return contiene_letra(palabra[1:], letra)


# 6.Definir una función recursiva multiplicar(a, b) que calcule la multiplicación
#de dos números utilizando solo sumas.


def multiplicar(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + multiplicar(a, b - 1)
    else:  # Para soportar números negativos
        return -multiplicar(a, -b)


# 7. Crear una función recursiva llamada cuenta_regresiva(n) que reciba un
#número entero positivo y muestre todos los números desde n hasta 1, en
#orden descendente

def cuenta_regresiva(n):
    if n == 0:
        return
    print(n)
    cuenta_regresiva(n - 1)


# 8.  Crear una función recursiva llamada mostrar_letras(palabra) que reciba
#una cadena de texto y la muestre letra por letra, una debajo de otra, usando
#recursividad.

def mostrar_letras(palabra):
    if palabra == "":
        return
    print(palabra[0])
    mostrar_letras(palabra[1:])