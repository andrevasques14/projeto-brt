import streamlit as st
import pandas as pd
import time

# 1. Configuração da Página
st.set_page_config(page_title="Gestão de Frota", layout="wide")
st.title("Monitoramento em Tempo Real")

placeholder = st.empty()

# 2. O Motor do Dashboard
while True:
    try:
        df = pd.read_csv("dados_brt.csv")
        
        with placeholder.container():
            # --- ALERTA DE PROXIMIDADE (O que você pediu!) ---
            if len(df) > 1:
                # Calcula a distância entre os ônibus (Exemplo simples por posição X)
                distancias = df['Posicao_X'].diff().abs().dropna()
                if (distancias < 50).any():
                    st.error("🚨 ALERTA: Ônibus muito próximos! Risco de comboio.")
                else:
                    st.success("✅ Distanciamento entre veículos está adequado.")

            # --- PARTE A: Velocímetros ---
            st.subheader("Dados da Frota")
            cols = st.columns(5)
            for i, row in df.iterrows():
                # AJUSTE DO PREFIXO: Transformando 'veh679' em 'B67.9'
                id_original = str(row['ID'])
                if 'B' in id_original:
                    # Pega os números e coloca o ponto antes do último dígito
                    num = id_original.replace('B', '')
                    id_formatado = f"B{num[:-1]}.{num[-1]}" if len(num) > 1 else id_original
                else:
                    id_formatado = id_original

                with cols[i % 5]:
                    st.write(f"**{id_formatado}**")
                    st.progress(min(float(row['Velocidade']) / 80, 1.0))
                    st.caption(f"{row['Velocidade']:.1f} km/h")

            st.divider()

            # --- PARTE B: Tabela de Telemetria ---
            st.subheader("Monitoramento em Tempo Real")
            st.dataframe(df, width="stretch")

            # --- PARTE C: Gráfico de Histórico e Lotação ---
            st.markdown("---")
            st.subheader("Análise de Desempenho (Histórico)")
            try:
                df_hist = pd.read_csv("historico_brt.csv")
                if not df_hist.empty:
                    chart_data = df_hist.pivot(index='Registro de horário', columns='ID', values='Velocidade')
                    chart_data = chart_data.interpolate(method='linear').fillna(0)
                    st.line_chart(chart_data.tail(100))
                    
                    media_lotacao = df_hist['Lotação'].mean()
                    st.metric("Lotação Média da Frota", f"{media_lotacao:.1f}%")
            except:
                st.info("Aguardando dados históricos...")

        time.sleep(1)

    except Exception as e:
        st.warning("Aguardando conexão com o simulador...")
        time.sleep(2)