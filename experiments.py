from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector



def quantum_coin_flip(shots):

    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(qc, shots=shots)
    result = job.result()

    return result.get_counts()

def quantum_rng(bits):

    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    backend = Aer.get_backend("qasm_simulator")

    random_bits = []

    for _ in range(bits):
        job = backend.run(qc, shots=1)
        result = job.result()
        counts = result.get_counts()
        bit = list(counts.keys())[0]
        random_bits.append(bit)

    return random_bits


def entanglement_experiment(shots):

    qc = QuantumCircuit(2, 2)

    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(qc, shots=shots)
    result = job.result()

    return result.get_counts()

def teleportation_experiment(initial_state, shots):

    qc = QuantumCircuit(3, 3)

    if initial_state == 1:
        qc.x(0)

    qc.h(1)
    qc.cx(1, 2)

    qc.cx(0, 1)
    qc.h(0)

    qc.measure(0, 0)
    qc.measure(1, 1)

    qc.cx(1, 2)
    qc.cz(0, 2)

    qc.measure(2, 2)

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()

    # Extract Bob's qubit (leftmost bit)
    bob_counts = {"0": 0, "1": 0}

    for state, count in counts.items():
        bob_bit = state[0]   # q2
        bob_counts[bob_bit] += count

    return bob_counts


def bloch_state(gate):

    qc = QuantumCircuit(1)

    if gate == "H":
        qc.h(0)
    elif gate == "X":
        qc.x(0)
    elif gate == "Z":
        qc.z(0)

    state = Statevector.from_instruction(qc)

    return [
        {"real": float(val.real), "imag": float(val.imag)}
        for val in state.data
    ]

