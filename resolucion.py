'''
Evaluacion Parcial.
Parte 1
'''

#1
nombres = ["Ana", "Luis", "Pedro"]

#2
#se puede eliminar con pop()

#3
while True:
 print("Hola")
 break #Imprime Hola

#4
informacion = {
 "nombre" : "Derek Adriel Matul",
 "edad" : 20,
 "carrera" : "Ingenieria en sistemas e informatica"
}

#5
#La diferencias entre una lista y tupla es que las tuplas no se pueden modificar, en cambio las listas si.
#las tuplas se reprecentan con () y las listas se representan con []

'''
Parte2
'''

#1
contador = 0
while True:
 num = float(input("Ingrese un numero, si desea termiar ingrese un 0: "))

 if num != 0:
  contador += num
 else:
  print(f"El total es: {contador}")
  break

#2
numeros = [10, 20, 30, 40]

for i in numeros:
 print(f"{i * 2}")

#3

productos = [
 {"nombre" : "Agua", "precio" : 3, "stock" : 10},
 {"nombre" : "Pan", "precio" : 1.20, "stock" : 5},
 {"nombre" : "Leche", "precio" : 8, "stock" : 25}
]

for i in productos:
 print(f"El producto {i['nombre']} cuesta Q.{i['precio']} y hay {i['stock']} unidades disponibles.")