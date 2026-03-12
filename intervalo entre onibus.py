from geopy.distance import geodesic

posicao_onibus_B690 = (-1.438482, -48.460032)
posicao_onibus_B688 = (-1.438286, -48.456040)

estacao_alvo = (-1.448311, -48.467079)

distancia_B690 = geodesic(posicao_onibus_B690, estacao_alvo).kilometers
distancia_B688 = geodesic(posicao_onibus_B688, estacao_alvo).kilometers

headway_km = abs(distancia_B690 - distancia_B688)

velocidade_media = 40
headway_minutos = (headway_km / velocidade_media) * 60

print("-"*40)
print("INTERVALO ENTRE ÔNIBUS")
print("-"*40)
print(f"DISTÂNCIA ENTRE ÔNIBUS B688 E B690:{headway_km:.2f} km")
print(f"INTERVALO DE TEMPO:{headway_minutos:.1f} minutos")

meta_intervalo = 5.0

if headway_minutos < 2.0:
  print("🚨 ALERTA: Risco de Comboio! B688 está muito próximo.")
elif headway_minutos > 8.0:
    print("📢 ALERTA: Buraco na linha! Grande intervalo entre os carros.")
else:
    print("✅ STATUS: Intervalo dentro do planejado.")