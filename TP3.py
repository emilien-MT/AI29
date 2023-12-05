r"""°°°
## Algo de Deutsh-Josza
Permet d'évaluer une fonction, constante ou équilibrée.
Si on a 000, c'est contant, sinon c'est équilibré.
3 portes H vers un oracle. Si l'oracle n'est composé d'aucune porte : ça sera toujours constant.
-> changer l'oracle pour qu'il y ait toujours 1.
On ajoute X.

Oracle équilibré : la moitié donne 0 et l'autre donne 1.

°°°"""
# |%%--%%| <LbSGBVlcjB|gds269LYWv>

from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_bloch_multivector
from qiskit.providers.aer import AerSimulator
from qiskit.quantum_info import *


circuit = QuantumCircuit(3, 3)
circuit.h(1)
circuit.h(2)
circuit.h(0)

circuit.draw('mpl')

# |%%--%%| <gds269LYWv|WtQWAFax7z>

# Oracle équilibré
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer
#from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, transpile

# import basic plot tools
from qiskit.visualization import plot_histogram

# set the length of the n-bit input string. 
n = 3

balanced_oracle = QuantumCircuit(n+1)
b_str = "010"

# Place H-gates
for qubit in range(len(b_str)):
    balanced_oracle.h(qubit)
balanced_oracle.h(n)
balanced_oracle.x(1)

# Use barrier as divider
balanced_oracle.barrier()

balanced_oracle.barrier()

# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Show oracle
balanced_oracle.draw('mpl')


# |%%--%%| <WtQWAFax7z|ywuzWNYF6E>



# |%%--%%| <ywuzWNYF6E|XxAjIZQUCF>

# Question 3 :

# importing Qiskit
from qiskit import IBMQ, Aer
#from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, transpile

# import basic plot tools
from qiskit.visualization import plot_histogram

balanced_oracle = QuantumCircuit(n+1)
b_str = "101"

# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Use barrier as divider
balanced_oracle.barrier()

# Controlled-NOT gates
for qubit in range(n):
    balanced_oracle.cx(qubit, n)

balanced_oracle.barrier()

# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Show oracle
balanced_oracle.draw()

dj_circuit = QuantumCircuit(n+1, n)

# Apply H-gates
for qubit in range(n):
    dj_circuit.h(qubit)

# Put qubit in state |->
dj_circuit.x(n)
dj_circuit.h(n)

# Add oracle
dj_circuit = dj_circuit.compose(balanced_oracle)

# Repeat H-gates
for qubit in range(n):
    dj_circuit.h(qubit)
dj_circuit.barrier()

# Measure
for i in range(n):
    dj_circuit.measure(i, i)
# Display circuit
dj_circuit.draw('mpl')


# use local simulator
aer_sim = Aer.get_backend('aer_simulator')
results = aer_sim.run(dj_circuit).result()
answer = results.get_counts()

plot_histogram(answer)





# |%%--%%| <XxAjIZQUCF|HagqXnGJKu>

#Question 4
# importing Qiskit
from qiskit import IBMQ, Aer
#from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, transpile
from qiskit_textbook.problems import dj_problem_oracle
# import basic plot tools
from qiskit.visualization import plot_histogram

balanced_oracle = QuantumCircuit(n+1)
oracle = dj_problem_oracle(1)
b_str = "101"

# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Use barrier as divider
balanced_oracle.barrier()

# Controlled-NOT gates
for qubit in range(n):
    balanced_oracle.cx(qubit, n)

balanced_oracle.barrier()

# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Show oracle
balanced_oracle.draw()

dj_circuit = QuantumCircuit(n+1, n)

# Apply H-gates
for qubit in range(n):
    dj_circuit.h(qubit)

# Put qubit in state |->
dj_circuit.x(n)
dj_circuit.h(n)

# Add oracle
dj_circuit = dj_circuit.compose(balanced_oracle)

# Repeat H-gates
for qubit in range(n):
    dj_circuit.h(qubit)
dj_circuit.barrier()

# Measure
for i in range(n):
    dj_circuit.measure(i, i)
# Display circuit
dj_circuit.draw()



# |%%--%%| <HagqXnGJKu|eY7zIahfX5>


