import csv
from flask import Flask, request

app = Flask(__name__)


@app.route('/addGame', methods=['POST'])
def adicionarJogo():
    with open('jogos.csv', 'a', newline='') as games:
        writer = csv.writer(games, delimiter=',')
        game = request.json

        gameAdded = [game['id'], game['name'],
                     game['release'], game['platforms']]
        writer.writerow(gameAdded)

    return 'OK'


@app.route('/searchGame/<id>', methods=['GET'])
def buscarJogoPorId(id):
    with open('jogos.csv', 'r', encoding='utf-8') as games:
        table = csv.reader(games, delimiter=',')
        for line in table:
            if (line[0] == id):
                game = {
                    "id": line[0],
                    "name": line[1],
                    "release": line[2],
                    "platforms": line[3]
                }

                return game

    return 'Jogo não encontrado!'


@app.route('/deleteGame/<id>', methods=['DELETE'])
def deletarJogoPorId(id):
    with open('jogos.csv', 'r', encoding='utf-8') as games:
        reader = csv.reader(games, delimiter=',')
        data = list(reader)

    with open('jogos.csv', 'w', newline='') as games:
        writer = csv.writer(games, delimiter=',')

        for item in data:
            gameId, name, release, platforms = item

            if gameId != id:
                writer.writerow(item)

    return 'OK'
