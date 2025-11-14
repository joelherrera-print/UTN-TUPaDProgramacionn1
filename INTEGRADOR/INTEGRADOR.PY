import csv
import os

#Función para leer el CSV y retornar lista de diccionarios
def leer_csv(archivo):
    paises = []
    try:
        with open(archivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Convertir población y superficie a int
                    row['poblacion'] = int(row['poblacion'])
                    row['superficie'] = int(row['superficie'])
                    paises.append(row)
                except ValueError:
                    print(f"Error de formato en fila: {row}. Se omite.")
        if not paises:
            raise ValueError("El archivo CSV está vacío o sin datos válidos.")
        return paises
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo}' no encontrado.")
        exit(1)
    except Exception as e:
        print(f"Error al leer CSV: {e}")
        exit(1)

# Función para buscar país por nombre 
def buscar_por_nombre(paises, nombre):
    nombre_lower = nombre.lower()
    resultados = [p for p in paises if nombre_lower in p['nombre'].lower()]
    if not resultados:
        print("No se encontraron países con ese nombre.")
    return resultados

# Función para filtrar países
def filtrar_paises(paises, opcion, params):
    if opcion == 'continente':
        continente = params.get('continente', '').lower()
        return [p for p in paises if p['continente'].lower() == continente]
    elif opcion == 'poblacion':
        min_pop = params.get('min', 0)
        max_pop = params.get('max', float('inf'))
        return [p for p in paises if min_pop <= p['poblacion'] <= max_pop]
    elif opcion == 'superficie':
        min_sup = params.get('min', 0)
        max_sup = params.get('max', float('inf'))
        return [p for p in paises if min_sup <= p['superficie'] <= max_sup]
    return []

# Función para ordenar países
def ordenar_paises(paises, criterio, ascendente=True):

    if criterio == 'nombre':
        key = lambda p: p['nombre'].lower()
    elif criterio == 'poblacion':
        key = lambda p: p['poblacion']
    elif criterio == 'superficie':
        key = lambda p: p['superficie']
    else:
        print("Criterio inválido.")
        return []
    return sorted(paises, key=key, reverse=not ascendente)

# Función para calcular estadísticas
def calcular_estadisticas(paises):
    if not paises:
        return {}
    
    # Max y min población
    max_pop = max(paises, key=lambda p: p['poblacion'])
    min_pop = min(paises, key=lambda p: p['poblacion'])
    
    # Promedios
    total_pop = sum(p['poblacion'] for p in paises)
    total_sup = sum(p['superficie'] for p in paises)
    promedio_pop = total_pop / len(paises)
    promedio_sup = total_sup / len(paises)
    
    # Conteo por continente
    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1
    
    return {
        'max_pop': max_pop,
        'min_pop': min_pop,
        'promedio_pop': promedio_pop,
        'promedio_sup': promedio_sup,
        'continentes': continentes
    }

# Función para mostrar lista de países
def mostrar_paises(lista):
    if not lista:
        print("No hay resultados para mostrar.")
        return
    for p in lista:
        print(f"Nombre: {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²| Continente: {p['continente']}")

# Función para mostrar estadísticas
def mostrar_estadisticas(stats):
    if not stats:
        print("No hay datos para estadísticas.")
        return
    print(f"País con mayor población: {stats['max_pop']['nombre']} ({stats['max_pop']['poblacion']})")
    print(f"País con menor población: {stats['min_pop']['nombre']} ({stats['min_pop']['poblacion']})")
    print(f"Promedio de población: {stats['promedio_pop']:.2f}")
    print(f"Promedio de superficie: {stats['promedio_sup']:.2f} km²")
    print("Cantidad de países por continente:")
    for cont, cant in stats['continentes'].items():
        print(f"  {cont}: {cant}")

# Menú principal
def menu_principal(paises):
    while True:
        print("\n============ Menú ============:")
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas")
        print("5. Salir")
        print("===================")
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '1':
            nombre = input("Ingrese nombre del país: ").strip()
            if not nombre:
                print("Entrada inválida.")
                continue
            resultados = buscar_por_nombre(paises, nombre)
            mostrar_paises(resultados)
        
        elif opcion == '2':
            print("Filtro por: (a) Continente, " \
                              "(b) Rango población, " \
                              "(c) Rango superficie")
            sub_op = input("Elige: ").strip().lower()
            if sub_op == 'a':
                cont = input("Ingrese continente: ").strip()
                resultados = filtrar_paises(paises, 'continente', {'continente': cont})
            elif sub_op == 'b':
                try:
                    min_pop = int(input("Población mínima: "))
                    max_pop = int(input("Población máxima: "))
                    resultados = filtrar_paises(paises, 'poblacion', {'min': min_pop, 'max': max_pop})
                except ValueError:
                    print("Entrada no numérica.")
                    continue
            elif sub_op == 'c':
                try:
                    min_sup = int(input("Superficie mínima: "))
                    max_sup = int(input("Superficie máxima: "))
                    resultados = filtrar_paises(paises, 'superficie', {'min': min_sup, 'max': max_sup})
                except ValueError:
                    print("Entrada no numérica.")
                    continue
            else:
                print("Opción inválida.")
                continue
            if not resultados:
                print("No se encontraron países.")
            mostrar_paises(resultados)
        
        elif opcion == '3':
            print("Ordenar por: (a) Nombre, "
                               "(b) Población, "
                               "(c) Superficie")
            crit = input("Elige: ").strip().lower()
            if crit == 'a':
                crit = 'nombre'
            elif crit == 'b':
                crit = 'poblacion'
            elif crit == 'c':
                crit = 'superficie'
            else:
                print("Criterio inválido.")
                continue
            dir_asc = input("Ascendente (si/no)? ").strip().lower() == 'si'
            resultados = ordenar_paises(paises, crit, dir_asc)
            mostrar_paises(resultados)
        
        elif opcion == '4':
            stats = calcular_estadisticas(paises)
            mostrar_estadisticas(stats)
        
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecución principal
if __name__ == "__main__":
    archivo_csv = "paises.csv"  # Nombre del archivo CSV
    paises = leer_csv(archivo_csv)
    print(f"Se cargaron {len(paises)} países.")
    menu_principal(paises)