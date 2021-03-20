from stockfish import Stockfish

import flask

# stockfish = Stockfish("./stockfish_13_win_x64_bmi2")
# stockfish = Stockfish("./stockfish_13_win_x64_bmi2")
stockfish = Stockfish("./stockfish_13_win_x64_bmi2", parameters={"Ponder": "true", "UCI_Chess960":"true","Threads": 3, "Minimum Thinking Time": 30, "Write Debug Log": "true"})
# stockfish.set_fen_position("1n4r1/2N2N2/2k5/3p3p/1p1p2B1/1n6/1K6/8")

# stockfish.set_position(["f2f4", "e7e6", "g2g4"])
stockfish.set_depth(15)
# stockfish.set_fen_position("1n4r1/2N2N2/2k5/3p3p/1p1p2B1/1n6/1K6/8 b")
# stockfish.set_fen_position("8/1p6/RP2p3/N1P1p3/1k2B1Q1/2N1K3/8/B1R5")

nejlepsiTah = stockfish.get_best_move()
# print(stockfish.get_board_visual())
# print(stockfish.get_fen_position())

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return '<h1>Test nejlepsi tah ze zakladniho asdffsda</h1>' + '<br>' + stockfish.get_best_move()


# A route to return all of the available entries in our catalog.
@app.route('/api/nejlepsiTah', methods=['GET'])
def api_all():
	if 'id' in request.args:
		id = request.args['id']

	else:
		return "Error: No id field provided. Please specify an id."

	# Create an empty list for our results
	results = []

	# Loop through the data and match results that fit the requested ID.
	# IDs are unique, but other fields might return many results

	# Use the jsonify function from Flask to convert our list of
	# Python dictionaries to the JSON format.
	# stockfish.set_fen_position(id)
	return stockfish.get_best_move()

app.run()
