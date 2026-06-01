"""
Quantum Coin Flipper
--------------------
Simulates a fair coin flip using a single-qubit quantum circuit. 
A Hadamard gate places the qubit in equal superposition of |0⟩ and |1⟩. 
Measuring the qubit collapses it to either state with 50% probability.

Circuit: q0--H--M--

Dependencies: qiskit, matplotlib
"""
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# build circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# run it
shots = int(input("Enter number of shots: 1" ))
sampler = StatevectorSampler()
job = sampler.run([qc], shots = shots)
result = job.result()

# extract counts
counts = result[0].data.c.get_counts()

print("Results: ", counts)
plot_histogram(counts)
plt.title(f"Quantum Coin Flip - {shots} Shots")
plt.savefig("histogram.png")
plt.show()