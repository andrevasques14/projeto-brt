from geopy.distance import geodesic
posicao_onibus = (-1.4297, -48.4541)
posicao_estacao = (-1.4106, -48.4412)

distancia_km = geodesic(posicao_onibus, posicao_estacao).kilometers
velocidade_media = 15

tempo_estimado_min = (distancia_km/velocidade_media)*60
minutos_inteiros = int(tempo_estimado_min)
#segundos = int ((tempo_estimado_min - minutos_inteiros)*60)

print("-"*30)
print(f"M101 SENTIDO > MARITUBA")
print("-"*30)
#print(f"PREVISÃO DE CHEGADA:{minutos_inteiros} min {segundos} seg")
print(f"PREVISÃO DE CHEGADA:{minutos_inteiros:.1f} minutos")
print("-"*30)

tempo_planejado = 2
atraso = tempo_estimado_min - tempo_planejado

# if tempo_estimado_min > tempo_planejado:
  # atraso_total_seg = int ((tempo_estimado_min - tempo_planejado) *60)
  # min_atraso = atraso_total_seg // 60
  #seg_atraso = atraso_total_seg % 60
  # print(f"Ônibus com {min_atraso}min {seg_atraso} seg de atraso!")
  # print(f"Ônibus com {min_atraso:.1f} minutos de atraso!")
# else:
  # print("No horário")

if atraso <= 0:
  print("✅No horário")
elif atraso <= 2:
  print(f"🟡Atraso leve({atraso:.1f} min)")
elif atraso <= 5:
  print(f"🟠Atraso moderado ({atraso:.1f} min)")
else:
  print(f"🚨Atraso crítico ({atraso:.1f} min. Formação de comboio)")