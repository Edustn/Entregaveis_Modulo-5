import serial.tools.list_ports
from pydobot import Dobot

class RobotFinder:
    def __init__(self):
        pass

    # Método para tentar conectar-se ao robô em uma porta específica
    def tentar_conectar(self, port):
        try:
            dobot = Dobot(port=port)
            if dobot.is_connected():
                print(f"Robô conectado na porta {port}.")
                return dobot  # Retorna a instância do Dobot se a conexão for bem-sucedida
            else:
                print(f"Não foi possível conectar-se ao robô na porta {port}.")
                return None
        except Exception as e:
            print(f"Erro ao tentar conectar-se ao robô na porta {port}: {e}")
            return None

    # Método para fazer a varredura por todas as portas e tentar conectar-se ao robô
    def varrer_portas(self):
        for port in serial.tools.list_ports.comports():
            print(f"Tentando conectar-se à porta {port.device}...")
            dobot = self.tentar_conectar(port.device)
            if dobot:
                return dobot  # Retorna a instância do Dobot se a conexão for bem-sucedida
        print("Nenhum robô encontrado em nenhuma porta disponível.")
        return None
