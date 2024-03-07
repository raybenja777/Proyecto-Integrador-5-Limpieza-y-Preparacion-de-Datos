import pandas as pd

def preprocesar_datos(df):
    # Verificar y manejar valores faltantes
    df.dropna(inplace=True)

    # Verificar y eliminar filas duplicadas
    df.drop_duplicates(inplace=True)
    
    # Verificar y eliminar valores atípicos en la columna 'Ingresos'
    Q1 = df['Ingresos'].quantile(0.25)
    Q3 = df['Ingresos'].quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    df = df.loc[(df['Ingresos'] >= limite_inferior) & (df['Ingresos'] <= limite_superior)]
    
    # Crear una columna que categorice por grupos de edad
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jovenes Adultos', 'Adulto', 'Adulto mayor']
    df['Categoria_edad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

    # Guardar el resultado como csv
    df.to_csv('datos_preprocesados.csv', index=False)

    return df

# Cargar el archivo CSV
df = pd.read_csv('datos.csv')

# Llamar a la función preprocesar datos
df = preprocesar_datos(df)

# Imprimir el DataFrame
print(df)