# -*- coding: utf-8 -*-
__author__ = 'Chason'
import pickle
from EvolutionNeuralNetwork import *

f = open("EnnPlayer.data")
load_player = pickle.load(f)
f.close()

load_player.enn.show_structure()