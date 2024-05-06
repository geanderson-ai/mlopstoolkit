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
