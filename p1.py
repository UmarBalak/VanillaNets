# 4 inputs with single neuron
'''
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = sum(inputs[i] * weights[i] for i in range(len(inputs))) + bias
print(output)
'''

# 4 inputs with 3 neurons
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
biases = [2.0, 3.0, 0.5]

outputs = []
for i in range(len(weights)):
    res = sum(inputs[j] * weights[i][j] for j in range(len(inputs))) + biases[i]
    
    outputs.append(res)

print(outputs)
