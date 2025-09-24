#Actividad 1
lista = list(range(4,100,4))
print(lista)

#Actividad 2
lista = ["cuchillo","cs","mariposa","sofia","dolares "]
print(lista[3])

#Actividad 3
lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append(3)
print(lista_vacia)

#Actividad 4
animales = ["perro", "gato", "conejo", "pez"] 
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#Actividad 5
#numero.remove remueve el un numero de la lista, y al ser max(numero) remueve el mas grande

#Actividad 6
lista = list(range(10 ,30 ,5))
print(lista[0:2])

#Actividad 7
autos = ["sedan", "polo", "suran", "gol"] 
autos[0] = "peugeot"
autos[1] = "chevrolet"
print(autos)

#Actividad 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"
compras[0].remove("pan")
print(compras)
 
#Actividad 10
lista_anidada = [15,True,[25.5, 57.9, 30.6],False ]              
print(lista_anidada)