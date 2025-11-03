from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title="Aluguéis Justos SP", version="2.0")

# Carregar o modelo treinado
model = joblib.load("model.pkl")

# Modelo de entrada
class InputData(BaseModel):
    Condo: float
    Size: float
    Rooms: int
    Toilets: int
    Suites: int
    Parking: int
    Elevator: int
    Furnished: int
    Swimming_Pool: int
    New: int
    District: str
    Negotiation_Type: str
    Property_Type: str
    Latitude: float
    Longitude: float

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    preco_previsto = model.predict(df)[0]
    return {"preco_previsto": round(preco_previsto, 2), "status": "ok"}

@app.post("/predict_future")
def predict_future(data: InputData, annual_growth_rate: float = 0.035):
    try:
        # Transforma a entrada em DataFrame
        df = pd.DataFrame([data.dict()])

        # Converte strings para o mesmo formato usado no treino
        df_encoded = pd.get_dummies(df)

        # Garante que as colunas estejam alinhadas com o modelo
        model_features = model.feature_names_in_
        for col in model_features:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        df_encoded = df_encoded[model_features]

        # Faz a predição base (conversão para float nativo do Python)
        preco_base = float(model.predict(df_encoded)[0])

        # Projeta crescimento até 2030
        anos = list(range(2025, 2031))
        previsoes = []
        preco_atual = preco_base

        for ano in anos:
            preco_atual *= (1 + annual_growth_rate)
            previsoes.append({
                "ano": ano,
                "preco_estimado": round(float(preco_atual), 2)
            })

        return {
            "preco_base_2025": round(preco_base, 2),
            "previsao_ate_2030": previsoes,
            "status": "ok"
        }

    except Exception as e:
        # Loga o erro e retorna resposta tratada
        return {"erro": str(e), "status": "falha"}
