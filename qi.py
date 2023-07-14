from qiskit import QuantumCircuit, Aer, execute
import numpy as np

prefix = "sk-FU8tzDbeJV2PstDuijYTT"
suffix = "3BlbkFJl"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
output_file = "generated_keys.txt"

def generate_keys(circuit, key, length):
    if length == 16:
        # Measure the qubits and append the suffix to the key
        circuit.measure_all()
        key = key + suffix

        # Execute the circuit and get the results
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(circuit, simulator, shots=1).result()
        counts = result.get_counts()

        # Append the key to the output file
        with open(output_file, 'a') as file:
            file.write(key + '\n')

    else:
        # Recursively create superposition of characters
        for char in characters:
            circuit.x(length)
            circuit.h(length)
            generate_keys(circuit, key + char, length + 1)
            circuit.h(length)
            circuit.x(length)

# Create quantum circuit
num_qubits = 16
circuit = QuantumCircuit(num_qubits, num_qubits)

# Generate keys
generate_keys(circuit, prefix, 0)

print("Keys generated successfully. Please check", output_file)
