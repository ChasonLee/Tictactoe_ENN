# -*- coding: utf-8 -*-
__author__ = 'Chason'
from EvolutionNeuralNetwork import *
import copy

class EnnPlayer:
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3, enn = None, evolution_times = 0, hand_make_enn = False, player = 1):
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM
        self.play_times = 0
        self.win_times = 0
        self.loss_times = 0
        self.draw_times = 0
        self.evolution_times = evolution_times
        self.player = player

        if enn == None and hand_make_enn == False:
            self.enn = EvolutionNeuralNetwork(self.ROW * self.COL * 3, 4, 10, self.ROW * self.COL)
            for i in range(10):
                self.enn.rnd_add_connection(self.enn.rnd_pick_unused_node())
            for node in self.enn.layer_out:
                for i in range(5):
                    self.enn.rnd_add_connection(node)
        elif enn != None and hand_make_enn == False:
            self.enn = copy.deepcopy(enn)
        elif hand_make_enn == True:
            self.enn = EvolutionNeuralNetwork(self.ROW * self.COL * 3, 1, 24, self.ROW * self.COL)
            self.enn.layer_out[0].addInput(self.enn.layer_in[1], -100)
            self.enn.layer_out[0].addInput(self.enn.layer_in[2], -100)
            self.enn.layer_out[1].addInput(self.enn.layer_in[4], -100)
            self.enn.layer_out[1].addInput(self.enn.layer_in[5], -100)
            self.enn.layer_out[2].addInput(self.enn.layer_in[7], -100)
            self.enn.layer_out[2].addInput(self.enn.layer_in[8], -100)
            self.enn.layer_out[3].addInput(self.enn.layer_in[10], -100)
            self.enn.layer_out[3].addInput(self.enn.layer_in[11], -100)
            self.enn.layer_out[4].addInput(self.enn.layer_in[13], -100)
            self.enn.layer_out[4].addInput(self.enn.layer_in[14], -100)
            self.enn.layer_out[5].addInput(self.enn.layer_in[16], -100)
            self.enn.layer_out[5].addInput(self.enn.layer_in[17], -100)
            self.enn.layer_out[6].addInput(self.enn.layer_in[19], -100)
            self.enn.layer_out[6].addInput(self.enn.layer_in[20], -100)
            self.enn.layer_out[7].addInput(self.enn.layer_in[22], -100)
            self.enn.layer_out[7].addInput(self.enn.layer_in[23], -100)
            self.enn.layer_out[8].addInput(self.enn.layer_in[25], -100)
            self.enn.layer_out[8].addInput(self.enn.layer_in[26], -100)

            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][0], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][1], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][2], 10)
            # self.enn.layer_out[1].addInput(self.enn.layer_hid[0][3], 10)
            # self.enn.layer_out[1].addInput(self.enn.layer_hid[0][4], 10)
            # self.enn.layer_out[2].addInput(self.enn.layer_hid[0][5], 10)
            # self.enn.layer_out[2].addInput(self.enn.layer_hid[0][6], 10)
            # self.enn.layer_out[2].addInput(self.enn.layer_hid[0][7], 10)
            # self.enn.layer_out[3].addInput(self.enn.layer_hid[0][8], 10)
            # self.enn.layer_out[3].addInput(self.enn.layer_hid[0][9], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][10], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][11], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][12], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][13], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][14], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][15], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][16], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][17], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][18], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][19], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][20], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][21], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][22], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_hid[0][23], 10)
            #
            # self.enn.layer_hid[0][0].addInput(self.enn.layer_in[5], 10)
            # self.enn.layer_hid[0][0].addInput(self.enn.layer_in[8], 10)
            # self.enn.layer_hid[0][1].addInput(self.enn.layer_in[14], 10)
            # self.enn.layer_hid[0][1].addInput(self.enn.layer_in[26], 10)
            # self.enn.layer_hid[0][2].addInput(self.enn.layer_in[11], 10)
            # self.enn.layer_hid[0][2].addInput(self.enn.layer_in[20], 10)
            #
            # self.enn.layer_hid[0][3].addInput(self.enn.layer_in[2], 10)
            # self.enn.layer_hid[0][3].addInput(self.enn.layer_in[8], 10)
            # self.enn.layer_hid[0][4].addInput(self.enn.layer_in[14], 10)
            # self.enn.layer_hid[0][4].addInput(self.enn.layer_in[23], 10)
            #
            # self.enn.layer_hid[0][5].addInput(self.enn.layer_in[2], 10)
            # self.enn.layer_hid[0][5].addInput(self.enn.layer_in[5], 10)
            # self.enn.layer_hid[0][6].addInput(self.enn.layer_in[14], 10)
            # self.enn.layer_hid[0][6].addInput(self.enn.layer_in[20], 10)
            # self.enn.layer_hid[0][7].addInput(self.enn.layer_in[17], 10)
            # self.enn.layer_hid[0][7].addInput(self.enn.layer_in[26], 10)
            #
            # self.enn.layer_hid[0][8].addInput(self.enn.layer_in[2], 10)
            # self.enn.layer_hid[0][8].addInput(self.enn.layer_in[20], 10)
            # self.enn.layer_hid[0][9].addInput(self.enn.layer_in[14], 10)
            # self.enn.layer_hid[0][9].addInput(self.enn.layer_in[17], 10)
            #
            # self.enn.layer_hid[0][10].addInput(self.enn.layer_in[2], 10)
            # self.enn.layer_hid[0][10].addInput(self.enn.layer_in[26], 10)
            # self.enn.layer_hid[0][10].addInput(self.enn.layer_in[5], 10)
            # self.enn.layer_hid[0][10].addInput(self.enn.layer_in[23], 10)


            # self.enn.layer_out[0].addInput(self.enn.layer_in[4], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_in[10], 10)
            # self.enn.layer_out[0].addInput(self.enn.layer_in[13], 10)
            #
            # self.enn.layer_out[1].addInput(self.enn.layer_in[1], 10)
            # self.enn.layer_out[1].addInput(self.enn.layer_in[7], 10)
            # self.enn.layer_out[1].addInput(self.enn.layer_in[13], 10)
            #
            # self.enn.layer_out[2].addInput(self.enn.layer_in[4], 10)
            # self.enn.layer_out[2].addInput(self.enn.layer_in[13], 10)
            # self.enn.layer_out[2].addInput(self.enn.layer_in[16], 10)
            #
            # self.enn.layer_out[3].addInput(self.enn.layer_in[1], 10)
            # self.enn.layer_out[3].addInput(self.enn.layer_in[13], 10)
            # self.enn.layer_out[3].addInput(self.enn.layer_in[19], 10)
            #
            # self.enn.layer_out[4].addInput(self.enn.layer_in[1], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[4], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[7], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[10], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[16], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[19], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[22], 10)
            # self.enn.layer_out[4].addInput(self.enn.layer_in[25], 10)
            #
            # self.enn.layer_out[5].addInput(self.enn.layer_in[7], 10)
            # self.enn.layer_out[5].addInput(self.enn.layer_in[13], 10)
            # self.enn.layer_out[5].addInput(self.enn.layer_in[25], 10)
            #
            # self.enn.layer_out[6].addInput(self.enn.layer_in[10], 10)
            # self.enn.layer_out[6].addInput(self.enn.layer_in[13], 10)
            # self.enn.layer_out[6].addInput(self.enn.layer_in[22], 10)
            #
            # self.enn.layer_out[7].addInput(self.enn.layer_in[13], 10)
            # self.enn.layer_out[7].addInput(self.enn.layer_in[19], 10)
            # self.enn.layer_out[7].addInput(self.enn.layer_in[25], 10)
            #
            # self.enn.layer_out[8].addInput(self.enn.layer_in[13], 10)
            # self.enn.layer_out[8].addInput(self.enn.layer_in[16], 10)
            # self.enn.layer_out[8].addInput(self.enn.layer_in[22], 10)

        self.enn.save_enn_information()

    def set_enn(self, enn):
        self.enn = copy.deepcopy(enn)

    def enn_sense_input(self, board):
        board_list = []
        for r in board:
            for p in r:
                for i in range(3):
                    if p.value == i:
                        board_list.append(1)
                    else:
                        board_list.append(0)

        for inx, node in enumerate(self.enn.layer_in):
            node.value = board_list[inx]

    def enn_move(self):
        self.enn.forward_propagation()
        best_output = 0
        best_output_inx = -1
        for o in self.enn.layer_out:
            if best_output_inx == -1:
                best_output = o.value
                best_output_inx = o.node_num
            elif o.value > best_output:
                best_output = o.value
                best_output_inx = o.node_num
        return best_output_inx

    def show_enn_player_info(self):
        print "Enn Player information:"
        print "\tplay times:", self.play_times
        print "\t win times:", self.win_times
        print "\tloss times:", self.loss_times
        print "\tdraw times:", self.draw_times
        print

    def rnd_evolve(self):
        times = (int)(random.random() * 5)
        for i in range(times):
            self.enn.rnd_add_connection(self.enn.rnd_pick_unused_node())
        times = (int)(random.random() * 5)
        for i in range(times):
            self.enn.rnd_disconnection(self.enn.rnd_pick_used_node())
        for node in self.enn.layer_out:
            times = (int)(random.random() * 5)
            for i in range(times):
                self.enn.rnd_add_connection(node)
            times = (int)(random.random() * 5)
            for i in range(times):
                self.enn.rnd_disconnection(node)

    def small_evolve(self):
        times = (int)(random.random() * 2)
        for i in range(times):
            self.enn.rnd_add_connection(self.enn.rnd_pick_unused_node())

        times = (int)(random.random() * 2)
        for i in range(times):
            self.enn.rnd_disconnection(self.enn.rnd_pick_used_node())

        times = (int)(random.random() * 2)
        for i in range(times):
            self.enn.rnd_add_connection(self.enn.rnd_pick_used_node())
