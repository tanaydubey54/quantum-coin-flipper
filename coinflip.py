"""
Quantum Coin Flipper
--------------------
Simulates a fair coin flip using a single-qubit quantum circuit.
A Hadamard gate places the qubit in equal superposition of |0⟩ and |1⟩.
Measuring collapses it to either state with 50% probability.

Circuit: q0--H--M--

Dependencies: qiskit, matplotlib
"""
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    # build circuit
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    
    # display circuit
    print("\nQuantum Circuit:")
    print(qc.draw())
    
    # get number of shots
    try:
        shots = int(input("\nEnter number of shots: "))
        if shots <= 0:
            raise ValueError("Shots must be positive")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Run simulation
    print(f"\nRunning simulation with {shots} shots...")
    sampler = StatevectorSampler()
    job = sampler.run([qc], shots=shots)
    result = job.result()
    
    # Extract and display counts
    counts = result[0].data.c.get_counts()
    print(f"\nResults: {counts}")
    
    # Calculate probabilities
    total = sum(counts.values())
    prob_0 = counts.get('0', 0) / total * 100
    prob_1 = counts.get('1', 0) / total * 100
    print(f"P(|0⟩) = {prob_0:.2f}%")
    print(f"P(|1⟩) = {prob_1:.2f}%")
    
    # Visualize
    fig = plot_histogram(counts)
    plt.title(f"Quantum Coin Flip - {shots} Shots")
    
    # Save with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"histogram_{timestamp}.png"
    plt.savefig(filename)
    print(f"\nHistogram saved as {filename}")
    
    plt.show()

if __name__ == "__main__":
    main()