from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Step 1: Create entanglement between qubit 1 & 2 (Bell pair)
qc.h(1)  # Hadamard gate on qubit 1
qc.cx(1, 2)  # CNOT gate with qubit 1 as control and qubit 2 as target

# Step 2: Apply a random state to qubit 0 (Message qubit)
qc.h(0)  # Hadamard gate to create superposition

# Step 3: Bell measurement between qubit 0 & qubit 1
qc.cx(0, 1)  # CNOT gate
qc.h(0)  # Hadamard gate
qc.measure([0, 1], [0, 1])  # Measure qubits 0 & 1

# Step 4: Classical communication and correction on qubit 2
qc.cx(1, 2)  # Conditional X gate based on qubit 1 measurement
qc.cz(0, 2)  # Conditional Z gate based on qubit 0 measurement
qc.measure(2, 2)  # Measure qubit 2

# Execute on simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts(qc)

# Display results
plot_histogram(counts)
print("Measurement Outcomes:", counts)
