import pandas as pd # A biblioteca que você usou para aprender data analysis
from geopy.distance import geodesic

# 1. Simulação de como vamos ler sua tabela de testes em Julho
# df = pd.read_csv("sua_tabela_brt.csv") 

# 2. Mantendo a lógica de ontem, mas organizando para o Networking
estacao_alvo = (-1.4106, -48.4412) # Estação alvo fixa
velocidade_media = 15

def calcular_status_headway(dist_bus_1, dist_bus_2):
    headway_km = abs(dist_bus_1 - dist_bus_2)
    tempo_min = (headway_km / velocidade_media) * 60
    
    if tempo_min <= 2:
        return f"🚨 CRÍTICO: Comboio ({tempo_min:.1f} min)"
    elif tempo_min <= 5:
        return f"✅ NORMAL: ({tempo_min:.1f} min)"
    else:
        return f"📢 ALERTA: Buraco na linha ({tempo_min:.1f} min)"


# Exemplo de teste rápido no VS Code
dist_A = 2.5 # Simulando que veio da tabela
dist_B = 2.8 # Simulando que veio da tabela

print(f"STATUS DA LINHA: {calcular_status_headway(dist_A, dist_B)}")