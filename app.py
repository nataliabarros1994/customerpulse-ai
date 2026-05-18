import streamlit as st
import pandas as pd
import joblib
import os

# ==================== TÍTULO ====================
st.title("🛡️ CustomerPulse AI - Previsor de Churn")
st.write("Preveja se um cliente vai cancelar o serviço")

# ==================== CARREGAR MODELO ====================
model_path = 'modelo_churn_randomforest.pkl'

if os.path.exists(model_path):
    modelo = joblib.load(model_path)
    st.success("✅ Modelo carregado com sucesso!")
else:
    st.error("❌ Modelo não encontrado!")
    st.stop()

# ==================== INPUTS ====================
idade = st.slider("Idade", 18, 70, 35)
salario = st.number_input("Salário (R$)", 1500, 15000, 4500)
tempo_cliente = st.slider("Tempo como cliente (meses)", 1, 120, 12)
compras = st.slider("Compras nos últimos 3 meses", 0, 50, 8)

# ==================== BOTÃO ====================
if st.button("🔮 Prever Cancelamento"):
    dados = pd.DataFrame({
        "idade": [idade],
        "salario": [salario],
        "tempo_cliente": [tempo_cliente],
        "compras": [compras]
    })
    
    pred = modelo.predict(dados)[0]
    prob = modelo.predict_proba(dados)[0][1]
    
    if pred == 1:
        st.error(f"🚨 ALTO RISCO DE CANCELAMENTO ({prob:.1%})")
    else:
        st.success(f"✅ Baixo risco de cancelamento ({prob:.1%})")