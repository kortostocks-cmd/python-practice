
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

#todo junto
precios_con_itbms = [100, 107, 50, 53.5, 20, 21.4]

def obtener_solo_impuestos(lista):
    # Asumiendo que el precio base es múltiplo de 100 y el impuesto es 7%
    # Filtramos los que NO son enteros redondos o tienen el decimal del 7%
    return list(filter(lambda p: p % 1 != 0, lista))

# Si lo que quieres es filtrar una lista de diccionarios por una categoría:
productos = [
    {"nombre": "A", "precio": 50, "tiene_impuesto": False},
    {"nombre": "B", "precio": 20, "tiene_impuesto": True},
    {"nombre": "C", "precio": 100, "tiene_impuesto": True}
]

def filtrar_con_impuesto(lista):
    return list(filter(lambda x: x["tiene_impuesto"] == True, lista))

print(filtrar_con_impuesto(productos))

 #TODO JUNTO
precios_con_itbms = [100, 107, 50, 53.5, 20, 21.4]

def obtener_solo_impuestos(lista):
    return list(filter(lambda p: p % 1 != 0, lista))

print(obtener_solo_impuestos(precios_con_itbms))
