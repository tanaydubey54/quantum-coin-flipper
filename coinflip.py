from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.h(0)

sv = Statevector(qc)
counts = sv.sample_counts(10000)
print("Results: ", counts)

plot_histogram(counts)
plt.title("Quantum Coin Flip - 1000 shots")
plt.savefig("histogram.png")
plt.show()