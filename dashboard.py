import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Monitoramento BRT Metropolitano", layout="wide")

st.title("Painel de Controle BRT Metropolitano")

# Espaço para os indicadores
placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("dados_brt.csv")
        df['ID'] = df['ID'].str.replace('.', '')
        
        with placeholder.container():
            # 1. Indicadores Principais
            col1, col2, col3 = st.columns(3)
            col1.metric("M101 - Ver-o-Peso", len(df))
            col2.metric("Velocidade Média", f"{df['Velocidade'].mean():.2f} km/h")
            col3.metric("Status", "CONECTADO", delta_color="normal")

            st.divider()

            # 2. Velocímetros (Gauges) dos Ônibus
            st.subheader("Velocidade por Veículo")
            
            # Cria colunas dinâmicas (5 por linha para não ficar apertado)
            col_velocimetros = st.columns(5)
            
            for i, row in df.iterrows():
                with col_velocimetros[i % 5]:
                    # Exibe o prefixo e uma barra de progresso como "velocímetro"
                    valor_vel = min(float(row['Velocidade']) / 80, 1.0) # Normaliza para 80km/h max
                    st.write(f"**{row['ID']}**")
                    st.progress(valor_vel)
                    st.caption(f"{row['Velocidade']:.1f} km/h")

            st.divider()

            # 3. Tabela Detalhada
            st.subheader("Dados linha M101")
            st.dataframe(df, use_container_width=True)
            
    except Exception:
        st.warning("Aguardando sinal dos rastreadores...")
    
    time.sleep(1)