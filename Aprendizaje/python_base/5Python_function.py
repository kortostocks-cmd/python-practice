
#Practicas funciones

# descuento basico
def calcular_descuento(precio, impuesto):
    return precio * (1 -impuesto)

print(calcular_descuento(100,0.07))

# Descuento fijo
def aplicar_impuesto(precios):
    totales = [] 

    for p in precios:
        total = p * 1.07 
        totales.append(total)
    return totales

mis_precios = 100, 200, 300
print(aplicar_impuesto(mis_precios))

# Pares
def pares(numeros):
    pares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares

numeros = 1,2,3,4,5
print(pares(numeros))


#LAMBDAS 
productos = [
    {"nombre": "A", "precio":50},
    {"nombre": "B", "precio":20},
    {"nombre": "C", "precio":100}
]

# Ordenar de mayor a menor 
productos.sort(key=lambda x: x["precio"], reverse=True)

print(productos)



