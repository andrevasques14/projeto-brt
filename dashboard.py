import streamlit as st
import pandas as pd
import time
import math

st.set_page_config(page_title="Monitoramento BRT Metropolitano", layout="wide")
st.title("Painel de controle linha M101 - Ver-o-Peso")

placeholder = st.empty()

# Função para calcular distância simples entre dois pontos (x1, y1) e (x2, y2)
def calcular_distancia(p1, p2):
    # p1 e p2 são strings vindas do CSV como "(x, y)"
    # Precisamos converter de volta para números
    try:
        coord1 = eval(p1)
        coord2 = eval(p2)
        return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
    except:
        return 1000 # Caso dê erro, assume distância grande

while True:
    try:
        df = pd.read_csv("dados_brt.csv")
        df['ID'] = df['ID'].str.replace('.', '', regex=False)
        
        with placeholder.container():
            # 1. Indicadores
            col1, col2, col3 = st.columns(3)
            col1.metric("Frota Ativa", len(df))
            col2.metric("Vel. Média", f"{df['Velocidade'].mean():.1f} km/h")
            
            # 2. Lógica de Headway (Distância entre os carros)
            alertas_comboio = []
            if len(df) > 1:
                # Comparamos cada ônibus com o que vem logo atrás dele na tabela
                for i in range(len(df) - 1):
                    dist = calcular_distancia(df.iloc[i]['Posicao'], df.iloc[i+1]['Posicao'])
                    if dist < 50: # Se estiverem a menos de 50 metros
                        alertas_comboio.append(f"⚠️ **COMBOIO DETECTADO:** {df.iloc[i]['ID']} e {df.iloc[i+1]['ID']} estão a {dist:.1f}m!")

            # Exibe alertas de comboio se existirem
            if alertas_comboio:
                for alerta in alertas_comboio:
                    st.error(alerta)
            else:
                st.success("✅ Distanciamento entre veículos está adequado.")

            st.divider()

            # 3. Velocímetros Visuais
            cols = st.columns(5)
            for i, row in df.iterrows():
                with cols[i % 5]:
                    st.write(f"**{row['ID']}**")
                    st.progress(min(float(row['Velocidade']) / 80, 1.0))
                    st.caption(f"{row['Velocidade']:.1f} km/h")

            st.divider()
            st.subheader("📋 Telemetria em Tempo Real")
            st.dataframe(df, use_container_width=True)
            
    except Exception as e:
        st.warning(f"Aguardando dados... {e}")
    
    time.sleep(1)