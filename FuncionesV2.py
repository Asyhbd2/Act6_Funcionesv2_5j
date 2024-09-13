print("Funciones version 2")
print("Angel Tadeo De Leon Ceniceros")
#Zona de listas,tuplas,set y diccionarios
celulares=["Samsung A52","Iphone 11","Chafa"]
nombreperros=("Wanona","Princesita","Destructor de universos")
espacio={"Luna","Sol","Estrellas"}
nombreyapellidos={
    "Angel Tadeo":"De Leon Ceniceros",
    "Carlos":"Quinto",
    "Susana":"Horia"
}
#Zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
def verperros(nombres):
    for perros in nombres:
        print(perros)
def verespacio(astros):
    for espacio in astros:
        print(espacio)
def verdiccionario(n):
    for nam in n:
        print(nam)
        print(n[nam])
#Llamadas a funciones
print("Imprime celulares:")
verlista(celulares)        
print("Imprime nombre de perros:")
verperros(nombreperros)
print("Imprime algunos elementos del espacio exterior:")
verespacio(espacio)
print("Imprime los nombres y apellidos")
verdiccionario(nombreyapellidos)