#Bucles for y range "range(5)" → 0,1,2,3,4
for i in range(5):
    print(i) # 1 2 3 4 5

#listas con datos
numeros = [1, 2, 3, 4]
for n in numeros:
    print(n)


#metodos con texto texto[::-1] invierte texto
def palindromo(texto):
    return texto == texto[::-1]

#largo del texto en numeros
def contar_letras(texto):
    return len(texto)

#recorre el texto
for letra in "texto":
    print(letra)
# t 
# e
# x
# t
# o

#metodo append() devuelve el texto al final
pares = []

for n in [1,2,3,4,5]:
    if n % 2 == 0:
        pares.append(n)

print(pares) #devuelve solo 2 4 porque lo agrega al finalde la formula

#DICCIONARIOS: es una estructura clave -> VALOR
usuario = {
    "nombre": "Abra",
    "edad": 20,
    "pais": "Panama"
}

#ACCEDER A ESTOS DATOS
print(usuario["nombre"])  # Abra
#AGREGAR DATOS
usuario["email"] = "abra@gmail.com"
#RECORRER DICCIONARIO
for clave, valor in usuario.items():
    print(clave,valor)
    #clave nombre edad pais 
    #usuario.value = abra 20 panama = valor

