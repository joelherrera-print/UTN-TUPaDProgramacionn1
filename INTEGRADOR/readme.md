# Sistema de Gestión de Países

## Descripción del Programa

Este programa es un sistema de gestión y análisis de datos de países desarrollado en Python. Permite cargar información desde un archivo CSV y realizar diversas operaciones como búsquedas, filtros, ordenamientos y cálculos estadísticos sobre los datos de los países.

El sistema está diseñado para facilitar el análisis de información demográfica y geográfica de manera interactiva a través de un menú de consola.

### Características Principales

- **Carga de datos desde CSV**: Lee y valida información de países desde un archivo estructurado
- **Búsqueda por nombre**: Encuentra países por coincidencias parciales en el nombre
- **Filtros avanzados**: Filtra países por continente, rango de población o superficie
- **Ordenamiento flexible**: Ordena los resultados por nombre, población o superficie (ascendente/descendente)
- **Estadísticas completas**: Calcula promedios, máximos, mínimos y distribución por continente
- **Validación de datos**: Manejo robusto de errores en el formato del archivo

---

## Instrucciones de Uso

### Requisitos Previos

- Python 3.7 o superior
- Módulo `csv` (incluido en la biblioteca estándar de Python)

### Estructura del Archivo CSV

El programa requiere un archivo CSV con el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45000000,2780400,América del Sur
Brasil,214000000,8515767,América del Sur
Japón,125000000,377975,Asia
```

**Campos obligatorios:**
- `nombre`: Nombre del país (texto)
- `poblacion`: Población total (número entero)
- `superficie`: Superficie en km² (número entero)
- `continente`: Continente al que pertenece (texto)

### Instalación y Ejecución

1. **Clonar o descargar** el proyecto en tu computadora

2. **Preparar el archivo CSV**:
   - Crear un archivo llamado `paises.csv` en el mismo directorio que el programa
   - Asegurarse de que tenga el formato correcto (ver ejemplo arriba)

3. **Ejecutar el programa**:
   ```bash
   python main.py
   ```

4. **Navegar por el menú**: Seleccionar las opciones ingresando el número correspondiente

---

## 📖 Ejemplos de Entradas y Salidas

### Ejemplo 1: Buscar País por Nombre

**Entrada:**
```
Elige una opción: 1
Ingrese nombre del país: arg
```

**Salida:**
```
Nombre: Argentina | Población: 45000000 | Superficie: 2780400 km²| Continente: América del Sur
```

---

### Ejemplo 2: Filtrar por Continente

**Entrada:**
```
Elige una opción: 2
Filtro por: (a) Continente, (b) Rango población, (c) Rango superficie
Elige: a
Ingrese continente: asia
```

**Salida:**
```
Nombre: China | Población: 1400000000 | Superficie: 9596961 km²| Continente: Asia
Nombre: India | Población: 1380000000 | Superficie: 3287263 km²| Continente: Asia
Nombre: Japón | Población: 125000000 | Superficie: 377975 km²| Continente: Asia
```

---

### Ejemplo 3: Filtrar por Rango de Población

**Entrada:**
```
Elige una opción: 2
Filtro por: (a) Continente, (b) Rango población, (c) Rango superficie
Elige: b
Población mínima: 100000000
Población máxima: 200000000
```

**Salida:**
```
Nombre: Brasil | Población: 214000000 | Superficie: 8515767 km²| Continente: América del Sur
Nombre: Japón | Población: 125000000 | Superficie: 377975 km²| Continente: Asia
```

---

### Ejemplo 4: Ordenar Países

**Entrada:**
```
Elige una opción: 3
Ordenar por: (a) Nombre, (b) Población, (c) Superficie
Elige: b
Ascendente (si/no)? no
```

**Salida:**
```
Nombre: China | Población: 1400000000 | Superficie: 9596961 km²| Continente: Asia
Nombre: India | Población: 1380000000 | Superficie: 3287263 km²| Continente: Asia
Nombre: Brasil | Población: 214000000 | Superficie: 8515767 km²| Continente: América del Sur
Nombre: Japón | Población: 125000000 | Superficie: 377975 km²| Continente: Asia
Nombre: Argentina | Población: 45000000 | Superficie: 2780400 km²| Continente: América del Sur
```

---

### Ejemplo 5: Mostrar Estadísticas

**Entrada:**
```
Elige una opción: 4
```

**Salida:**
```
País con mayor población: China (1400000000)
País con menor población: Argentina (45000000)
Promedio de población: 632800000.00
Promedio de superficie: 4911673.00 km²
Cantidad de países por continente:
  Asia: 3
  América del Sur: 2
```

---

## Participación de los Integrantes

###  [Santiago Prandina]
**Rol**: Desarrollador Principal
- Implementación de funciones de lectura y validación de CSV
- Desarrollo de funciones de búsqueda y filtrado
- Pruebas y debugging del sistema

### [Joel Herrera]
**Rol**: Desarrollador de Lógica
- Implementación de funciones de ordenamiento
- Desarrollo del módulo de estadísticas
- Optimización de algoritmos


##  Funciones Principales del Código

### `leer_csv(archivo)`
Lee el archivo CSV y retorna una lista de diccionarios con los datos de los países. Incluye manejo de errores para archivos no encontrados o con formato inválido.

### `buscar_por_nombre(paises, nombre)`
Busca países cuyo nombre contenga el término ingresado (búsqueda insensible a mayúsculas).

### `filtrar_paises(paises, opcion, params)`
Filtra la lista de países según diferentes criterios: continente, rango de población o rango de superficie.

### `ordenar_paises(paises, criterio, ascendente)`
Ordena la lista de países por nombre, población o superficie, en orden ascendente o descendente.

### `calcular_estadisticas(paises)`
Calcula estadísticas como máximo/mínimo de población, promedios y conteo por continente.

### `menu_principal(paises)`
Función principal que gestiona la interacción con el usuario a través del menú de opciones.



## Notas Adicionales

- El programa utiliza **list comprehensions** para optimizar las operaciones de filtrado
- Las funciones **lambda** se emplean para criterios de ordenamiento dinámicos
- El manejo de excepciones (`try-except`) asegura que el programa no se detenga por errores de entrada
- La búsqueda es **case-insensitive** (no distingue mayúsculas de minúsculas)

---

## Manejo de Errores

El programa maneja los siguientes casos de error:

- **Archivo no encontrado**: Muestra un mensaje y finaliza el programa
- **Formato inválido en CSV**: Omite filas con errores y continúa con las válidas
- **Entradas no numéricas**: Solicita reingresar los datos
- **Archivo vacío**: Muestra un mensaje y finaliza el programa
- **Opciones de menú inválidas**: Muestra un mensaje y vuelve a solicitar la opción



## Licencia

Este proyecto fue desarrollado con fines educativos para la asignatura de Programación 1.

