
# alugueis-justos-sp
Análise e previsão de preços de aluguéis justos na Grande São Paulo (2019–2030)
=======
# 🏙️ Aluguéis Justos SP — API de Previsão de Preços de Aluguéis

## 📖 Descrição
API desenvolvida em **FastAPI** que prevê se o preço de um aluguel na Grande São Paulo é justo, 
e também faz **projeções de preço até 2030** com base em uma taxa anual de crescimento.

---

## 🚀 Endpoints Principais

### `POST /predict`
Previsão de preço atual com base nas características do imóvel.

#### Exemplo de corpo JSON:
```json
{
  "Condo": 1000,
  "Size": 120,
  "Rooms": 3,
  "Toilets": 2,
  "Suites": 1,
  "Parking": 1,
  "Elevator": 1,
  "Furnished": 0,
  "Swimming_Pool": 1,
  "New": 0,
  "District": "Pinheiros",
  "Negotiation_Type": "rent",
  "Property_Type": "apartment",
  "Latitude": -23.561084,
  "Longitude": -46.685139
}
Exemplo de resposta esperada:
{
  "preco_previsto": 36275.74,
  "status": "ok"

 ## 📦 Instalação

### Instale as dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Execute o servidor
```bash
python -m uvicorn api.main_app:app --reload --host 0.0.0.0 --port 8000
```

### 4️⃣ Acesse a documentação interativa (Swagger)

👉 http://127.0.0.1:8000/docs

---

## 🧠 Modelo Preditivo

Treinado com dados reais de aluguéis de 2019 na Grande São Paulo, o modelo utiliza algoritmos de Machine Learning para prever o preço justo de locação com base em variáveis estruturais e geográficas.

---

## 👨‍💻 Autor

**Bernardo Carvalho**  
Economista | Cientista de Dados | Desenvolvedor de Soluções Tech

---

## 📦 Dependências

- FastAPI
- Uvicorn
- Pandas
- NumPy
- Joblib
- Scikit-Learn

---

## ✅ Resumo

Esse README.md é apenas documentação explicativa. Serve para quem acessar meu projeto no GitHub entender o que a API faz e como executá-la.

