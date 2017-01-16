# -*- coding: utf-8 -*-
__author__ = 'Chason'
import math
class Neuron:
    def __init__(self,layer_num , node_num, value = -1, ):
        self.value = value
        self.input_neurons = []
        self.theta = []
        self.layer_num = layer_num
        self.node_num = node_num
        self.threshold = 0.5

    def output(self):
        if self.value > self.threshold:
            return True
        else:
            return False

    def addInput(self, neuron, theta):
        self.input_neurons.append(neuron)
        self.theta.append(theta)

    def delInput(self, inx):
        if inx >= len(self.input_neurons):
            print "error: Index of delete operation out of range!"
            return False
        self.input_neurons.pop(inx)
        self.theta.pop(inx)
        return True

    def sigmoid(self, z):
        return 1.0 / (1.0 + math.exp(-z))

    def get_input_size(self):
        return len(self.input_neurons)

    def activation(self):
        inputs_len = self.get_input_size()
        if inputs_len != len(self.theta):
            print "error: Input neurons and theta must be the same size!"
            return None
        elif inputs_len == 0:
            print "error: This neuron has no inputs!"
            return None
        res = 0
        # print self.layer_num,self.node_num
        for inx in range(inputs_len):
            res += self.input_neurons[inx].value * self.theta[inx]
        res = self.sigmoid(res)
        self.setValue(res)
        return res

    def setTheta(self, theta):
        if self.get_input_size() != len(theta):
            print "The size of thetas cannot change!"
            return False
        self.theta = theta
        return True

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value