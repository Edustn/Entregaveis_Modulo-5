from flask import Flask, render_template, request
from flask_cors import CORS
from tinydb import TinyDB
from  pydobot import Dobot
from VerficarPortas import RobotFinder


app = Flask(__name__)

db = TinyDB('logs.json')

CORS(app)

try:
    robot_instance = Dobot(port="COM9")
    robot_instance.speed(250)
except:
    robot_instance = None

print(robot_instance)



# Retorna o index.html
@app.route('/')
def index():
    if robot_instance is None:
        return'<h1> Voce so pode entrar na rota /log, pois o robô não está conectado!<h1>'
    return render_template('index.html')

if robot_instance is not None:

    @app.route('/print')
    def printar():
        db.insert({'log':'GET na /print'})
        return '<h1>L</h1>'
    
    @app.route('/posicao')
    def posicao():
        db.insert({'log': 'GET da posicao do robô'})
        return f'<h1>{robot_instance.pose()}<h1>'
    
    @app.route('/mover', methods=['GET','POST'])
    def mover():
        if request.method == 'POST':
            x = request.args.get('x')
            y = request.args.get('y')
            z = request.args.get('z')
            r = request.args.get('r')
            db.insert({'log': 'POST as posicoes'})
            robot_instance.move_to(float(x),float(y),float(z),float(r))
            return f'<h1>X: {x}, Y: {y}, Z: {z}</h1>'





@app.route('/log')
def exibir_logs():
    logs = db.all()
    print(logs)
    return render_template('logs.html', logs=logs)
   

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
