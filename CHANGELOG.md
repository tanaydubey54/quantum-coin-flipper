# Changelog
## v1.1.1 [June 2 2026]
- added MIT License for the project to be used freely
- added input validation for number of shots
- added Qiskit's `draw` visualization tool in the code to generate circuit diagram 
- histogram output files are now timestamped as: `histogram_YYYYMMDD_HHMMSS.png` 
- other minor polishes: bug fixes, addition of .gitignore, wrapped code in main
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