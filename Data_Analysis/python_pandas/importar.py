import pandas as pd
import sqlite3
import requests
import io

# 1. Descargamos el archivo REAL directamente de la fuente (raw)
url = "https://raw.githubusercontent.com/AlexTheAnalyst/MySQL-YouTube-Series/main/layoffs.csv"
s = requests.get(url).content

# 2. Lo convertimos en un DataFrame (aquí pandas arregla el formato automáticamente)
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

# 3. Creamos la base de datos (se guardará en la misma carpeta que este script)
conn = sqlite3.connect('analisis_layoffs.db')

# 4. Metemos los datos en la tabla 'layoffs'
df.to_sql('layoffs', conn, if_exists='replace', index=False)

conn.close()
print("¡Listo! Se creó el archivo 'analisis_layoffs.db' con éxito.")

import pandas as pd
import sqlite3
import os

try:
    # URL directa del CSV
    url = "https://raw.githubusercontent.com/AlexTheAnalyst/MySQL-YouTube-Series/main/layoffs.csv"
    
    # Leer datos
    print("Descargando datos...")
    df = pd.read_csv(url)
    
    # Definir ruta en el Escritorio para que no se pierda
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    db_path = os.path.join(desktop, "layoffs_alex.db")
    
    # Crear conexión y guardar
    conn = sqlite3.connect(db_path)
    df.to_sql('layoffs', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"✅ ¡LOGRADO! El archivo está en tu escritorio: {db_path}")
    print(f"Total de filas importadas: {len(df)}")

except Exception as e:
    print(f"❌ Error: {e}")
    