Claro, aqui está um guia completo do Passo 1 ao Passo 5 em um único documento Markdown:

```markdown
# Guia Completo: Criando um Aplicativo Básico com BentoML

Este guia vai te ensinar a criar um aplicativo básico usando BentoML, treinando e servindo um modelo de classificação de íris.

## Passo 1: Instale o BentoML e Outros Requisitos

Certifique-se de que você tem o `bentoml`, `scikit-learn`, `numpy` e `pandas` instalados:

```bash
pip install bentoml scikit-learn numpy pandas
```

## Passo 2: Treine um Modelo Simples e Salve-o com BentoML

Crie um script chamado `train.py` que treina um modelo de classificação de íris usando o `scikit-learn` e salva-o usando BentoML.

```python
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
```

Execute o script `train.py` para salvar o modelo:

```bash
python train.py
```

## Passo 3: Crie um Serviço BentoML

Crie um novo arquivo chamado `service.py` que vai definir um serviço BentoML para servir o modelo salvo.

```python
# service.py

import bentoml
from bentoml.io import JSON
import numpy as np

# Carregue o modelo salvo
iris_model = bentoml.sklearn.get("iris_classifier:latest")

# Defina um serviço BentoML
svc = bentoml.Service("iris_classifier_service", runners=[iris_model.to_runner()])

# Defina uma API para prever os dados
@svc.api(input=JSON(), output=JSON())
async def classify(input_data):
    # Prepare os dados para previsão
    data = np.array(input_data["data"]).reshape(1, -1)
    prediction = await svc.runners[0].predict.async_run(data)
    return {"prediction": int(prediction[0])}
```

## Passo 4: Servindo o Serviço BentoML

Agora, inicie o serviço executando:

```bash
bentoml serve service.py:svc
```

A API ficará disponível no endereço `http://127.0.0.1:3000/classify`.

## Passo 5: Teste o Serviço

Você pode testar o serviço usando `curl` ou criando um pequeno script Python.

### Usando `curl`:

```bash
curl -X POST "http://127.0.0.1:3000/classify" -H "Content-Type: application/json" -d '{"data": [5.1, 3.5, 1.4, 0.2]}'
```

### Usando Python:

```python
import requests

url = "http://127.0.0.1:3000/classify"
input_data = {"data": [5.1, 3.5, 1.4, 0.2]}
response = requests.post(url, json=input_data)
print(response.json())
```

### Resultado Esperado

Você deve obter um resultado semelhante ao seguinte:

```json
{
  "prediction": 0
}
```

**Classes correspondentes:**

- 0: Setosa
- 1: Versicolor
- 2: Virginica

---

E assim, você terá um aplicativo básico que utiliza BentoML para servir um modelo de classificação de íris.

```