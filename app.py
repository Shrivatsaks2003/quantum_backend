from flask import Flask, jsonify
from experiments import (
    quantum_coin_flip,
    quantum_rng,
    entanglement_experiment,
    teleportation_experiment,
    bloch_state
)
from flask import request



app = Flask(__name__)


@app.route("/coinflip", methods=["POST"])
def coinflip():

    data = request.get_json()
    shots = data.get("shots", 1)

    return jsonify(quantum_coin_flip(shots))



@app.route("/qrng", methods=["POST"])
def qrng():

    data = request.get_json()
    bits = data.get("bits", 1)

    return jsonify({"random_bits": quantum_rng(bits)})


@app.route("/entanglement", methods=["POST"])
def entanglement():

    data = request.get_json()
    shots = data.get("shots", 100)

    return jsonify(entanglement_experiment(shots))


@app.route("/teleportation", methods=["POST"])
def teleportation():

    data = request.get_json()
    initial_state = data.get("initial_state", 0)
    shots = data.get("shots", 100)

    return jsonify(teleportation_experiment(initial_state, shots))


@app.route("/bloch", methods=["POST"])
def bloch():

    data = request.get_json()
    gate = data.get("gate", "H")

    return jsonify({"statevector": bloch_state(gate)})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
