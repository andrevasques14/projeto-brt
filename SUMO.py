import os
import sys
import traci

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Por favor, configure a variável 'SUMO_HOME'")

sumo_binary = "sumo-gui"
caminho_config = r"C:\Users\André\Documents\projeto-brt\belem.sumocfg"
sumo_cmd = [sumo_binary, "-c", caminho_config]

try:
    traci.start(sumo_cmd)
    print("Conectado ao SUMO com sucesso!")

    step = 0
    while step < 1000:
        traci.simulationStep()
        step += 1

    traci.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")