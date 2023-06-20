from sklearn.datasets import load_iris #conjunto de datos
from sklearn.linear_model import Perceptron #importa clase preceptron
from sklearn.model_selection import train_test_split #entrenamiento y pruebas
from sklearn.metrics import accuracy_score #calcular la Precicion del modelo

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data #atributos del conjunto de datos
y = iris.target #etiquetas

# Dividir el conjunto de datos en entrenamiento y prueba                  random_state=42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear un objeto de perceptrón
perceptron = Perceptron()

# Entrenar el perceptrón
perceptron.fit(X_train, y_train)

# Predecir las etiquetas de clase para el conjunto de prueba
y_pred = perceptron.predict(X_test)

# Calcular la precisión de las predicciones
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy*100, "%")
print("Etiquetas reales:   ", y_test)
print("Etiquetas predichas:", y_pred)