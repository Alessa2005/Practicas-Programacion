from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from .Clasificador import Clasificador

class Comparador:
    """
    Clase para comparar múltiples clasificadores utilizando 
    datos de entrenamiento y validación.

    Atributos:
        x_train: Datos de entrada para entrenamiento.
        y_train: Etiquetas correspondientes a los datos 
        de entrenamiento.
        x_valid: Datos de entrada para validación.
        y_valid: Etiquetas correspondientes a los datos 
        de validación.
    """
        
    def __init__(self, x_train, y_train, x_valid, y_valid):

        self.x_train = x_train
        self.x_valid = x_valid
        self.y_train = y_train
        self.y_valid = y_valid

    def comparaClasificadores(self):
        """
        Compara diferentes clasificadores en términos de f1-score,
        reporte de clasificación y matriz de confusión.

        Los clasificadores evaluados son:
        - Regresión Logística
        - K-Nearest Neighbors
        - SVM (Support Vector Machines)
        - Árbol de Decisión
        - Random Forest

        Returns:
            list[dict]: Lista de diccionarios con los resultados 
            de evaluación de cada clasificador. Cada diccionario contiene:
                - "Modelo": Nombre del clasificador.
                - "f1Score": Puntaje f1 obtenido.
                - "Reporte": Reporte detallado de clasificación.
                - "Matriz_de_confusión": Matriz de confusión 
                generada.
        """

        scores = []

        clasificadores = [
            ("Regresión Logística", LogisticRegression(max_iter=1000)),
            ("K-Nearest Neighbors", KNeighborsClassifier()),
            ("SVM", SVC(class_weight='balanced')),
            ("Árbol de Decisión", DecisionTreeClassifier()),
            ("Random Forest", RandomForestClassifier())
        ]

        for nombre, instancia in clasificadores:
            c = Clasificador(instancia)
            c.entrenar(self.x_train, self.y_train)
            prediccion = c.predecir(self.x_valid)
            f1, reporte, matrizC = c.evaluar(prediccion, self.y_valid)

            scores.append({
                "Modelo" : nombre,
                "f1Score" : f1,
                "Reporte": reporte,
                "Matriz_de_confusión" : matrizC
            })
        
        return scores

    def ordenar(self, scores):
        """
        Ordena los clasificadores evaluados en orden 
        descendente por su f1-score.

        Args:
            scores (list[dict]): Lista de diccionarios 
            con los resultados de evaluación.

        Returns:
            list[dict]: Lista de diccionarios ordenada 
            por f1-score en orden descendente.
        """
        ordenados = sorted(scores, key=lambda x: x.get("f1Score", 0) if x.get("f1Score") is not None else 0,
                           reverse=True)
        return ordenados

    

