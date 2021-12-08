### In this file we will construct the game board which is needed to track the moves of the players ###

## important information on encodings - must read to understand the code below ##
# Encoding for players: Red 1, Blue 2, Yellow 3, Green 4
# Encoding of pieces: Pawn 1, Rook 2, Knight 3, Bishop 4, Queen 5, King 6
## ##

# coordinates a-n left to right, 1-14 bottom-up
# 14x14 board while each 3x3 corner is not playable

player_encoding = {1:"red", 2:"blue", 3:"yellow", 4:"green"}

def initial_board():
    ## construct initial board ##
    cols = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
    rows = range(1,15)[::-1]
    # board is stored as a dictionary, each field is a key-value-pair filled with figure and color codes
    # if a figure is placed on it, and with [0,0] if it is empty
    b = {}
    # construct empty board
    for r in rows:
        for c in cols:
            b[f"{c}{r}"]=[0,0]
    # fill the board with the figures
    # yellow color, first row
    b["d14"], b["k14"] = [2,3], [2,3]
    b["e14"], b["j14"] = [3,3], [3,3]
    b["f14"], b["i14"] = [4,3], [4,3]
    b["g14"] = [6,3]
    b["h14"] = [5,3]

    # blue color, first column
    b["a11"], b["a4"] = [2, 2], [2, 2]
    b["a10"], b["a5"] = [3, 2], [3, 2]
    b["a9"], b["a6"] = [4, 2], [4, 2]
    b["a8"] = [5, 2]
    b["a7"] = [6, 2]

    # red color, first row
    b["d1"], b["k1"] = [2,1], [2,1]
    b["e1"], b["j1"] = [3,1], [3,1]
    b["f1"], b["i1"] = [4,1], [4,1]
    b["g1"] = [5,1]
    b["h1"] = [6,1]

    # green color, first column
    b["n11"], b["n4"] = [2, 4], [2, 4]
    b["n10"], b["n5"] = [3, 4], [3, 4]
    b["n9"], b["n6"] = [4, 4], [4, 4]
    b["n8"] = [5, 4]
    b["n7"] = [6, 4]

    # yellow color, pawn row
    for c in cols[3:11]:
        b[f"{c}13"] = [1,3]

    # blue color, pawns column
    for r in rows[3:11]:
        b[f"b{r}"] = [1,2]

    # green color, pawns column
    for r in rows[3:11]:
        b[f"m{r}"] = [1,4]

    # red color, pawns column
    for c in cols[3:11]:
        b[f"{c}2"] = [1,1]
    # now delete obsolete corners, which are not playable
    corners = []
    for i in range(1, 4):
        for c in "abc":
            corners += [f"{c}{i}"]
        for c in "lmn":
            corners += [f"{c}{i}"]

    for i in range(12, 15):
        for c in "abc":
            corners += [f"{c}{i}"]
        for c in "lmn":
            corners += [f"{c}{i}"]

    for i in corners:
        del b[i]

    return b


def clean_moves(moves):
    # this functions "cleans up" the moves
    # possible moves formats: Nj1-i3 (normal, N = Knight), Nj1xQi3 (Knight beats queen),
    # # Nj1-i3+, Nj1-i3#, Nj1xi3+#, Nj1-i3+#, j1-i3=Q, O-O, R, S, T
    # output: [['e2', 'g1'], ['b4', 'h14'], ['d13', 'd11']...]
    moves = [moves[i].replace("x", "-").split("-") for i in range(len(moves))]
    #print(moves)
    for i in range(len(moves)):
        if (len(moves[i]) == 1):
            moves[i] = "dropped"
        for j in range(len(moves[i])):
            if type(moves[i]) != str:
                moves[i][j] = moves[i][j].replace("+", "")
                moves[i][j] = moves[i][j].replace("#", "")
                moves[i][j] = moves[i][j].replace("=Q", "")
                if moves[i][j][0].isupper() and moves[i][j] != "O": # remove piece name, not needed
                    moves[i][j] = moves[i][j][1:]
    #print(moves)
    return moves

def perform_castling(board, castling_move):
    # which castling move:
    # queenside castling
    if castling_move == ["O", "O", "O"]:
        # check which player can castle
        # player 1 red
        if (board["d1"] == [2, 1]) and (not any([sum(board["e1"]), sum(board["f1"]), sum(board["g1"])])) and board["h1"] == [6, 1]:
            board["f1"], board["g1"] = board["h1"], board["d1"]
            board["d1"], board["h1"] = [0,0], [0,0]
            return 1
        # player 2 blue
        elif (board["a4"] == [2, 2]) and (not any([sum(board["a5"]), sum(board["a6"]), sum(board["a7"])])) and board["a8"] == [6, 2]:
            board["a6"], board["a7"] = board["a8"], board["a4"]
            board["a4"], board["a8"] = [0,0], [0,0]
            return 2
        # player 3 yellow
        if (board["k14"] == [2, 3]) and (not any([sum(board["j14"]), sum(board["i14"]), sum(board["h14"])])) and board["g14"] == [6, 3]:
            board["i14"], board["h14"] = board["g14"], board["k14"]
            board["k14"], board["g14"] = [0, 0], [0, 0]
            return 3
        # player 4 green
        elif (board["n11"] == [2, 4]) and (not any([sum(board["n10"]), sum(board["n9"]), sum(board["n8"])])) and board["n7"] == [6, 4]:
            board["n9"], board["n8"] = board["n7"], board["n11"]
            board["n7"], board["n11"] = [0, 0], [0, 0]
            return 4
    # kingside castling
    elif castling_move == ["O", "O"]:
        # player 1 red
        if (board["k1"] == [2, 1]) and (not any([sum(board["j1"]), sum(board["i1"])])) and board["h1"] == [6, 1]:
            board["j1"], board["i1"] = board["h1"], board["k1"]
            board["h1"], board["k1"] = [0, 0], [0, 0]
            return 1
        # player 2 blue
        elif (board["a11"] == [2, 2]) and (not any([sum(board["a10"]), sum(board["a9"])])) and board["a8"] == [6, 2]:
            board["a10"], board["a9"] = board["a8"], board["a11"]
            board["a11"], board["a8"] = [0, 0], [0, 0]
            return 2
        # player 3 yellow
        if (board["d14"] == [2, 3]) and (not any([sum(board["e14"]), sum(board["f14"])])) and board["g14"] == [6, 3]:
            board["e14"], board["f14"] = board["g14"], board["d14"]
            board["d14"], board["g14"] = [0, 0], [0, 0]
            return 3
        # player 4 green
        elif (board["n4"] == [2, 4]) and (not any([sum(board["n5"]), sum(board["n6"])])) and board["n7"] == [6, 4]:
            board["n5"], board["n6"] = board["n7"], board["n4"]
            board["n4"], board["n7"] = [0, 0], [0, 0]
            return 4
    else:
        print("Castling condition not fulfilled!")

def check_kings(board):
    dropped = []
    # check if any kings are not on the board anymore
    kings = ([6,1], [6,2], [6,3], [6,4])
    for k in kings:
        if k not in board.values():
            dropped.append(k[1])
            #print(f"The King of player {k[1]} is not on the board anymore. Player {k[1]} dropped out.")
    return dropped

def check_dropped(board, moves):
    # check if any player did not take a move that turn
    moves_clean = clean_moves(moves)
    dropped = [] # keep record of dropped players each round
    players = [] # keep track of players still in game each round
    for i in range(len(moves_clean)):
        if moves_clean[i] != "dropped":
            if moves_clean[i] == ["O", "O"]:
                castled = perform_castling(board, moves_clean[i])
                moves[i] = "kcastling"
                players.append(castled)
            elif moves_clean[i] == ["O", "O", "O"]:
                castled = perform_castling(board, moves_clean[i])
                moves[i] = "qcastling"
                players.append(castled)
            else:
                players.append(board[moves_clean[i][0]][1])
    not_moved = list(set([1,2,3,4]) - set(players)) # get players who did not make a move
    if not_moved != []:
        #print(f"Player(s) {not_moved} did not make a move this turn and dropped out of the game.")
        dropped += not_moved # add missing players
    dropped += list(set(check_kings(board)) - set(dropped)) # also count in missing kings (but no player twice)
    return dropped


def mk_move(moves, board):
    # change board according to moves
    moves = clean_moves(moves) # clean moves
    dropped = check_dropped(board, moves) # check dropped players
    for i in range(len(moves)):
        if "castling" not in moves[i] and moves[i] != "dropped":
            board[moves[i][0]], board[moves[i][1]] = [0, 0], board[moves[i][0]]
    dropped += list(set(check_kings(board, dropped)) - set(dropped)) # check kings after moves were made again
    #if dropped != []:
        #print("Dropped players: ")
        #for i in dropped:
        #    print(player_encoding[i]) # print player colors
    return board


moves = ["e2-e4", "Qb4xNd4", "Nd13-d11+#", "Km7-k7#"]
moves2 = ["Nj1-i3", "k8-j9=Q", "Nj1-h14+", "Nj1xg1+#"]
moves3 = ["e2-e4", "Qb4xNd4", "Nd13-d11+#"]
moves4 = ["e2-g1", "b4-h14", "d13-d11"]
moves5 = ["O-O-O", "R", "T", "m11-l11"] # tests castling and dropped players by timeout and R
#b = mk_move(moves, b) # nobody drops
#b = mk_move(moves2, b) # tests only move formats, not dropped players
#b = mk_move(moves3, b) # player four makes no move, knowing by player who occupies field which was moved
#b = mk_move(moves4, b) # checks kings of player 1 and 2, while player four did not make a move
#b = initial_board()
#b["j1"], b["i1"] = [0,0], [0,0]
#b["g1"], b["f1"], b["e1"] = [0,0], [0,0], [0,0]
#print(not any([sum(b["g1"]), sum(b["f1"]), sum(b["e1"])]))
#(board["k1"] == [3, 1]) and (not any([sum(board["j1"]), sum(board["i1"])])) and board["h1"] == [6, 1]
#print(b["d1"] == [2, 1])
#print(b["h1"] == [6, 1])

#b = mk_move(moves5, b)

