# Implementation of sigmoid function
import math
# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
# Test values
values = [-5, -2, 0, 2, 5]
# Print sigmoid values
for x in values:
    result = sigmoid(x)
    print("x =", x, "Sigmoid =", result)

# Explanation of the sigmoid function 
# The sigmoid function acts like a converter.")
# It takes a number, no matter how large or small,")
# and squeezes it into a range from 0 to 1.")
