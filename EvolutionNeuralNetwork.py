# -*- coding: utf-8 -*-
__author__ = 'Chason'
from Neuron import *
import random

class EvolutionNeuralNetwork:
    def __init__(self, input_nodes_num, max_layer_hid_num, max_hidden_nodes_num, output_nodes_num):
        self.input_nodes_num = input_nodes_num
        self.max_hidden_layers_num = max_layer_hid_num
        self.max_hidden_nodes_num = max_hidden_nodes_num
        self.output_nodes_num = output_nodes_num
        self.layer_in = [Neuron(0, i, 0) for i in range(input_nodes_num)]
        self.layer_hid = [[Neuron((i + 1), j) for j in range(max_hidden_nodes_num)] for i in range(max_layer_hid_num)]
        self.layer_out = [Neuron(max_layer_hid_num + 1, i, 0) for i in range(output_nodes_num)]
        self.connection_num = 0
        self.information = "Evolution Neural Network"
        
    def forward_propagation(self):
        for lay in self.layer_hid:
            for node in lay:
                if node.get_input_size() > 0:
                    node.activation()
        for node in self.layer_out:
            if node.get_input_size() > 0:
                node.activation()

    def punishment(self):
        pass

    def rnd_pick_new_input_neuron(self, neuron):
        if neuron == None:
            return
        if neuron.layer_num <= 0 or neuron.layer_num > (self.max_hidden_layers_num + 1):
            print "[error] host layer index out of range!"
            return None
        unconnected_nodes = []
        for node in self.layer_in:
            for input_node in neuron.input_neurons:
                if input_node == node:
                    break
            else:
                unconnected_nodes.append(node)
        for layer_inx, layer in enumerate(self.layer_hid):
            if (layer_inx + 1) < neuron.layer_num:
                for node in layer:
                    if node.get_input_size() > 0:
                        for input_node in neuron.input_neurons:
                            if input_node == node:
                                break
                        else:
                            unconnected_nodes.append(node)
            else:
                break
        unconnected_num = len(unconnected_nodes)
        # print "number of unconnected nodes:", unconnected_num
        if unconnected_num > 0:
            rnd_index = (int)(random.random() * unconnected_num)
            return unconnected_nodes[rnd_index]
        else:
            print "[warning] There is no unconnected node."
            return None

    def rnd_pick_used_node(self):
        used_nodes = []
        for layer in self.layer_hid:
            for node in layer:
                if node.get_input_size() > 0:
                    used_nodes.append(node)
        for node in self.layer_out:
            if node.get_input_size() > 0:
                used_nodes.append(node)
        unused_num = len(used_nodes)
        if unused_num > 0:
            rnd_index = (int)(random.random() * unused_num)
            return used_nodes[rnd_index]
        else:
            print "[warning] There is no used node."
            return None

    def rnd_pick_unused_node(self):
        unused_nodes = []
        for layer in self.layer_hid:
            for node in layer:
                if node.get_input_size() == 0:
                    unused_nodes.append(node)
        unused_num = len(unused_nodes)
        if unused_num > 0:
            rnd_index = (int)(random.random() * unused_num)
            return unused_nodes[rnd_index]
        else:
            print "[warning] There is no unused node."
            return None

    def rnd_add_connection(self, neuron):
        if neuron == None:
            return
        ne = self.rnd_pick_new_input_neuron(neuron)
        if ne == None:
            return
        theta = (random.random() * 20) - 10
        # print "connecting:","[" + str(neuron.layer_num) + ", " + str(neuron.node_num) + "] from [" + \
        #                           str(ne.layer_num) + ", " + str(ne.node_num) + "]\ttheta:",theta
        neuron.addInput(ne, theta)
        neuron.setValue(0)
        self.connection_num += 1

    def rnd_disconnection(self, neuron):
        if neuron == None or neuron.get_input_size() == 0:
            print "[warning] There is nothing to disconnect."
            return
        rnd_index = (int)(random.random() * neuron.get_input_size())
        ne = neuron.input_neurons[rnd_index]
        theta = neuron.theta[rnd_index]
        # print "disconnecting:","[" + str(neuron.layer_num) + ", " + str(neuron.node_num) + "] from [" + \
        #                           str(ne.layer_num) + ", " + str(ne.node_num) + "]\ttheta:",theta
        neuron.delInput(rnd_index)
        self.connection_num -= 1

    def show_structure(self):
        print "/******************************************************************************************\\"
        print "|\tself-evolution neural network maximum structure: %d -"%self.input_nodes_num,
        for i in range(self.max_hidden_layers_num):
            print "%d -"%self.max_hidden_nodes_num,
        print self.output_nodes_num

        print "|\tinput layer0:\t",
        for i in self.layer_in:
            print i.getValue(),"\t",
        print
        for inx, i in enumerate(self.layer_hid):
            print "|\thidden layer%d:\t"%(inx+1),
            for j in i:
                print j.getValue(), "\t",
            print
        print "|\toutput layer%d:\t"%(self.max_hidden_layers_num + 1),
        for i in self.layer_out:
            print i.getValue(),"\t",
        print
        print "|------------------------------------------------------------------------------------------"
        print "|\tconnections:\t%d"%self.connection_num
        for layer in self.layer_hid:
            for node in layer:
                if node.get_input_size() > 0:
                    print "|\t%d neurons connected to [%d, %d]:"%(node.get_input_size(), node.layer_num, node.node_num)
                    for inx, input_node in enumerate(node.input_neurons):
                        print "|\t\t[%d, %d]\ttheta: %f"%(input_node.layer_num, input_node.node_num, node.theta[inx])
        for node in self.layer_out:
            if node.get_input_size() > 0:
                print "|\t%d neurons connected to [%d, %d]:"%(node.get_input_size(), node.layer_num, node.node_num)
                for inx, input_node in enumerate(node.input_neurons):
                    print "|\t\t[%d, %d]\ttheta: %f"%(input_node.layer_num, input_node.node_num, node.theta[inx])
        print "\******************************************************************************************/"

    def save_enn_information(self):
        self.information = "/******************************************************************************************\\\n"
        self.information += str("|\tself-evolution neural network maximum structure: %d -"%self.input_nodes_num)
        for i in range(self.max_hidden_layers_num):
            self.information += str("%d -"%self.max_hidden_nodes_num,)
        self.information += str(self.output_nodes_num) + "\n"

        self.information += str("|\tinput layer0:\t")
        for i in self.layer_in:
            self.information += str(str(i.getValue()) + "\t")
        self.information += "\n"
        for inx, i in enumerate(self.layer_hid):
            self.information += str("|\thidden layer%d:\t"%(inx+1),)
            for j in i:
                self.information += str(str(j.getValue()) + "\t")
            self.information += "\n"
        self.information += str("|\toutput layer%d:\t"%(self.max_hidden_layers_num + 1),)
        for i in self.layer_out:
            self.information += str(str(i.getValue()) + "\t")
        self.information += "\n"
        self.information += "|------------------------------------------------------------------------------------------\n"
        self.information += str("|\tconnections:\t%d\n"%self.connection_num)
        for layer in self.layer_hid:
            for node in layer:
                if node.get_input_size() > 0:
                    self.information += str("|\t%d neurons connected to [%d, %d]:\n"%(node.get_input_size(), node.layer_num, node.node_num))
                    for inx, input_node in enumerate(node.input_neurons):
                        self.information += str("|\t\t[%d, %d]\ttheta: %f\n"%(input_node.layer_num, input_node.node_num, node.theta[inx]))
        for node in self.layer_out:
            if node.get_input_size() > 0:
                self.information += str("|\t%d neurons connected to [%d, %d]:\n"%(node.get_input_size(), node.layer_num, node.node_num))
                for inx, input_node in enumerate(node.input_neurons):
                    self.information += str("|\t\t[%d, %d]\ttheta: %f\n"%(input_node.layer_num, input_node.node_num, node.theta[inx]))
        self.information += "\******************************************************************************************/"
