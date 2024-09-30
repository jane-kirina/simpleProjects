import numpy as np
import neuron as n


class SimpleNeuralNetwork:
    '''
    A neural network with:
      - 2 inputs
      - a hidden layer with 2 neurons (h1, h2)
      - an output layer with 1 neuron (o1)
    '''

    def __init__(self, weights=np.array([0, 1, 1]), bias=0):
        self.h1 = n.Neuron(weights, bias)
        self.h2 = n.Neuron(weights, bias)
        self.o1 = n.Neuron(weights, bias)

    def feedforward(self, X):
        out_h1 = self.h1.feedforward(X)
        out_h2 = self.h2.feedforward(X)
        print(out_h1)
        print(out_h2)

        # The inputs for o1 are the outputs from h1 and h2
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1


'''
# EXAMPLE
'''

network = SimpleNeuralNetwork()
x = np.array([2, 3, 2])
print(network.feedforward(x))  # 0.7216325609518421
