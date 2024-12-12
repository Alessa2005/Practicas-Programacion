import numpy as np
from src.Comparador import Comparador
from src.Consola import Consola
from src.TablaDatos import TablaDatos
from sklearn.model_selection import train_test_split

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
BRIGHT = "\033[1m"

def ejecutar_cancer():

    """
    Ejecuta el análisis del mejor modelo de árbol de decisión para el archivo 'cancer.csv'.

    Este método carga los datos de un archivo CSV, divide los datos en conjuntos de entrenamiento y validación, 
    y evalúa distintos clasificadores para seleccionar el mejor modelo utilizando el F1-score. Los resultados, 
    incluyendo el modelo, F1-score, reporte de clasificación y matriz de confusión, se muestran en consola.

    El proceso se repite en un bucle hasta que el usuario decida salir.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Si ocurre un error durante el proceso de evaluación de clasificadores.
    """

    cl= Consola()
    print(BLUE + BRIGHT + "\n--ANÁLISIS DEL MEJOR ÁRBOL DE DESICIÓN PARA CANCER.CSV--\n\n" + RESET)
    tabla = TablaDatos("cancer.csv")
    x, y = tabla.datos("diagnosis")

    x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=0.3, random_state=42)
    comparador = Comparador(x_train, y_train, x_valid, y_valid)
    resultados = comparador.comparaClasificadores()

    ordenados = comparador.ordenar(resultados)
    for resultado in ordenados:
        print("______________________________________________________________")
        print(f"\nModelo: {resultado['Modelo']}")
        print(f"F1-Score: {resultado['f1Score']}")
        print("Reporte de Clasificación:\n")
        print(resultado['Reporte'])
        print("Matriz de Confusión:")
        print(resultado['Matriz_de_confusión'])
        print("\n")

    mejor = ordenados[0]

    print(BRIGHT + GREEN + "Mejor Árbol de Desición:" + RESET)
    print(f"Modelo: {mejor['Modelo']}")
    print(f"F1-Score: {mejor['f1Score']}")
    print("Reporte de Clasificación:")
    print(mejor['Reporte'])
    print("Matriz de Confusión:")
    print(mejor['Matriz_de_confusión'])
    print("\n")

def ejecutar_bases():
    """
    Ejecuta el proceso de clasificación utilizando bases de datos genéricas.

    Este método permite al usuario seleccionar dos bases de datos, una para el entrenamiento y otra para la validación, 
    asegurándose de que ambas tengan las mismas clases y etiquetas. Luego, se selecciona una columna como objetivo de la predicción 
    y se evalúan diferentes clasificadores. Los resultados, incluyendo el modelo, F1-score, reporte de clasificación y matriz de confusión, 
    se muestran en consola.

    El proceso se repite en un bucle hasta que el usuario decida salir.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Si ocurre un error durante la selección de bases de datos o el proceso de evaluación de clasificadores.
    """

    cl = Consola()
    print(BLUE + BRIGHT + "\n--CLASIFICADOR CON BASES GENÉRICAS--\n\n" + RESET)
    print(
        BRIGHT + GREEN + "Asegúrate de que los archivos a seleccionar se encuentren en la carpeta /docs de este proyecto.\n" + RESET)
    base_entrena = cl.entradaDatos("Ingrese el nombre de la base de datos que se usará para el entrenamiento: ")
    base_valid = cl.entradaDatos("\nIngrese el nombre de la base de datos que se usará para la validación: ")
    if not base_entrena.compara(base_valid):
        print(
            BRIGHT + RED + f"Error: Las etiquetas y la clase de los archivos ingresados no coinciden. Por favor," "asegúrate de que ambas bases de datos tengan las mismas clases y etiquetas." + RESET)
        print(BRIGHT + "Intente de nuevo\n" + RESET)
        return
    titulo = "\n\nSeleccione la columna que definirá el objetivo de la predicción (clase)." \
             "El resto de columnas serán asignadas como datos asociados a esta clase (etiquetas).\n"
    clase = cl.mostrar_opciones(titulo, base_entrena.cabecera())
    if clase == "regresar":
        return
    x_entrenar, y_entrenar = base_entrena.datos(clase)
    x_validacion, y_validacion = base_valid.datos(clase)

    validar_datos(x_entrenar, "Entrenamiento")
    validar_datos(x_validacion, "Validación")
    
    cd = Comparador(x_entrenar, y_entrenar, x_validacion, y_validacion)
    resultados = cd.ordenar(cd.comparaClasificadores())
    for resultado in resultados:
        print("______________________________________________________________")
        print("\nModelo: " + str(resultado["Modelo"]))
        print("f1Score: " + str(resultado["f1Score"]))
        print("Reporte: \n" + str(resultado["Reporte"]))
        print("Matriz_de_confusión: \n" + str(resultado["Matriz_de_confusión"]) + "\n")

def validar_datos(datos, nombre):
    """
    Verifica que los datos proporcionados sean válidos para su uso en el modelo.
        
    Args:
        datos (np.ndarray): Matriz de datos a validar.
        nombre (str): Nombre del conjunto de datos para identificar errores.
        
    Raises:
        ValueError: Si los datos contienen valores no numéricos o NaN.
    """
    if not np.issubdtype(datos.dtype, np.number):
        raise ValueError(f"El conjunto de datos '{nombre}' contiene valores no numéricos." \
                         " Intenta con otra clase (todas las etiquetas deben ser valores numéricos).")
    if np.isnan(datos).any():
        raise ValueError(f"El conjunto de datos '{nombre}' contiene valores faltantes (NaN).")