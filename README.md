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


The output of the quantum teleportation circuit depends on the measurement outcomes. Since quantum states involve probabilities, the results will vary across different runs. However, here’s a general expectation:

Initial State: The first qubit (q0) is placed in superposition before teleportation.

Bell Measurement Results: Measuring qubits q0 and q1 yields four possible outcomes (00, 01, 10, 11), each corresponding to different corrections on q2.

Final Teleported State: After applying the necessary quantum gates based on measurement results, qubit 2 (q2) holds the original quantum state of qubit 0.

In practice, after running this on a quantum simulator, the output will be a histogram of possible measurement outcomes, showing how often each result appears. The results would look like:

python
{'000': 250, '001': 260, '010': 260, '011': 254} # Example counts from 1024 runs
This means that teleportation works correctly, and qubit q2 receives the expected quantum state based on classical corrections.

