from sklearn.metrics import f1_score, classification_report, confusion_matrix

class Clasificador:
    """
    Clase que encapsula un modelo de clasificación y proporciona métodos para entrenar, predecir y evaluar.

    Atributos:
        modelo: Instancia del modelo de clasificación (por ejemplo, de sklearn).
    """

    def __init__(self, modelo):
        """
        Inicializa el clasificador con el modelo especificado.

        Args:
            modelo: Modelo de clasificación a utilizar
            (debe implementar los métodos fit y predict).
        """
        self.modelo = modelo 

    def entrenar(self, x_entrenar, y_entrenar):
        """
        Entrena el modelo con los datos proporcionados.

        Args:
            x_entrenar: Datos de entrada para el entrenamiento.
            y_entrenar: Etiquetas correspondientes
            a los datos de entrenamiento.
        """
        self.modelo.fit(x_entrenar, y_entrenar)

    def predecir(self, x_validacion):
        """
        Realiza predicciones utilizando el modelo entrenado.

        Args:
            x_validacion: Datos de entrada
            para realizar las predicciones.

        Returns:
            array: Predicciones realizadas por el modelo.
        """
        predicc = self.modelo.predict(x_validacion)
        return predicc

    def evaluar(self, y_predicc, y_validacion):
        """
        Evalúa el desempeño del modelo utilizando métricas comunes.

        Args:
            y_predicc (array-like): Predicciones realizadas 
            por el modelo.
            y_validacion (array-like): Etiquetas reales 
            correspondientes a los datos de validación.

        Returns:
            tuple: Una tupla con los siguientes elementos:
                - f1 (float): Puntaje F1 promedio (micro).
                - reporte (str): Reporte detallado de clasificación.
                - matriz_conf (array[array]): Matriz de confusión.
        """

        f1 = f1_score(y_validacion, y_predicc, average='micro')
        reporte = classification_report(y_validacion, y_predicc)
        matrizConf = confusion_matrix(y_validacion, y_predicc)

        return f1, reporte, matrizConf



