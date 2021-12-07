### This file includes the necessary functions to create a 4 Player Chess Game Board. The board is needed
### to keep track of the gameplay and of the dropped players within a game. I.e., functions are built to run through
### the data, emulate piece movements, store dropped and active players and return the state of the board after
### each round.

## important information on encodings
# Encoding for players: Red 1, Blue 2, Yellow 3, Green 4
# Encoding of pieces: Pawn 1, Rook 2, Knight 3, Bishop 4, Queen 5, King 6, Promoted Rook 7, prom. Knight 8,
# prom. Bishop 9, prom. Queen 10

# coordinates a-n: left to right; 1-14: bottom-up
# 14x14 board while each 3x3 corner is not playable

def add_dropped_active(games):
    '''This function adds two new lists "dropped_players" and "active_players". The purpose of these lists is
    to keep track of the dropped and still active players within a game. Hence, dropped_players = [] and
    active_players = [1, 2, 3, 4] at the beginning of each game. They will be manipulated while a game is being
    processed.'''
    for g in games:
        g["dropped_players"] = []
        g["active_players"] = [1, 2, 3, 4]
    return games

def delete_corners(board):
    '''Function to delete the unplayable corners of a 14x14 sized dictionary serving as a 4PChess board. The function
    is currently not in use as most algorithms will need the whole 14x14 board as a matrix input'''
    corners = []
    for i in range(1, 4):
        for c in "abc":
            corners += [f"{c}{i}"] # a1 - c3
        for c in "lmn":
            corners += [f"{c}{i}"] # l1 - n4

    for i in range(12, 15):
        for c in "abc":
            corners += [f"{c}{i}"] # a12 - a14
        for c in "lmn":
            corners += [f"{c}{i}"] # l12 - n14

    for i in corners:
        del board[i]

    return board

def initial_board():
    '''initla_board() creates the board at the beginning of each game. The board is a dictionary of size 14x14. Each
    piece of each player is placed on its starting position. Remember the player and piece encodings.'''
    cols = [chr(i) for i in range(97, 111)]  # get characters a - n
    rows = range(1, 15)[::-1] # 14-1
    # board is stored as a dictionary, each field is a key-value-pair where each value represents a list including
    # the figure and color codes or [0,0] if the field is empty.
    b = {}
    # construct empty board
    # start by making every value [0, 0]
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

def clean_moves(board, moves, active_players):
    '''This functions cleans the input moves. It splits each move into initial field and destination field and removes
    any "x", "-", "+", "#", the piece names "Q", "K", "N", "R", "B" and pawn promotions e.g. "=Q" and makes up for
    random movements of kings after timeouts, stalements or resignations. Also the castling moves are split up for
    further processing. It takes as input the current state of the board, the moves of one round and the list
    of still active players. The latter input is needed to perform castling moves in case any player has already
    dropped out. The output is a list of lists containing the cleaned moves for one round.'''
    b = board
    # replace "x" with "-" and split on "-"
    cleaned = [moves[i].replace("x", "-").split("-") for i in range(len(moves))]
    # output: [['Ne2', 'g1+'], ['b4', 'h14+#'], ['d13', 'd11=Q']...]
    # now delete +, #, =Q, T, R and S
    # go through cleaned, which is a list of lists
    # list comprehension covers several identical entries, for example two timeouts in one round
    if ["T"] in cleaned:
        player_nr = active_players[cleaned.index(["T"])] # get which player had timeout
        if [6, player_nr] in board.values():
            # if the king of this player is still on the board, come up for the random movement and change the move "T"
            # to [king position, king position] so it can be processed and the player can be counted as still
            # in play in case the king moves randomly the next rounds.
            king_position = [key for key,value in board.items() if value == [6, player_nr]] # store the player's king
            # position
            # now take the king and do not move it, as it might move randomly in the next rounds. Timeouts do not
            # necessarily mean that a player drops out immediately. His/her king might still move around randomly
            # although being dead.
            cleaned = [[king_position[0], king_position[0]] if move == ["T"] else move for move in cleaned]
        else:
            # if the king is not on the board anymore, there is no random movement the next rounds meaning the
            # player won't be active in the upcoming rounds.
            cleaned = [move for move in cleaned if move != ["T"]]
    if ["R"] in cleaned:
        # this is done for the resignations as well
        player_nr = active_players[cleaned.index(["R"])] # get which player had timeout
        if [6, player_nr] in board.values():
            king_position = [key for key,value in board.items() if value == [6, player_nr]] #
            cleaned = [[king_position[0], king_position[0]] if move == ["R"] else move for move in cleaned]
        else:
            cleaned = [move for move in cleaned if move != ["R"]]
    if ["S"] in cleaned:
        # and for stalements as well
        player_nr = active_players[cleaned.index(["S"])]
        if [6, player_nr] in board.values():
            king_position = [key for key,value in board.items() if value == [6, player_nr]]
            cleaned = [[king_position[0], king_position[0]] if move == ["S"] else move for move in cleaned]
        else:
            cleaned = [move for move in cleaned if move != ["S"]]
    # after about 12.000 moves the PGN4 notation changed slightly, introducing some new moves formats:
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
    for i in range(len(cleaned)):  # 0 to 4 if all players are still in game - go through moves list
        for j in range(len(cleaned[i])): # 0 to 1, or 0 to 2 in queenside castling move - go through each move
            cleaned[i][j] = cleaned[i][j].replace("+", "") # remove "+"
            cleaned[i][j] = cleaned[i][j].replace("#", "") # remove "#"
            # cover pawn promotions and use new encodings for promoted pawns
            # note that here the function changes the piece encoding directly on the current board.
            if "=R" in cleaned[i][j]: # pawn promotion to rook
                # [["a11", "a12=R"],...]
                b[cleaned[i][0]][0] = 7 # 7 = encoding for promoted pawn to rook
                cleaned[i][j] = cleaned[i][j].replace("=R", "")
            elif "=N" in cleaned[i][j]: # pawn promotion to knight
                b[cleaned[i][0]][0] = 8 # encoding for promoted pawn to knight
                cleaned[i][j] = cleaned[i][j].replace("=N", "")
            elif "=B" in cleaned[i][j]: # promotion to bishop
                b[cleaned[i][0]][0] = 9
                cleaned[i][j] = cleaned[i][j].replace("=B", "")
            elif "=Q" in cleaned[i][j]: # promotion to queen
                b[cleaned[i][0]][0] = 10
                cleaned[i][j] = cleaned[i][j].replace("=Q", "")
            elif "=D" in cleaned[i][j]: # in older games it states =D for queen promotion
                b[cleaned[i][0]][0] = 10
                cleaned[i][j] = cleaned[i][j].replace("=D", "")
            # in older games there are castling moves in the following formats: "O-OR", "O-OT"
            if "OT" in cleaned[i][j]:
                cleaned[i][j] = cleaned[i][j].replace("OT", "O")
            if "OR" in cleaned[i][j]:
                cleaned[i][j] = cleaned[i][j].replace("OR", "O")

            # in some older games, there exists a move in the format "i3-i2R". That R, sometimes also a T,
            # in the end does not seem to have any particular significance.
            if cleaned[i][j][-1].isupper() and cleaned[i][j][0] != "O": # check if there is an upper case letter
                # in the end of a move which is not a castling move and remove it.
                cleaned[i][j] = cleaned[i][j][:-1]

            # remove piece information, as it is not needed for our purposes
            if cleaned[i][j][0].isupper() and cleaned[i][j][0] != "O":
                # remove upper case letter at the beginning of each move except when it's a castling move
                cleaned[i][j] = cleaned[i][j][1:]
    return b, cleaned

def perform_castling(board, castling_move, player_nr):
    ''' This function performs queenside and kingside castling. It needs to know the player which is performing
     the castling move. For that it uses the index on currently active players. The input consists of the current
     state of the board, the castling move in cleaned format (["O", "O"] or ["O", "O", "O"] and the player number.'''
    if castling_move == ["O", "O", "O"]:  # queenside castling
        if player_nr == 1: # red player...
            # perform queenside castling
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
            # perform kingside castling
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

def mk_move(games):
    '''This function will track the moves and update the board state accordingly each round. It also updates
    active and dropped players each round. It takes the whole data_set as input and goes through each game and each
    round to add the necessary information for our LSTM model.'''
    for g in games: # go through each game
        try:
            board = initial_board()  # construct new board at the beginning of each game
            print(f"Going through all games... {round(games.index(g)/len(games)*100, 1)}%")  # print progress in percent
            # at the start of each game, all the players are active and none has dropped
            # reset the active and dropped players lists each game
            g["active_players"] = [1,2,3,4]
            g["dropped_players"] = []
            for r in g["Rounds"]: # go through each round
                # clean the moves and return the board after potential changes due to pawn promotions
                board, moves = clean_moves(board, r["Moves"], g["active_players"])
                # no move has been made until now, also no castling move
                currently_active_players = [] # reset the list of active players and update it each round
                for i in range(len(moves)): # go through each player's moves
                    if moves[i] == ["O", "O"]: # if kingside castling
                        player_nr = g["active_players"][i] # use index of move on active players list from last round
                        board = perform_castling(board, ["O", "O"], player_nr) # perform castling move
                        currently_active_players.append(player_nr) # add the player to the currently active players list
                    elif moves[i] == ["O", "O", "O"]: # queenside castling
                        # same procedure as above
                        player_nr = g["active_players"][i]
                        board = perform_castling(board, ["O", "O", "O"], player_nr)
                        currently_active_players.append(player_nr)
                    else: # if no castling move is being made
                        # if current move kicks out a king (6) and its not a random king movement due to T, S or R
                        if board[moves[i][1]][0] == 6 and moves[i][0] != moves[i][1]:
                            # i.e., if castling happens in the same round as some player has dropped out and there has not
                            # been a T, S or R we check if a player's king has been kicked out so we do not get a wrong
                            # index on the active players for the castling move.
                            player_nr = board[moves[i][1]][1] # store the player number of the player who has dropped by
                            # fallen king
                            if player_nr not in g["dropped_players"]: # add that player to the dropped players list
                                # if not already there
                                g["dropped_players"].append(player_nr)
                        # if there's no king being kicked out during this round, just perform the normal move
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
                # also into the times we insert a placeholder value of 0
                if len(g["dropped_players"]) > 0: # if we have at least one dropped player
                    for p in g["dropped_players"]:
                        r["Moves"].insert(p-1, "") # insert at index player number (1,2,3,4) - 1 (0,1,2,3)
                        r["Times"].insert(p-1, 0)
        except:
            continue
    return games

def polish_data(data):
    '''This function takes a json game data and keeps track of dropped and active players. Within the moves
    the function inserts an empty string in the place of a dropped player.'''
    data = add_dropped_active(data) # add lists to each game to keep track of active and dropped players
    return mk_move(data) # emulate piece movements, board states and keep track of active and dropped players