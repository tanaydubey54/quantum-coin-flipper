# Changelog
## v1.1.0 [June 1 2026]
- migrated to proper Qiskit execution pipeline using StatevectorSampler instead of using sample_counts()
- added classical register to QuantumCircuit
- added explicit measurement gate (qc.measure)
- made number of shots user-configurable via input()
- fixed plt.title() to use f-string formatting and show correct shot count
- added module-level docstrings 
- added inline comments

## v1.0.0 [May 31 2026]
- initial release
single-qubit Hadamard circuit
- Statevector sampling (10000 shots)
- Histogram output saved as histogram.png