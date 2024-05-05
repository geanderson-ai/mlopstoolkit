# Importações necessárias
import prefect
from prefect import flow, task
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Tarefa para carregar os dados
@task
def load_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y

# Tarefa para dividir os dados em treino e teste
@task
def split_data(X, y):
    return train_test_split(X, y, test_size=0.3, random_state=42)

# Tarefa para padronizar os dados
@task
def preprocess_data(X_train, X_test):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test

# Tarefa para treinar o modelo
@task
def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

# Tarefa para avaliar o modelo
@task
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=datasets.load_iris().target_names)
    return accuracy, report

# Fluxo principal
@flow
def ml_pipeline():
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train, X_test = preprocess_data(X_train, X_test)
    model = train_model(X_train, y_train)
    accuracy, report = evaluate_model(model, X_test, y_test)
    
    prefect.get_run_logger().info(f"Accuracy: {accuracy:.2f}")
    prefect.get_run_logger().info("Classification Report:")
    prefect.get_run_logger().info(report)

# Executar o fluxo
if __name__ == "__main__":
    ml_pipeline()
