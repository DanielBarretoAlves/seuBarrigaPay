from flask import Flask, render_template, request, redirect
from flask import Flask

def index():
    pronto = {}
    pronto['cliente.ID'] = 99999


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/dono", methods=["GET"])
def dono():
    return render_template('dono.html')


@app.route('/manage_game', methods=['POST'])
    def manage_game():
    start = request.form['action'] == 'Start'
    game_id = request.form['game_id']

    if start:
        start_game(game_id)
    else:
        stop_game(game_id)
    return redirect(url_for('index'))