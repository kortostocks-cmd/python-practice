#RETO 1
print("abraham")
print(20)

#RETO 2
nombre = input("COMO TE LLAMAS ")
print("Un Gusto "   + nombre)

#RETO 3
numero = int(input("Dame tu numero "))
print(numero * 2)

#RETO 4
pedi_numero = int(input("Que numero me das "))

if pedi_numero >= 10:
    print("mayor de 10")
else:
    print("menor de 10")

#RETO 5

if pedi_numero % 2 == 0:
    print("par")
else:
    print("impar")

#RETO 6 
for i in range(10):
    print(i)

#RETO 7
numero7 = [1, 2, 3, 4, 5]
print(numero7)

#RETO 8
for n in numero7:
    print(n * 2)

#RETO 9
suma = 0
for nan in numero7:
    suma += nan

print(suma)#me copie perdon

#RETO 10
cantidad_pares = 0
cantidad_impares = 0

for non in numero7:
    if non % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1


print("pares: ",cantidad_pares)
print("impares: ",cantidad_impares)

#RETO 11
def saludo():
    print("Hola mundo")

#RETO 12
def multi(numero):
    return(numero * 2)

#RETO 13
def par_o_impar(numero):
    if numero % 2 == 0:
        print("numero par ",numero)
    else:
        print("numero impar ", numero)

#RETO 14
def suma_total(lista):
    suma = 0
    for n in lista:
        suma += n
        return suma

#RETO 15
def contar_pares(lista):
    pares = 0
    impares = 0
    
    
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        return pares,impares
    
    #resultado = contar_pares([1,2,3,4,5,6])
    #print(resultado)

#RETO 16(
def contar_letras(texto):
    return len(texto)

#RETO 17
def invierte_texto(texto):
    return texto[::-1]

#RETO 18
def contar_letra(palabra, letra_objetivo):
    contador = 0
    
    for letra in palabra:
        if letra == letra_objetivo:
            contador += 1
        
        return contador
    
    print(contar_letra("banana","a"))

#RETO 19
def palindromo(texto):
    return texto == texto[::-1]

#RETO 20
def eliminar_duplicados(lista):
    nueva = []
    
    for n in lista:
        if n not in nueva:
            nueva.append(n)
        
        return nueva
    print(eliminar_duplicados([1,2,2,3,3,4]))
    

#RETO 21
    diccionario = {
        "nombre": "jhon",
        "edad": 20,
        "pais": "USA"
    }

#RETO 22
    for n in diccionario.values():
        print(n)

#RETO 23
    diccionario["email"] = "abraham@gmail.com"

#RETO 24
    texto = "hola hola mundo"
    palabras = texto.split()
    contador = {}
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else: 
            contador[palabra] = 1
        print(contador)

#RETO 25 Login simulador

usuarios = {
    "admin": "1234",
    "abra":"pass"
}

user = input("Usuario: ")
password = input("Contraseña: ")

if user in usuarios:
    if usuarios[user] == password:
        print("login correcto")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no existe")


#RETO 26
with open("archivo.txt","w") as f:
    f.write("abraham")
#RETO 27
with open("archivo.txt","r") as f:
    contenido =f.read()
print(contenido)
#RETO 28
with open("archivo.txt", "w") as f:
    f.write("primera linea\n")
    f.write("segunda linea\n")
    f.write("tercera linea\n")
#RETO 29
with open("archivo.txt","r") as f:
    for contenido in f:
        contenido.read()
#RETO 30
import json

usuarios = {
    "abro": "pass1",
    "lano": "pass2",
    "fano": "pass3"
}

with open("usuarios.json", "w") as f:
    json.dump(usuarios, f)

with open("usuarios.json", "r") as f:
    usuarios = json.load(f)

user = input("Usuario: ")
password = input("Contraseña: ")

if user in usuarios:
    if usuarios[user] == password:
        print("login correcto")
    else:
        print("contraseña incorrecta")
else:
    print("usuario no existe")
    
#RETO 31


#RETO 32
#RETO 33
#RETO 34
#RETO 35