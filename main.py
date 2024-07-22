import pandas as pd
import math

# Leer el archivo original de Excel
df = pd.read_excel('final.xlsx')

# Número de filas por archivo
num_filas_por_archivo = 2000

# Número total de filas del DataFrame (excluyendo la cabecera)
num_filas_total = len(df)

# Número de partes que se necesitarán
num_partes = math.ceil(num_filas_total / num_filas_por_archivo)

# Nombre base para los archivos nuevos
nombre_base_archivo = 'final_part'

# Dividir el DataFrame en partes y guardarlas como archivos separados
for i in range(num_partes):
    inicio = i * num_filas_por_archivo
    fin = inicio + num_filas_por_archivo
    df_parte = df.iloc[inicio:fin]
    
    # Guardar cada parte como un nuevo archivo de Excel con la cabecera original
    nombre_archivo = f'{nombre_base_archivo}_{i+1}.xlsx'
    df_parte.to_excel(nombre_archivo, index=False, header=True)

print("Ficheros divididos y guardados con éxito.")
