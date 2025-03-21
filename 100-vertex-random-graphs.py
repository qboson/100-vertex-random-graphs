# Import necessary libraries
import numpy as np

# Number of vertices in the graph
num_bit = 100

# Edge density (probability of an edge existing between two vertices)
density = 0.8

# Bit width for weighting edges (set to 0 in this example)
bit_width = 0

# Maximum number based on bit width
max_number = 2 ** bit_width

# Initialize adjacency matrix J with zeros
J = np.zeros((num_bit, num_bit))

# Generate random weights for edges
for i in range(num_bit):
    for j in range(num_bit):
        if i < j:
            # Randomly determine whether to create an edge based on density
            if np.random.rand() < density:


                # Assign a random weight between 1 and max_number
                J[i, j] = int(np.ceil(np.random.rand() * max_number))
                J[j, i] = int(np.ceil(np.random.rand() * max_number))

# Ensure all vertices have at least one connection
for i in range(num_bit):
    if np.sum(J[i, :]) == 0:
        # Randomly select a connected vertex for the isolated vertex
        j = int(np.floor(num_bit * np.random.rand()))
        J[i, j] = 1
        J[j, i] = 1

# Save the adjacency matrix to a file
np.savetxt(
    'G' + str(num_bit) + '_' + str(int(density * 10)) + '_' + str(bit_width) + 'bit.graph',
    J,
    delimiter=",",
    fmt='%.6f'
)

# Print statistics about the graph
print(np.sum(np.float64(J > 0)))  # Total number of edges
print(np.sum(J - J.T))            # Check for symmetry in the adjacency matrix
