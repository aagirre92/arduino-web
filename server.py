import pyfirmata
from flask import Flask, render_template

app = Flask(__name__)
board = pyfirmata.Arduino('COM6')
def arduino(board=board):
    if board.digital[13].read()==1:
        board.digital[13].write(0)
    else:
        board.digital[13].write(1)

    return board.digital[13].read()

@app.route("/")
def index(board = board):
    if board.digital[13].read()==1:
        boton = "Apagar Led"
    else:
        boton = "Encender Led"
    return render_template('index.html',boton = boton)

@app.route("/control",methods=["GET","POST"])
def control():
    status = arduino()
    return str(status)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
