import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def cargar_datos(ruta_archivo):
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv(ruta_archivo)
   
    
def generar_nube_palabras(df, column_name, ruta_salida):
    """Genera una nube de palabras a partir del texto proporcionado."""

    ## INICIO - COMPLETAR CODIGO
    # Concatenar todo el texto de la columna especificada
    texto = None
    ## FIN - COMPLETAR CODIGO

    nube = WordCloud(width=800, height=400, background_color='white').generate(texto)
    plt.figure(figsize=(10, 5))
    plt.imshow(nube, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(ruta_salida)
    plt.close()

if __name__ == "__main__":
    ruta_archivo = 'expectativas.csv'  # Cambia esto por la ruta de tu archivo CSV
    columna_texto = 'expectativa'      # Cambia esto por el nombre de la columna que contiene el texto
    ruta_salida = 'nube_palabras.png'  # Ruta donde se guardará la imagen de la nube de palabras

    df = cargar_datos(ruta_archivo)
    generar_nube_palabras(df, columna_texto, ruta_salida)
    print(f"Nube de palabras guardada en {ruta_salida}")
