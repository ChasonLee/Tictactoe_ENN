__author__ = 'GXK'
# coding:utf-8
import random

ROW = 3
COL = 3
WIN_NUM = 3
PLAYER1_NUM = 1
PLAYER2_NUM = 2
PLAYER1_CHAR = '#'
PLAYER2_CHAR = '*'
MAPS = '.'
AI = 0

board = [[0] * COL for i in range(ROW)]
# hist_board = [[[0] * COL for i in range(ROW)] for j in range(ROW * COL)]

empty_board = range(9)
param = [([0] * (ROW * COL * 2 + 1)) for i in range(ROW * COL)]
# param = [[-8194, 69334, 26538, 31294, 46964, 38172, 42240, 46234, 39412, 41684, 48714, 35892, 42790, 47014, 40254, 40100, 48964, 34328, 44022, 48334, 38728, 40300, 47294, 35442, 44600, 46894, 37938, -28440], [-33270, 20850, 12516, 13330, 40910, 800, 4990, 19860, 12400, 14450, 21660, 9400, 15650, 19630, 15150, 11930, 21640, 8740, 16330, 20080, 13590, 13040, 21030, 9670, 16010, 20310, 12370, -27820], [-8276, 46958, 36344, 40444, 46922, 35566, 41520, 67584, 26580, 29644, 48482, 33430, 42032, 45634, 39306, 39010, 48182, 34236, 41440, 45524, 38742, 39582, 47382, 32936, 43656, 45524, 38482, -29300], [-34856, 21116, 11926, 14892, 20706, 11428, 15930, 20916, 13328, 13840, 42416, -872, 6540, 19736, 15118, 13230, 22266, 10428, 15390, 20656, 14448, 12980, 21216, 10568, 16270, 20586, 12028, -27910], [10560, 66354, 54786, 60024, 66354, 54462, 60610, 66394, 54822, 60164, 67584, 52522, 61340, 87356, 47134, 46900, 67284, 51688, 62342, 65334, 56174, 59890, 65404, 52882, 63100, 65934, 55668, -29610], [-35476, 20368, 12438, 14450, 20368, 11874, 15050, 20728, 13064, 13500, 21958, 9964, 15370, 20448, 14014, 12830, 42328, -1476, 6440, 20828, 13074, 13390, 21888, 9554, 15830, 20448, 12594, -29040], [-6280, 47550, 36368, 42042, 46450, 36590, 43180, 46460, 38100, 41672, 48030, 35690, 42530, 45760, 40746, 39730, 48660, 34674, 42900, 67750, 28620, 29870, 47830, 35560, 42810, 47310, 37740, -28100], [-35730, 18290, 10010, 12510, 19000, 9100, 12710, 17860, 9360, 13590, 19810, 7740, 13260, 17470, 13040, 10300, 20020, 6950, 13840, 18000, 13000, 9810, 39150, -3060, 4710, 17750, 11810, -28800], [-18520, 39716, 28036, 32074, 38720, 28060, 33430, 38100, 30044, 31956, 40920, 25130, 34152, 38422, 32166, 29570, 40450, 25714, 33928, 38832, 29722, 31542, 38790, 26830, 34560, 60692, 18734, -41370]]
# param = [[942, -2026, -2380, 188, 280, 190, 274, 222, 272, 162, 238, 180, 322, 222, 230, 218, 350, 82, 282], [3622, 560, 512, -3686, -3618, 406, 578, 584, 640, 460, 482, 438, 776, 576, 540, 468, 666, 452, 582], [972, 160, 330, 218, 294, -2130, -2350, 222, 382, 258, 220, 130, 362, 186, 298, 234, 310, 242, 304], [5580, 1736, 1784, 1812, 1936, 1600, 1972, -2672, -2174, 1950, 1244, 1640, 2022, 1922, 1652, 1730, 1980, 1550, 1882], [1098, 212, 276, 236, 354, 162, 382, 252, 268, -2140, -2570, 120, 306, 206, 292, 218, 250, 124, 352], [970, 300, 304, 242, 326, 226, 290, 164, 466, 278, 218, -2298, -2540, 206, 364, 220, 410, 236, 346], [1056, 214, 338, 298, 296, 162, 386, 222, 288, 166, 308, 258, 360, -1922, -2500, 192, 374, 246, 306], [1014, 254, 316, 210, 344, 222, 312, 248, 370, 234, 270, 198, 420, 200, 330, -2434, -2730, 210, 290], [894, 204, 282, 196, 298, 190, 304, 256, 256, 120, 226, 212, 308, 168, 254, 118, 300, -2076, -2420]]

input_layer = [0] * (ROW * COL * 2 + 1)
hist_input_layer = []
output_layer = [0] * (ROW * COL)
hist_output = []

def InitBoard():
    global board
    global empty_board
    global hist_input_layer
    global hist_output
    board = [[0,0,0],[0,0,0],[0,0,0]]
    empty_board = range(9)
    hist_input_layer = []
    hist_output = []

def PrintPiece(inx):
    if inx == PLAYER1_NUM:
        print PLAYER1_CHAR,
    elif inx == PLAYER2_NUM:
        print PLAYER2_CHAR,
    else:
        print MAPS,

def ShowBoard():
    for i in board:
        for j in i:
            PrintPiece(j),
        print
    print

def Judge(r, c):
    player = board[r][c]
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
        elif i == 3:
            dr = 0
            dc = 1
        nr = r + dr
        nc = c + dc
        count = 1
        while nr >= 0 and nr < ROW and nc >= 0 and nc < COL:
            if board[nr][nc] == player:
                count = count + 1
                nr = nr + dr
                nc = nc + dc
            else:
                break
        dr = -dr
        dc = -dc
        nr = r + dr
        nc = c + dc
        while nr >= 0 and nr < ROW and nc >= 0 and nc < COL:
            if board[nr][nc] == player:
                count = count + 1
                nr = nr + dr
                nc = nc + dc
            else:
                break
        if count >= WIN_NUM:
            return player
    return

def ShowResult(res):
    if res == PLAYER1_NUM:
        print "Player(",PLAYER1_CHAR,") Wins!"
        return 1
    elif res == PLAYER2_NUM:
        print "Player(",PLAYER2_CHAR,") Wins!"
        return 1
    else:
        print "No one wins"
        return 0

def Move(r, c, player):
    if board[r][c] == 0:
        board[r][c] = player
        return 1
    else:
        return 0
def rnd_coordinate():
    res = -1
    n = len(empty_board)
    if n > 0:
        rnd = int(n * random.random())
        res = empty_board[rnd]
        empty_board.remove(res)
    return res / 3, res % 3
def rnd_coord():
    res = int(9 * random.random())
    return res / 3, res % 3
def Play_Rnd():
    for i in range(9):
        r, c = rnd_coordinate()
        if i % 2 == 0:
            Move(r, c, PLAYER1_NUM)
        else:
            Move(r, c, PLAYER2_NUM)
        # print r,c
        # ShowBoard()
        jd = Judge(r, c)
        if ShowResult(jd) == 1:
            break
    return jd
def Get_Layer():
    global input_layer
    global hist_input_layer
    inx = 0
    input_layer = [0] * (ROW * COL * 2 + 1)
    input_layer[0] = 1
    for i in board:
        for j in i:
            if j > 0:
                input_layer[inx * 2 + j] = 1
            inx += 1
    hist_input_layer.append(input_layer)
    # print 'input_layer:', input_layer

def Calc_Move():
    res_list = []
    for j in range(ROW * COL):
        sum = 0
        for i in range(ROW * COL * 2 + 1):
            sum += input_layer[i] * param[j][i]
        if sum >= 0:
            output_layer[j] = 1
            res_list.append(j)
        else:
            output_layer[j] = 0
    # print 'res_list:', res_list
    n = len(res_list)
    if n > 0:
        rnd = int(n * random.random())
        res = res_list[rnd]
    else:
        res = int(9 * random.random())
    return res / 3, res % 3

def Reward(r, c, k):
    global param
    global hist_input_layer
    global input_layer
    node = r * 3 + c
    if k == 0:
        for inx, inp in enumerate(input_layer):
            if inp == 1:
                param[node][inx] += 10
        # print '1_Reward:', param
        return
    for w, hist in enumerate(hist_input_layer):
        # print 'hist:', hist
        # print 'hist_output:', hist_output
        for inx, inp in enumerate(hist):
            if inp == 1 and (inx % 2 == (1 - AI) or inx == 0):
                param[hist_output[w]][inx] += (w + 1) ** 3
    # print 'Reward:', param
def Punish(r, c, k):
    global param
    global hist_input_layer
    global input_layer
    node = r * 3 + c
    if k == 0:
        for i in range(node * 2 + 1, node * 2 + 2 + 1):
            if input_layer[i] == 1:
                param[node][i] -= 10
        # print '1_Punish:', param
        return
    for w, hist in enumerate(hist_input_layer):
        # print 'hist:', hist
        # print 'hist_output:', hist_output
        for inx, inp in enumerate(hist):
            if inp == 1 and (inx % 2 == AI or inx == 0):
                param[hist_output[w]][inx] -= (w + 1) ** 5
    # print 'Punish:', param

def Play_Learn():
    global hist_output
    for i in range(9):
        r, c = Calc_Move()
        rr, cc = rnd_coordinate()
        if i % 2 == AI:
            Get_Layer()
            while Move(r, c, PLAYER1_NUM) == 0:
                # print '-(', r, ',', c, ')-'
                Punish(r, c, 0)
                r, c = Calc_Move()
            hist_output.append(r * 3 + c)
            # print '(', r, ',', c, ')'
        else:
            while Move(rr, cc, PLAYER2_NUM) == 0:
                rr, cc = rnd_coord()
            # print '(', rr, ',', cc, ')'
        # ShowBoard()
        jd = Judge(r, c)
        if jd == 1:
            ShowResult(jd)
            Reward(r, c, 1)
            break
        elif jd == 2:
            ShowResult(jd)
            Punish(r, c , 1)
            break
        else:
            ShowResult(jd)
            pass
    return jd
def main():
    # InitBoard()
    # ShowBoard()
    # Play_Rnd()
    wins = 0
    loses = 0
    draw = 0
    for i in range(10000):
        InitBoard()
        print '****************************************Begin!****************************************'
        ShowBoard()
        res = Play_Learn()
        # res = Play_Rnd()
        if res == 1:
            wins += 1
        elif res == 2:
            loses += 1
        else:
            draw += 1

    print 'param:', param
    print 'wins:', wins
    print 'loses:', loses
    print 'draw:', draw
    # node1[2] = 2
    # print node1
    # hist_board[1][1][1] = 1
    # print hist_board
    return 0


main()