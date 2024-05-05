# train.py

import bentoml
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Carregue os dados
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Treine um modelo simples
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avalie o modelo
score = model.score(X_test, y_test)
print(f"Modelo treinado com acurácia: {score:.2f}")

# Salve o modelo com BentoML
bentoml.sklearn.save_model("iris_classifier", model)
