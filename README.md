# 🛡️ CustomerPulse AI - Previsor de Churn

**Projeto de Ciência de Dados Júnior**  
Previsor de cancelamento de clientes (Churn Prediction)

![Dashboard Streamlit](https://via.placeholder.com/800x400?text=CustomerPulse+AI+Dashboard)

---

## 🎯 Sobre o Projeto

Desenvolvi um modelo de Machine Learning para prever quais clientes têm alto risco de cancelar o serviço, junto com um **dashboard interativo** feito em Streamlit.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 3.12+
- **Pandas** + **NumPy**
- **Scikit-learn** (Random Forest)
- **Seaborn** / **Matplotlib** (visualizações)
- **Streamlit** (Dashboard web)
- **Joblib** (salvar modelo)

---

## 📊 Principais Resultados

- **Acurácia do modelo**: ~54% (dados sintéticos)
- Variável **mais importante**: **Salário**
- Segunda mais importante: **Tempo como cliente**

---

## 🚀 Como Executar o Projeto

```bash
# 1. Entre na pasta
cd ~/Desktop/CustomerPulseAI

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode o dashboard
streamlit run app.py