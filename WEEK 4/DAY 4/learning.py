# Implementation of sigmoid function
import math
# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
# Test values
values = [-10, -1, 1, 10]
# Print sigmoid values
for x in values:
    result = sigmoid(x)
    print("x =", x, "Sigmoid =", result)