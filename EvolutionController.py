# -*- coding: utf-8 -*-
__author__ = 'Chason'

import random
from EnnPlayer import *
import pickle
import threading

class Piece:
    def __init__(self,r, c, value = 0):
        self.r = r
        self.c = c
        self.value = value

class Tictactoe(threading.Thread):
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3, times = 1000, enn_player = None):
        threading.Thread.__init__(self)
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM

        self.EMPTY_NUM = 0
        self.PLAYER1_NUM = 1
        self.PLAYER2_NUM = 2
        self.DRAW = 3

        self.EMPTY_CHAR = '.'
        self.PLAYER1_CHAR = '#'
        self.PLAYER2_CHAR = '*'

        self.AI = 0
        self.board = [[Piece(r, c) for c in range(self.COL)] for r in range(self.ROW)]
        self.finished = False
        self.times = times
        self.enn_player = enn_player

    def initBoard(self):
        self.board = [[Piece(r, c) for c in range(self.COL)] for r in range(self.ROW)]

    def showBoard(self):
        for i in self.board:
            for j in i:
                if j.value == self.PLAYER1_NUM:
                    print self.PLAYER1_CHAR,
                elif j.value == self.PLAYER2_NUM:
                    print self.PLAYER2_CHAR,
                else:
                    print self.EMPTY_CHAR,
            print
        print

    def judge(self, r, c):
        player = self.board[r][c].value
        for i in range(4):
            if i == 0:
                dr = -1
                dc = -1
            elif i == 1:
                dr = -1
                dc = 0
            elif i == 2:
                dr = -1
                dc = 1
            else:
                dr = 0
                dc = 1
            nr = r + dr
            nc = c + dc
            count = 1
            while nr >= 0 and nr < self.ROW and nc >= 0 and nc < self.COL:
                if self.board[nr][nc].value == player:
                    count = count + 1
                    nr = nr + dr
                    nc = nc + dc
                else:
                    break
            dr = -dr
            dc = -dc
            nr = r + dr
            nc = c + dc
            while nr >= 0 and nr < self.ROW and nc >= 0 and nc < self.COL:
                if self.board[nr][nc].value == player:
                    count = count + 1
                    nr = nr + dr
                    nc = nc + dc
                else:
                    break
            if count >= self.WIN_NUM:
                return player

        empty_pieces = []
        for r in self.board:
            for p in r:
                if p.value == self.EMPTY_NUM:
                    empty_pieces.append(p)
        if len(empty_pieces) == 0:
            return self.DRAW
        return None

    def showResult(self, res):
        if res == self.PLAYER1_NUM:
            print "Player(", self.PLAYER1_CHAR,") Wins!"
            return True
        elif res == self.PLAYER2_NUM:
            print "Player(", self.PLAYER2_CHAR,") Wins!"
            return True
        elif res == self.DRAW:
            print "There is a draw."
            return True
        else:
            # print "No one wins"
            return False

    def move(self, r, c, player):
        if self.board[r][c].value == self.EMPTY_NUM:
            self.board[r][c].value = player
            return True
        else:
            print "error: [%d, %d] has been occupied."%(r, c)
            return False

    def move_inx(self, inx, player):
        r = (int)(inx / self.COL)
        c = inx % self.COL
        if self.board[r][c].value == self.EMPTY_NUM:
            self.board[r][c].value = player
            return True
        else:
            print "error: [%d, %d] has been occupied."%(r, c)
            return False

    def rnd_move(self, player):
        empty_pieces = []
        for r in self.board:
            for p in r:
                if p.value == self.EMPTY_NUM:
                    empty_pieces.append(p)
        empty_len = len(empty_pieces)
        if empty_len > 0:
            rnd_index = (int)(random.random() * empty_len)
            ep = empty_pieces[rnd_index]
            self.move(ep.r, ep.c, player)
            return self.judge(ep.r, ep.c)
        else:
            print "error: There is nowhere to move to."
            return None

    def other_player(self, player):
        if player == self.PLAYER1_NUM:
            return self.PLAYER2_NUM
        else:
            return self.PLAYER1_NUM

    def enn_move(self, enn_player, player):
        enn_player.enn_sense_input(self.board)
        inx = enn_player.enn_move()
        r = (int)(inx / self.COL)
        c = inx % self.COL
        if self.move(r, c, player):
            return self.judge(r, c)
        else:
            return self.other_player(player)

    def run(self):
        self.finished = False
        for t in range(self.times):
            self.initBoard()
            while True:
                res = self.enn_move(self.enn_player, self.PLAYER1_NUM)
                if res == self.PLAYER1_NUM:
                    self.enn_player.win_times += 1
                    self.enn_player.play_times += 1
                    break
                elif res == self.PLAYER2_NUM:
                    self.enn_player.loss_times += 1
                    self.enn_player.play_times += 1
                    break
                elif res == self.DRAW:
                    self.enn_player.draw_times += 1
                    self.enn_player.play_times += 1
                    break
                # self.showResult(res)
                # self.showBoard()
                res = self.rnd_move(self.PLAYER2_NUM)
                if res == self.PLAYER1_NUM:
                    self.enn_player.win_times += 1
                    self.enn_player.play_times += 1
                    break
                elif res == self.PLAYER2_NUM:
                    self.enn_player.loss_times += 1
                    self.enn_player.play_times += 1
                    break
                elif res == self.DRAW:
                    self.enn_player.draw_times += 1
                    self.enn_player.play_times += 1
                    break
                # self.showBoard()
            # self.showBoard()
        self.finished = True
        # self.enn_player.show_enn_player_info()

def main(load=False):
    ROW = 3
    COL = 3
    WIN_NUM = 3
    file_name = "EnnPlayer_27_4_10_9.data"
    if load == False:
        enn_players = [EnnPlayer(ROW, COL, WIN_NUM) for i in range(10)]
    else:
        f = open(file_name)
        load_player = pickle.load(f)
        f.close()
        print "loaded data."
        load_player.show_enn_player_info()

        new_enn_player = EnnPlayer(enn = load_player.enn, evolution_times=load_player.evolution_times)
        enn_players = [new_enn_player]
        for i in range(9):
            sme_enn_player = copy.deepcopy(new_enn_player)
            sme_enn_player.small_evolve()
            enn_players.append(EnnPlayer(enn = sme_enn_player.enn, evolution_times=sme_enn_player.evolution_times))
    generations = 100000
    for g in range(generations):
        ttts = []
        for inx, ep in enumerate(enn_players):
            ttt = Tictactoe(times=1000, enn_player=ep)
            ttt.setDaemon(True)
            ttts.append(ttt)
            ttt.start()
            ttt.join()
            print "generation: %d - %d"%(ep.evolution_times + 1, inx + 1)
            ep.show_enn_player_info()

        # while True:
        #     count = 0
        #     for t in ttts:
        #         if t.finished == True:
        #             count += 1
        #     else:
        #         if count == len(enn_players):
        #             print "All %d games are finished."%len(ttts)
        #             break
        #         else:
        #             print "%d finished..."%count

        best_ep_win_times = 0
        best_ep_win_times_inx = -1
        for inx, ep in enumerate(enn_players):
            if best_ep_win_times_inx == -1:
                best_ep_win_times = ep.win_times
                best_ep_win_times_inx = inx
            elif best_ep_win_times < ep.win_times:
                best_ep_win_times = ep.win_times
                best_ep_win_times_inx = inx
        print "best enn index:", best_ep_win_times_inx
        best_player = enn_players[best_ep_win_times_inx]
        best_player.show_enn_player_info()
        best_player.evolution_times += 1
        print "generation %d finished."%(best_player.evolution_times)
        print

        f = open(file_name,"w")
        pickle.dump(best_player, f)
        f.close()

        new_enn_player = EnnPlayer(enn = best_player.enn, evolution_times=best_player.evolution_times)
        # new_enn_player.enn.show_structure()
        print "enn connections:", new_enn_player.enn.connection_num

        if best_ep_win_times == 0:
            enn_players = [EnnPlayer(ttt.ROW, ttt.COL, ttt.WIN_NUM) for i in range(10)]
        elif g < generations - 1:
            enn_players = [new_enn_player]
            for i in range(9):
                sme_enn_player = copy.deepcopy(new_enn_player)
                sme_enn_player.small_evolve()
                enn_players.append(EnnPlayer(enn = sme_enn_player.enn, evolution_times=sme_enn_player.evolution_times))

def test_enn():
    ROW = 3
    COL = 3
    WIN_NUM = 3

    # file_name = "EnnPlayer_27_4_10_9.data"
    # f = open(file_name)
    # load_player = pickle.load(f)
    # f.close()
    # print "loaded data."
    # load_player.show_enn_player_info()

    enn_player = EnnPlayer(ROW, COL, WIN_NUM, hand_make_enn=True, player=1)
    ttt = Tictactoe(times=1000, enn_player=enn_player)
    ttt.setDaemon(True)
    ttt.start()
    ttt.join()
    print "generation: %d"%(enn_player.evolution_times + 1)
    enn_player.show_enn_player_info()

# main(load=True)
# main()
test_enn()