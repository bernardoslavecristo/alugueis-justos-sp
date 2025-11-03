import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor
import joblib

print("🚀 Iniciando o treinamento do modelo com base real de São Paulo...")

# ===============================
# 1. Carregar a base de dados
# ===============================
try:
    df = pd.read_csv("data/alugueis_sp_2019.csv")
except FileNotFoundError:
    print("⚠️ Arquivo 'data/alugueis_sp_2019.csv' não encontrado.")
    exit()

print(f"✅ Dados carregados: {df.shape[0]} linhas e {df.shape[1]} colunas")

# ===============================
# 2. Limpeza e pré-processamento
# ===============================

# Renomear colunas para padrão minúsculo e sem espaços
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remover registros com preço ausente ou zero
df = df[df['price'] > 0]

# Separar variável alvo e features
y = df['price']
X = df.drop(columns=['price'])

# Converter variáveis categóricas em dummies
X = pd.get_dummies(X, drop_first=True)

print(f"✅ Features finais: {X.shape[1]} colunas após dummies")

# ===============================
# 3. Dividir base de treino e teste
# ===============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===============================
# 4. Treinar modelo
# ===============================
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=6,
    random_state=42,
    n_jobs=-1
)

print("⚙️ Treinando modelo XGBoost...")
model.fit(X_train, y_train)

# ===============================
# 5. Avaliar modelo
# ===============================
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 Erro absoluto médio (MAE): {mae:.2f}")
print(f"📈 R²: {r2:.3f}")

# ===============================
# 6. Salvar modelo treinado
# ===============================
joblib.dump(model, "model.pkl")
print("✅ Modelo salvo como 'model.pkl'")
print("🎯 Treinamento concluído com sucesso!")
