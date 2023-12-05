#Question 4
# importing Qiskit
from qiskit import IBMQ, Aer
#from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, transpile
from qiskit_textbook.problems import dj_problem_oracle
# import basic plot tools
from qiskit.visualization import plot_histogram

from qiskit_textbook.problems import dj_problem_oracle
oracle = dj_problem_oracle(1)
oracle.name = " Oracle"

n = 4
dj_circuit = QuantumCircuit(n+1, n)

for qubit in range(n):
    dj_circuit.h(qubit)

dj_circuit.x(n)
dj_circuit.h(n)

dj_circuit.append(oracle, range(n+1))

for qubit in range(n):
    dj_circuit.h(qubit)
dj_circuit.barrier()

for i in range(n):
    dj_circuit.measure(i, i)

print(dj_circuit.draw())
