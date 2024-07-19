import cirq
import numpy as np
import matplotlib.pyplot as plt

# Define a qubit
qubit = cirq.GridQubit(0, 0)

# Define a quantum circuit
circuit = cirq.Circuit()

# Define a unitary operator (Hadamard gate in this case)
unitary_operator = cirq.H(qubit)

# Add the unitary operator to the circuit
circuit.append(unitary_operator)

# Define the initial state (|0⟩ state)
initial_state = np.array([1, 0])

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.simulate(circuit, initial_state=initial_state)

# Get the final state vector
final_state = result.final_state_vector

# Plot the real and imaginary parts of the final state vector
plt.figure(figsize=(10, 6))
plt.bar(range(len(final_state)), np.real(final_state), alpha=0.6, label='Real part')
plt.bar(range(len(final_state)), np.imag(final_state), alpha=0.6, label='Imaginary part')
plt.xlabel('State index')
plt.ylabel('Amplitude')
plt.title('Final State Vector after Applying Unitary Operator')
plt.legend()
plt.grid(True)
plt.show()
