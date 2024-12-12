from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import os

class TablaDatos:
    """
    Representa una base de datos como un data frame.
    :Attributes:
        Archivo: Base de datos representado como un data frame.
    """
    
    def __init__(self, archivo):
        """
        Inicializa una tabla de datos a partir de un archivo CSV.

        Este constructor carga el archivo especificado y lo convierte en un 
        DataFrame para ser manipulado posteriormente.

        Args:
            archivo (str): Ruta del archivo CSV que se desea leer.

        Returns:
            None

        Raises:
            Exception: Si ocurre algún error al intentar leer el archivo.
        """

        self.archivo = self.leer_archivo(archivo)
        
    def verifica_archivo(self, ruta):
        """
        Verifica si un archivo existe dentro de la carpeta 'docs'.

        Este método comprueba si el archivo especificado en la ruta existe dentro 
        de la carpeta 'docs'. Si el archivo no existe o la ruta no es válida, se lanza 
        una excepción.

        Args:
            ruta (str): Nombre del archivo que se desea verificar dentro de la carpeta 'docs'.

        Returns:
            str: Ruta completa del archivo si se encuentra.

        Raises:
            TypeError: Si la ruta proporcionada no es una cadena válida.
            FileNotFoundError: Si el archivo no se encuentra en la carpeta 'docs'.
            Exception: Si ocurre algún error al intentar leer el archivo.
        """
        if not isinstance(ruta, str):
            raise TypeError("La ruta debe ser una cadena válida.")
        ruta_actual = os.path.dirname(__file__)
        ruta_completa = os.path.join(ruta_actual, '../docs', ruta)
        try:
            with open(ruta_completa, 'r') as archivo:
                archivo.read()
            return ruta_completa
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo en la carpeta 'docs': {ruta}")
        except Exception as e:
            raise Exception(f"Ocurrió un error al leer el archivo: {e}")
        
    def leer_archivo(self, ruta):
        """
        Lee un archivo CSV y retorna un DataFrame.

        Este método lee el archivo especificado por la ruta, lo carga en un 
        DataFrame de Pandas y lo retorna.

        Args:
            ruta (str): Ruta del archivo CSV que se desea leer.

        Returns:
            pd.DataFrame: DataFrame con los datos leídos del archivo CSV.

        Raises:
            Exception: Si ocurre algún error al intentar leer el archivo.
        """
        df = pd.read_csv(self.verifica_archivo(ruta))
        return df 
    
    def cabecera(self):
        """
        Devuelve la cabecera del DataFrame.

        Este método retorna las columnas del DataFrame que representa la base de datos.

        Args:
            None

        Returns:
            list[str]: Lista de los nombres de las columnas del DataFrame.
        """
        return self.archivo.columns
    
    def compara(self, tabla2):
        """
        Compara dos objetos TablaDatos para verificar si tienen la misma cabecera.

        Este método compara las cabeceras de dos objetos TablaDatos, devolviendo 
        `True` si las cabeceras coinciden, de lo contrario, devuelve `False`.

        Args:
            tabla2 (TablaDatos): Objeto TablaDatos que se desea comparar con el actual.

        Returns:
            bool: `True` si las cabeceras son iguales, `False` si no lo son.
        """
        return set(self.cabecera()) == set(tabla2.cabecera())

    def columna_clases(self, columna):
        """
        Devuelve una columna específica de la base de datos.

        Este método obtiene una columna específica del DataFrame y la convierte en un 
        array de valores.

        Args:
            columna (str): El nombre de la columna que se desea obtener.

        Returns:
            np.ndarray: Array con los valores de la columna especificada.
        """
        columna = np.array(self.archivo[columna].values)
        return columna.ravel()
    
    def subtabla(self, columna):
        """
        Devuelve una subtabla sin una columna específica.

        Este método elimina la columna especificada del DataFrame y retorna el resto de los datos 
        en un nuevo DataFrame.

        Args:
            columna (str): El nombre de la columna que se desea excluir.

        Returns:
            np.ndarray: Array con todas las columnas de la tabla excepto la columna especificada.
        """
        return self.archivo.drop(columns=[columna]).values

    def datos(self, columna):
        """
        Devuelve las clases y las subtablas de etiquetas a partir de una columna de clases.

        Este método codifica la columna de clases especificada en valores numéricos y retorna 
        la subtabla de etiquetas junto con la columna de clases.

        Args:
            columna (str): El nombre de la columna que contiene las clases.

        Returns:
            tuple: Una tupla donde el primer elemento es la subtabla de etiquetas y el segundo 
                es la columna de clases codificada numéricamente.
        Raises:
            VAlueError: Si la columna no se encuentra en el dataframe.
        """
        if columna not in self.archivo.columns:
            raise ValueError(f"La columna no existe en el DataFrame.")
        clases = LabelEncoder().fit_transform(self.columna_clases(columna))
        subtabla = self.subtabla(columna)
        return subtabla, clases

    
    