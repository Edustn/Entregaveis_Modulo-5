import typer
from pydobot import Dobot

app = typer.Typer()

dobot = Dobot(port="COM9")
dobot.speed(250)

@app.command()
def mover(comando: str):
    """
    Move o robô na direção especificada.
    Exemplo: "mover x 100"
    """
    partes = comando.split()
    
    eixo = partes[0].lower()
    distancia = float(partes[1])

    if eixo == "x":
        dobot.move_to(distancia, 0, 0, 0)
    elif eixo == "y":
        dobot.move_to(0, distancia, 0, 0)
    elif eixo == "z":
        dobot.move_to(0, 0, distancia, 0)

@app.command()
def home():
    """
    Move o robô para a posição de origem (home).
    """
    dobot.move_to(242.23, 0, 151.35, 0)
    typer.echo("Home")

@app.command()
def ligar():
    """
    Liga o dispositivo na extremidade do efetuador.
    """
    dobot.suck(True)

@app.command()
def desligar():
    """
    Desliga a ventosa.
    """
    dobot.suck(False)

@app.command()
def atual():
    """
    Exibe a posição atual do robô.
    """
    typer.echo(f'Posição atual do robô: {dobot.pose()}')

if __name__ == "__main__":
    app()
    dobot.close()
