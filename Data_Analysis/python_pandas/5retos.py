import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración estética para los gráficos
plt.style.use('ggplot')

# --- PREPARACIÓN DE DATOS ---
data = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Laptop', 'Monitor', 'Mouse', 'Teclado', 'Laptop', 'Webcam'],
    'Vendedor': ['Ana', 'Luis', 'Ana', 'Luis', 'Ana', 'Pedro', 'Pedro', 'Ana', 'Luis', 'Pedro'],
    'Ventas': [1200, 25, 300, 150, 1300, 310, 30, 160, 1250, 80],
    'Fecha': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'])
}

df = pd.DataFrame(data)

# --- RESOLUCIÓN DE RETOS ---

print("--- NIVEL 1: Ventas de Ana > 200 ---")
filtro_ana = df[(df.Vendedor == 'Ana') & (df.Ventas > 200)]
print(filtro_ana, "\n")

print("--- NIVEL 2: Totales por Vendedor ---")
totales = df.groupby('Vendedor')['Ventas'].sum()
mejor_vendedor = totales.idxmax()
print(totales)
print(f"El mejor vendedor es: {mejor_vendedor}\n")

print("--- NIVEL 3: Cálculo de Precios con Descuento ---")
df['Descuento'] = df['Ventas'] * 0.10
df['Precio_Final'] = df['Ventas'] - df['Descuento']
print(df[['Producto', 'Ventas', 'Descuento', 'Precio_Final']].head(), "\n")

print("--- NIVEL 4: Top 3 Productos (Mayúsculas) ---")
top_3 = df.nlargest(3, 'Ventas').copy()
top_3['Producto'] = top_3['Producto'].str.upper()
print(top_3, "\n")

print("--- NIVEL 5: Rango de Fechas (03 al 07 de Enero) ---")
rango_fechas = df[df['Fecha'].between('2024-01-03', '2024-01-07')]
print(rango_fechas, "\n")

# --- VISUALIZACIÓN DE RESULTADOS ---

# Crear una figura con varios subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Ventas Totales por Vendedor (Barras)
totales.plot(kind='bar', ax=axes[0], color=['#3498db', '#e74c3c', '#2ecc71'])
axes[0].set_title('Total de Ventas por Vendedor')
axes[0].set_ylabel('USD')
axes[0].tick_params(axis='x', rotation=0)

# Gráfico 2: Ventas vs Precio Final (Comparativa)
df[['Ventas', 'Precio_Final']].plot(kind='line', marker='o', ax=axes[1])
axes[1].set_title('Efecto del Descuento en las Ventas')
axes[1].set_ylabel('Precio')
axes[1].set_xlabel('Índice de Venta')

plt.tight_layout()
plt.show()