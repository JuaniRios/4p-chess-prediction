### In this file we will construct the game board which is needed to track the moves of the players ###

## important information on encodings - must read to understand the code below ##
# Encoding for players: Red 1, Blue 2, Yellow 3, Green 4
# Encoding of pieces: Pawn 1, Rook 2, Knight 3, Bishop 4, Queen 5, King 6
## ##

# coordinates a-n left to right, 1-14 bottom-up
# 14x14 board while each 3x3 corner is not playable

player_encoding = {1:"red", 2:"blue", 3:"yellow", 4:"green"}

def delete_corners(board):
    # fucntion to delete obsolete corners, which are not playable
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
        del board[i]

    return board
# test case: check if every unplayable field is deleted

def initial_board():
    ## construct initial board ##
    cols = [chr(i) for i in range(97,111)] # get characters a - n
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
    b["d14"], b["k14"] = [2,3], [2,3] # place the rooks
    b["e14"], b["j14"] = [3,3], [3,3] # knights
    b["f14"], b["i14"] = [4,3], [4,3] # bishops
    b["g14"] = [6,3] # king
    b["h14"] = [5,3] # queen

    # blue color, first column
    b["a11"], b["a4"] = [2, 2], [2, 2]
    b["a10"], b["a5"] = [3, 2], [3, 2]
    b["a9"], b["a6"] = [4, 2], [4, 2]
    b["a8"] = [6, 2]
    b["a7"] = [5, 2]

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

    # king's initial positions: b["h1"], b["a8"] b["g14"], b["n7"]

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

    return delete_corners(b) # delete obsolete, non-playable fields on the corners

# test case: check every piece of every player

def clean_moves(board, moves):
    # this functions "cleans up" the moves
    # possible moves formats: Nj1-i3 (normal, N = Knight), Nj1xQi3 (Knight beats queen),
    # # Nj1-i3+, Nj1-i3#, Nj1xi3+#, Nj1-i3+#, j1-i3=Q, O-O, R, S, T
    # replace x with dash and split on -
    cleaned = [moves[i].replace("x", "-").split("-") for i in range(len(moves))]
    # output: [['e2', 'g1'], ['b4', 'h14'], ['d13', 'd11']...]
    # print(moves)
    # now delete +, # and =Q
    # go through cleaned, which is a list of lists
    for i in range(len(cleaned)): # 0 to 4 typically
        if (len(cleaned[i]) == 1):
            # moves and cleaned have same length, one is list of strings, the other one is list of lists
            # if list with one move contains only one item ("R", "T", "S"), player drops
            moves[i] = "dropped" # "R" becomes "dropped"
            cleaned[i] = "dropped"
        else:
            for j in range(len(cleaned[i])):
                # go through each move eg. ["e2", "e4"]
                if "dropped" not in moves[i]:
                    # if it is not "dropped" already
                    cleaned[i][j] = cleaned[i][j].replace("+", "")
                    cleaned[i][j] = cleaned[i][j].replace("#", "")
                    cleaned[i][j] = cleaned[i][j].replace("=Q", "")
                    if cleaned[i][j][0].isupper() and cleaned[i][j] != "O": # remove piece name, if no castling
                        cleaned[i][j] = cleaned[i][j][1:]
                    elif cleaned[i] == ["O", "O", "O"] or cleaned[i] == ["O","O"]:
                        cleaned[i] = check_castling(board, cleaned[i]) # manipulate move so we see which player
                        # made the move and to later on be able to perform castling
        #print(moves)
        return cleaned


def getPlayers(board, cleaned_moves):
    # this function is done before castling is performed and after it has been checked!
    players = []
    for m in cleaned_moves: # [["e2", "e4"], ...]
        players.append(board[m[0]][1]) # board["e2"][1] which gives player number

def check_castling(board, castling_move):
    # function to perform the two castling moves
    # moves were cleaned beforehand already
    # we perform castling before we check who dropped
    # we should change the cleaned castling move to "kcastling" or "qcastling" WHY???
    # queenside castling
    if castling_move == ["O", "O", "O"]:
        # check which player can castle
        # player 1 red
        if (board["d1"] == [2, 1]) and (not any([sum(board["e1"]), sum(board["f1"]), sum(board["g1"])])) and board[
            "h1"] == [6, 1]:
            #board["f1"], board["g1"] = board["h1"], board["d1"]
            #board["d1"], board["h1"] = [0, 0], [0, 0]
            return ["h1", "f1"] # we return the move of the king. As the king can normally only move one tile,
            # we detect that castling was done. We return the move as we can later on determine more easily which
            # player has moved a piece this turn.
            # NOW THE MOVE HAS ALREADY BEEN MADE
            # in mk_move when we see this move, we perform castling!
        # player 2 blue
        elif (board["a4"] == [2, 2]) and (not any([sum(board["a5"]), sum(board["a6"]), sum(board["a7"])])) and \
                board["a8"] == [6, 2]:
            #board["a6"], board["a7"] = board["a8"], board["a4"]
            #board["a4"], board["a8"] = [0, 0], [0, 0]
            return ["a8", "a6"]
        # player 3 yellow
        if (board["k14"] == [2, 3]) and (not any([sum(board["j14"]), sum(board["i14"]), sum(board["h14"])])) and \
                board["g14"] == [6, 3]:
            #board["i14"], board["h14"] = board["g14"], board["k14"]
            #board["k14"], board["g14"] = [0, 0], [0, 0]
            return ["g14", "i14"]
        # player 4 green
        elif (board["n11"] == [2, 4]) and (not any([sum(board["n10"]), sum(board["n9"]), sum(board["n8"])])) and \
                board["n7"] == [6, 4]:
            #board["n9"], board["n8"] = board["n7"], board["n11"]
            #board["n7"], board["n11"] = [0, 0], [0, 0]
            return ["n7", "n9"]

    # kingside castling
    elif castling_move == ["O", "O"]:
        # player 1 red
        if (board["k1"] == [2, 1]) and (not any([sum(board["j1"]), sum(board["i1"])])) and board["h1"] == [6, 1]:
            #board["j1"], board["i1"] = board["h1"], board["k1"]
            #board["h1"], board["k1"] = [0, 0], [0, 0]
            return ["h1", "j1"]
        # player 2 blue
        elif (board["a11"] == [2, 2]) and (not any([sum(board["a10"]), sum(board["a9"])])) and board["a8"] == [6,
                                                                                                               2]:
            #board["a10"], board["a9"] = board["a8"], board["a11"]
            #board["a11"], board["a8"] = [0, 0], [0, 0]
            return ["a8", "a10"]
        # player 3 yellow
        if (board["d14"] == [2, 3]) and (not any([sum(board["e14"]), sum(board["f14"])])) and board["g14"] == [6,
                                                                                                               3]:
            #board["e14"], board["f14"] = board["g14"], board["d14"]
            #board["d14"], board["g14"] = [0, 0], [0, 0]
            return ["g14", "e14"]
        # player 4 green
        elif (board["n4"] == [2, 4]) and (not any([sum(board["n5"]), sum(board["n6"])])) and board["n7"] == [6, 4]:
            #board["n5"], board["n6"] = board["n7"], board["n4"]
            #board["n4"], board["n7"] = [0, 0], [0, 0]
            return ["n7", "n5"]
    else:
        print("Castling condition not fulfilled!")
        return None

def perform_castling(board, cleaned_castling_move):
    # this function will be called within the mk_move function
    # until now castling was not performed!
    if cleaned_castling_move == ["h1", "f1"]:
        board["f1"], board["g1"] = board["h1"], board["d1"]
        board["d1"], board["h1"] = [0, 0], [0, 0]

    elif cleaned_castling_move == ["a8", "a6"]:
        board["a6"], board["a7"] = board["a8"], board["a4"]
        board["a4"], board["a8"] = [0, 0], [0, 0]

    elif cleaned_castling_move == ["g14", "i14"]:
        board["i14"], board["h14"] = board["g14"], board["k14"]
        board["k14"], board["g14"] = [0, 0], [0, 0]

    elif cleaned_castling_move == ["n7", "n9"]:
        board["n9"], board["n8"] = board["n7"], board["n11"]
        board["n7"], board["n11"] = [0, 0], [0, 0]

    elif cleaned_castling_move == ["h1", "j1"]:
        board["j1"], board["i1"] = board["h1"], board["k1"]
        board["h1"], board["k1"] = [0, 0], [0, 0]

    elif cleaned_castling_move ==["a8", "a10"]:
        board["a10"], board["a9"] = board["a8"], board["a11"]
        board["a11"], board["a8"] = [0, 0], [0, 0]

    elif cleaned_castling_move ==["g14", "e14"]:
        board["e14"], board["f14"] = board["g14"], board["d14"]
        board["d14"], board["g14"] = [0, 0], [0, 0]

    elif cleaned_castling_move ==["n7", "n5"]:
        board["n5"], board["n6"] = board["n7"], board["n4"]
        board["n4"], board["n7"] = [0, 0], [0, 0]

    return board