# 🛡️ CustomerPulse AI - Previsor de Churn

**Projeto de Ciência de Dados Júnior**  
Previsor de cancelamento de clientes (Churn Prediction)

![Dashboard Streamlit](https://via.placeholder.com/800x400?text=Dashboard+CustomerPulse)

---

## 🎯 Sobre o Projeto

Desenvolvi um modelo de Machine Learning para prever quais clientes têm risco de cancelar o serviço, além de um dashboard interativo para facilitar o uso.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 3.12+
- **Pandas** + **NumPy** (manipulação de dados)
- **Scikit-learn** (Random Forest)
- **Seaborn / Matplotlib** (visualizações)
- **Streamlit** (dashboard web)
- **Joblib** (salvar modelo)

---

## 📊 Principais Resultados

- **Acurácia do modelo**: ~54% (dados sintéticos)
- Variável mais importante: **Salário**
- Segunda mais importante: **Tempo como cliente**

---

## 🚀 Como Executar o Projeto

```bash
# 1. Entre na pasta do projeto
cd ~/Desktop/CustomerPulseAI

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode o dashboard
streamlit run app.py