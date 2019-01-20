# ex_1qubit_1randombit.py
# This sample generates a single random bit.

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_state_qsphere
from qiskit.tools.visualization import plot_histogram

import warnings
warnings.simplefilter("ignore")

qr = QuantumRegister(1)
circ = QuantumCircuit(qr)

# place it into superposition of 0 and 1
circ.h(qr[0])

p = circ.draw(output='mpl')
p.savefig("circ.png")

backend_sv_sim = BasicAer.get_backend('statevector_simulator')
job_sim = execute(circ, backend_sv_sim)
result_sim = job_sim.result()
quantum_state = result_sim.get_statevector(circ, decimals=3)
print(quantum_state)

p = plot_state_qsphere(quantum_state)
p.savefig("q-sphere.png")

cr = ClassicalRegister(1)
meas_circ = QuantumCircuit(qr, cr)
meas_circ.barrier(qr)
meas_circ.measure(qr, cr)
complete_circuit = circ + meas_circ

p = complete_circuit.draw(output='mpl')
p.savefig("circ-meas.png")

backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(complete_circuit, backend_sim, shots=100)
result_sim = job_sim.result()
counts = result_sim.get_counts(complete_circuit)
print(counts)

p = plot_histogram(counts)
p.savefig("plot.png")
