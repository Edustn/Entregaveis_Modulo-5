from pydobot.pydobot import Dobot


dobot = Dobot(port="COM9") 

# Configuração da velocidade
dobot.speed(250)

while True:
    entrada = input("De um comando: ").split()
    
    if entrada[0] == "x":
        break

    if (len(entrada) == 3 and entrada[0].lower() == "mover"):
        
        eixo = entrada[1].lower()
        distancia = float(entrada[2])

        if eixo == "x":
            dobot.move_to(distancia, 0, 0, 0)
        elif eixo == "y":
            dobot.move_to(0, distancia, 0, 0)
        elif eixo == "z":
            dobot.move_to(0, 0, distancia, 0)

    else:
        if(entrada[0] == "home"):
            dobot.move_to(242.23,0,151.35, 0)
            print("home")
        
        elif(entrada[0] == "ligar"):
            dobot._set_end_effector_suction_cup(True)
        
        elif(entrada[0] == "desligar"):
            dobot._set_end_effector_suction_cup(False)

        elif(entrada[0] == "atual"):
            print(f'Posição atual do robô: {dobot.pose()}')

    entrada = []
dobot.close()
