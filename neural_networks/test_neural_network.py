import numpy as np
import neural_networks.neuron as n


class TestNeuralNetwork:
    '''
    A neural network with:
      - 2 inputs
      - a hidden layer with 2 neurons (h1, h2)
      - an output layer with 1 neuron (o1)
    '''

    def __init__(self):
        np.random.seed(42)
        # Weights
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        # Biases
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feedforward(self, x):
        # x is a numpy array with 2 elements
        h1 = n.Neuron(np.array([self.w1, self.w2]), self.b1).feedforward(np.array([x[0], x[1]]))
        h2 = n.Neuron(np.array([self.w3, self.w4]), self.b2).feedforward(np.array([x[0], x[1]]))

        o1 = n.Neuron(np.array([self.w5, self.w6]), self.b3).feedforward(np.array([h1, h2]))
        return o1

    def train(self, data, all_y_trues):
        '''
        - data - numpy array
        - all_y_trues is a numpy array with n elements
        '''
        learn_rate = 0.1
        epochs = 1000  # number of times to loop through the entire dataset

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # feedforward
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = n.sigmoid_activation_func(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = n.sigmoid_activation_func(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = n.sigmoid_activation_func(sum_o1)
                y_pred = o1

                # Calculate partial derivatives.  d_L_d_w1 -> "partial L / partial w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

                # Neuron o1
                d_ypred_d_w5 = h1 * n.derivative_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * n.derivative_sigmoid(sum_o1)
                d_ypred_d_b3 = n.derivative_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * n.derivative_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * n.derivative_sigmoid(sum_o1)

                # Neuron h1
                d_h1_d_w1 = x[0] * n.derivative_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * n.derivative_sigmoid(sum_h1)
                d_h1_d_b1 = n.derivative_sigmoid(sum_h1)

                # Neuron h2
                d_h2_d_w3 = x[0] * n.derivative_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * n.derivative_sigmoid(sum_h2)
                d_h2_d_b2 = n.derivative_sigmoid(sum_h2)

                # Update weights and biases
                # Neuron h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # Neuron h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                # Neuron o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

            # Calculate total loss at the end of each epoch
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = n.mse_loss(all_y_trues, y_preds)
                print("Epoch %d loss: %.3f" % (epoch, loss))


# Define dataset
data = np.array([
    [-2, -1],  # Alice
    [25, 6],  # Bob
    [17, 4],  # Charlie
    [-15, -6],  # Diana
])
all_y_trues = np.array([
    1,  # Alice
    0,  # Bob
    0,  # Charlie
    1,  # Diana
])

# Train neural network
network = TestNeuralNetwork()
network.train(data, all_y_trues)
