from geopy.distance import geodesic

estacao_sao_bras = (-1.4483, -48.4670)
estacao_castanheira = (-1.4048, -48.4315)

posicao_atual_onibus = (-1.4229, -48.4497)

distancia = geodesic(posicao_atual_onibus, estacao_castanheira).kilometers

print("-" * 30)
print(f"RASTREAMENTO BRT")
print("-"  * 30)
print(f"O ônibus está à {distancia:.2f} km  da Estação Castanheira")

if distancia < 0.5:
    print("STATUS: o ônibus está chegando!")
else:
    print ("STATUS: Ônibus em trânsito normal")