### In this file we will construct the game board which is needed to track the moves of the players
### Furthermore, functions are built to run through the data, recreate piece movements, store dropped and active
### players and return the state of the board after each round.

## important information on encodings
# Encoding for players: Red 1, Blue 2, Yellow 3, Green 4
# Encoding of pieces: Pawn 1, Rook 2, Knight 3, Bishop 4, Queen 5, King 6, Promoted Rook 7, prom. Knight 8, prom. Bishop 9, prom. Queen 10
##

# coordinates a-n left to right, 1-14 bottom-up
# 14x14 board while each 3x3 corner is not playable

player_encoding = {1: "red", 2: "blue", 3: "yellow", 4: "green"}


def add_dropped_active(chess_data):
    # this function adds two new lists to each game. The lists are used to track dropped and active players.
    for g in chess_data["data"]:
        g["dropped_players"] = []
        g["active_players"] = [1, 2, 3, 4]
    return chess_data

def delete_corners(board):
    # fucntion to delete obsolete corners, which are not playable
    # the function is currently not in use as the CNN will need the whole 14x14 board as a matrix input
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
    cols = [chr(i) for i in range(97, 111)]  # get characters a - n
    rows = range(1, 15)[::-1]
    # board is stored as a dictionary, each field is a key-value-pair filled with figure and color codes
    # if a figure is placed on it, and with [0,0] if it is empty
    b = {}
    # construct empty board
    for r in rows:
        for c in cols:
            b[f"{c}{r}"] = [0, 0]
    # fill the board with the figures
    # yellow color, first row
    b["d14"], b["k14"] = [2, 3], [2, 3]  # place the rooks
    b["e14"], b["j14"] = [3, 3], [3, 3]  # knights
    b["f14"], b["i14"] = [4, 3], [4, 3]  # bishops
    b["g14"] = [6, 3]  # king
    b["h14"] = [5, 3]  # queen

    # blue color, first column
    b["a11"], b["a4"] = [2, 2], [2, 2]
    b["a10"], b["a5"] = [3, 2], [3, 2]
    b["a9"], b["a6"] = [4, 2], [4, 2]
    b["a8"] = [6, 2]
    b["a7"] = [5, 2]

    # red color, first row
    b["d1"], b["k1"] = [2, 1], [2, 1]
    b["e1"], b["j1"] = [3, 1], [3, 1]
    b["f1"], b["i1"] = [4, 1], [4, 1]
    b["g1"] = [5, 1]
    b["h1"] = [6, 1]

    # green color, first column
    b["n11"], b["n4"] = [2, 4], [2, 4]
    b["n10"], b["n5"] = [3, 4], [3, 4]
    b["n9"], b["n6"] = [4, 4], [4, 4]
    b["n8"] = [5, 4]
    b["n7"] = [6, 4]

    # king's initial positions: b["h1"], b["a8"] b["g14"], b["n7"]

    # yellow color, pawn row
    for c in cols[3:11]:
        b[f"{c}13"] = [1, 3]

    # blue color, pawns column
    for r in rows[3:11]:
        b[f"b{r}"] = [1, 2]

    # green color, pawns column
    for r in rows[3:11]:
        b[f"m{r}"] = [1, 4]

    # red color, pawns column
    for c in cols[3:11]:
        b[f"{c}2"] = [1, 1]

    return b
# test case: check every piece of every player

def clean_moves(board, moves, active_players):
    b = board
    # this functions "cleans up" the moves
    # possible moves formats: Nj1-i3 (normal, N = Knight), Nj1xQi3 (Knight beats queen),
    # # Nj1-i3+, Nj1-i3#, Nj1xi3+#, Nj1-i3+#, j1-i3=Q, O-O, O-O-O, R, S, T
    # replace x with - and split on -
    cleaned = [moves[i].replace("x", "-").split("-") for i in range(len(moves))]
    # output: [['Ne2', 'g1+'], ['b4', 'h14+#'], ['d13', 'd11=Q']...]
    # now delete +, #, =Q, T, R and S
    # go through cleaned, which is a list of lists
    # list comprehension covers several identical entries, for example two timeouts in one round
    if ["T"] in cleaned:
        player_nr = active_players[cleaned.index(["T"])] # get which player had timeout
        if [6, player_nr] in board.values():

            king_position = [key for key,value in board.items() if value == [6, player_nr]] # store the player's king
            # position
            # now take the king and do not move it, as it might move randomly in the next rounds. Timeouts do not
            # necessarily mean that a player drops out immediately. His/her king might still move around randomly although
            # being dead.
            cleaned = [[king_position[0], king_position[0]] if move == ["T"] else move for move in cleaned]
            #print(player_nr)
            #print(king_position)
            #print(board)
            #print(cleaned)
        else:
            cleaned = [move for move in cleaned if move != ["T"]]
    if ["R"] in cleaned:
        player_nr = active_players[cleaned.index(["R"])] # get which player had timeout
        if [6, player_nr] in board.values():

            king_position = [key for key,value in board.items() if value == [6, player_nr]] # store the player's king
            # position
            # now take the king and do not move it, as it might move randomly in the next rounds. Timeouts do not
            # necessarily mean that a player drops out immediately. His/her king might still move around randomly although
            # being dead.
            cleaned = [[king_position[0], king_position[0]] if move == ["R"] else move for move in cleaned]
        else:
            cleaned = [move for move in cleaned if move != ["R"]]
    if ["S"] in cleaned:
        player_nr = active_players[cleaned.index(["S"])] # get which player had timeout
        if [6, player_nr] in board.values():

            king_position = [key for key,value in board.items() if value == [6, player_nr]] # store the player's king
            # position
            # now take the king and do not move it, as it might move randomly in the next rounds. Timeouts do not
            # necessarily mean that a player drops out immediately. His/her king might still move around randomly although
            # being dead.
            cleaned = [[king_position[0], king_position[0]] if move == ["S"] else move for move in cleaned]
        else:
            cleaned = [move for move in cleaned if move != ["S"]]
    # in game nr 12243 there is a move called RS
    if ["RS"] in cleaned:
        cleaned = [move for move in cleaned if move != ["RS"]]
    # some games later there is move called TS
    if ["TS"] in cleaned:
        cleaned = [move for move in cleaned if move != ["TS"]]
    # also in some old games we have moves in the following formats: R#, T#
    if ["R#"] in cleaned:
        cleaned = [move for move in cleaned if move != ["R#"]]
    if ["T#"] in cleaned:
        cleaned = [move for move in cleaned if move != ["T#"]]

    if len(cleaned) == 0:
        # if there are no more moves left, we return the board and the empty list
        return board, cleaned
    for i in range(len(cleaned)):  # 0 to 4 typically
        for j in range(len(cleaned[i])): # 0 to 1, or 0 to 2 in queenside castling move
            cleaned[i][j] = cleaned[i][j].replace("+", "")
            cleaned[i][j] = cleaned[i][j].replace("#", "")
            if "=R" in cleaned[i][j]:
                # [["a11", "a12=R"],...]
                b[cleaned[i][0]][0] = 7
                cleaned[i][j] = cleaned[i][j].replace("=R", "")
            elif "=N" in cleaned[i][j]:
                b[cleaned[i][0]][0] = 8
                cleaned[i][j] = cleaned[i][j].replace("=N", "")
            elif "=B" in cleaned[i][j]:
                b[cleaned[i][0]][0] = 9
                cleaned[i][j] = cleaned[i][j].replace("=B", "")
            elif "=Q" in cleaned[i][j]:
                b[cleaned[i][0]][0] = 10
                cleaned[i][j] = cleaned[i][j].replace("=Q", "")
            elif "=D" in cleaned[i][j]: # in older games it states =D for queen promotion
                b[cleaned[i][0]][0] = 10
                cleaned[i][j] = cleaned[i][j].replace("=D", "")
            # in older games there are moves in the following format: "O-OR", "O-OT"
            if "OT" in cleaned[i][j]:
                cleaned[i][j] = cleaned[i][j].replace("OT", "O")
            if "OR" in cleaned[i][j]:
                cleaned[i][j] = cleaned[i][j].replace("OR", "O")

            # in some older games, there exists a move in the format
            # of "i3-i2R". That R, sometimes also a T, in the end does not seem to have any particular significance.
            if cleaned[i][j][-1].isupper() and cleaned[i][j][0] != "O":
                cleaned[i][j] = cleaned[i][j][:-1]

            # next, cover pawn promotions
            # remove piece information, as it is not needed for the our purposes
            if cleaned[i][j][0].isupper() and cleaned[i][j][0] != "O":
                cleaned[i][j] = cleaned[i][j][1:]
    return b, cleaned


def perform_castling(board, castling_move, player_nr):
    # this function performes queenside and kingside castling.
    # it needs to know the player which is performing the castling move. for that it uses the index on
    # currently active players.
    if castling_move == ["O", "O", "O"]:  # queenside castling
        if player_nr == 1: # red player...
            board["f1"], board["g1"] = board["h1"], board["d1"]
            board["d1"], board["h1"] = [0, 0], [0, 0]

        elif player_nr == 2:
            board["a6"], board["a7"] = board["a8"], board["a4"]
            board["a4"], board["a8"] = [0, 0], [0, 0]

        elif player_nr == 3:
            board["i14"], board["h14"] = board["g14"], board["k14"]
            board["k14"], board["g14"] = [0, 0], [0, 0]

        elif player_nr == 4:
            board["n9"], board["n8"] = board["n7"], board["n11"]
            board["n7"], board["n11"] = [0, 0], [0, 0]

    elif castling_move == ["O", "O"]:  # kingside castling
        if player_nr == 1:
            board["j1"], board["i1"] = board["h1"], board["k1"]
            board["h1"], board["k1"] = [0, 0], [0, 0]

        elif player_nr == 2:
            board["a10"], board["a9"] = board["a8"], board["a11"]
            board["a11"], board["a8"] = [0, 0], [0, 0]

        elif player_nr == 3:
            board["e14"], board["f14"] = board["g14"], board["d14"]
            board["d14"], board["g14"] = [0, 0], [0, 0]

        elif player_nr == 4:
            board["n5"], board["n6"] = board["n7"], board["n4"]
            board["n4"], board["n7"] = [0, 0], [0, 0]
    return board

def mk_move(game):
    # this function will track the moves and update the board each round
    # it also keeps track of active and dropped players and gives the input to the castling function
    for g in game["data"]: # go through each game
        board = initial_board()  # construct new board at the beginning of each game
        #if game['data'].index(g) < 15915:
        #    continue
        print(f"Game #{game['data'].index(g)}")  # print game number
        # at the start of each game, all the players are active and none has dropped
        g["active_players"] = [1,2,3,4]
        g["dropped_players"] = []
        for r in g["Rounds"]: # go through each round
            #print("Raw Moves")
            #print(r["Moves"])
            #print(r["Moves"])
            board, moves = clean_moves(board, r["Moves"], g["active_players"])  # clean moves, return board after potential pawn promotion
            # sample output: [["e2", "e4"], ["g14", "i14"], ["O", "O", "O"], ...]
            # no move has been made until now, also no castling
            #print("Clean Moves:")
            #print(moves)
            currently_active_players = [] # reset the list of active players and update it each round
            for i in range(len(moves)): # go through each player's moves
                if moves[i] == ["O", "O"]: # if kingside castling
                    #print("now castling")
                    #print(g["active_players"])
                    player_nr = g["active_players"][i] # use index of move on active players list from last round
                    board = perform_castling(board, ["O", "O"], player_nr) # perform castling move
                    currently_active_players.append(player_nr) # add the player to the currently active players list
                elif moves[i] == ["O", "O", "O"]: # queenside castling
                    # same procedure as above
                    #print("now castling")
                    #print(g["active_players"])
                    player_nr = g["active_players"][i]
                    board = perform_castling(board, ["O", "O", "O"], player_nr)
                    currently_active_players.append(player_nr)
                else: # if no castling move is being made
                    #print(moves)
                    #print(moves[i])
                    if board[moves[i][1]][0] == 6 and moves[i][0] != moves[i][1]:
                        # if castling happens in the same round as some player has dropped out and there has not been a timeout,
                        # we check if a player's king has been kicked out so we do not get a wrong index for
                        # the castling move.
                        player_nr = board[moves[i][1]][1] # store the player number of the player who has dropped by
                        # fallen king
                        if player_nr not in g["dropped_players"]: # add that player to the dropped players list
                            # if not already there
                            g["dropped_players"].append(player_nr)
                        #if player_nr in g["active_players"]: # remove the dropped player from the active player list
                        #    # if not already missing
                        #    g["active_players"].remove(player_nr)
                    # if there's no king being kicked out during this round, perform the normal move
                    board[moves[i][0]], board[moves[i][1]] = [0, 0], board[moves[i][0]] # change positions of the
                    # moved pieces and add the player performing the move to the currently active players list
                    currently_active_players.append(board[moves[i][1]][1])
            # after each round update the dropped and active players list

            # active player from last round (1,2,3,4) - currently active players form this round (e.g. 1,3,4)
            g["dropped_players"] += list(set(g["active_players"]) - set(currently_active_players))
            # remove duplicates
            g["dropped_players"] = list(set(g["dropped_players"]))
            # sort dropped players list for correct insertion of placeholders
            g["dropped_players"].sort()
            # update active players list
            g["active_players"] = currently_active_players

            # here we insert empty strings at the place of the dropped player
            # also at times we insert a placeholder value of 0
            if len(g["dropped_players"]) > 0:
                for p in g["dropped_players"]:
                    r["Moves"].insert(p-1, "") # insert at index player number (1,2,3,4) - 1 (0,1,2,3)
                    r["Times"].insert(p-1, 0)

            # print board for the CNN
            #print(board)

            #print("Active players")
            #print(g["active_players"])
            #print("Dropped players")
            #print(g["dropped_players"])
            #print(g["Rounds"])
    return game

import json

# test with actual data
f = open("../solo_pretty.json")
data = json.load(f)
# print(len(data["data"])) # 16625

data = add_dropped_active(data)
#print(data["data"][0])
mk_move(data)

# write output to json file "algorithm_output.json
#with open('algorithm_output_testS.json','w') as output :
#    json.dump(data,output)
