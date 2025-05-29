# Quantum-Teleportation-Circuit-in-Python-
Quantum Teleportation Circuit in Python:


**How This Works:**
Entanglement: Creates an entangled pair between two qubits (1 and 2).

State Preparation: A random state is applied to qubit 0 (the one being teleported).

Bell Measurement: Qubit 0 and 1 interact using a CNOT and Hadamard gate, then are measured.

Classical Communication: The measurement results are used to apply corrections (CX and CZ) on qubit 2.

Final Result: Qubit 2 now holds the original quantum state of qubit 0, effectively "teleporting" it.

**Running This in Azure Quantum:**
You can submit this circuit using Azure Quantum providers (like IonQ or Quantinuum) instead of simulating it locally.

Install Qiskit (pip install qiskit).

Set up Azure Quantum workspace.

Use Qiskit's quantum backends in Azure instead of the simulator.

