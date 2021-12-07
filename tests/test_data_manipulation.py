# this is the testing file, where all the functions of our Data Manipulation will be tested

from data_manipulation import *
import pytest
import random

@pytest.fixture
def data():
    game = [
            {
                "Blue": "Bill13Cooper",
                "BlueElo": "1878",
                "Date": "Thu Dec 27 2018 01:20:05 GMT+0000 (UTC)",
                "Duration": "1311",
                "GameNr": "673575",
                "Green": "dimonchi73",
                "GreenElo": "1854",
                "Red": "pitifloo",
                "RedElo": "1912",
                "Result": "pitifloo: 20 - Bill13Cooper: 47 - rook6431: 42 - dimonchi73: 0",
                "Rounds": [
                    {
                        "Moves": [
                            "j2-j3",
                            "b5-c5",
                            "h13-h11",
                            "m10-l10"
                        ],
                        "Number": 1,
                        "Times": [
                            0,
                            5,
                            6,
                            5
                        ]
                    },
                    {
                        "Moves": [
                            "Nj1-i3",
                            "b4-d4",
                            "h11-h10",
                            "Bn9-m10"
                        ],
                        "Number": 2,
                        "Times": [
                            20,
                            8,
                            2,
                            11
                        ]
                    },
                    {
                        "Moves": [
                            "d2-d3",
                            "Na10-c9",
                            "i13-i12",
                            "m8-k8"
                        ],
                        "Number": 3,
                        "Times": [
                            51,
                            11,
                            1,
                            13
                        ]
                    },
                    {
                        "Moves": [
                            "Ni3-k4",
                            "b10-c10",
                            "Qh14-h11",
                            "m4-l4"
                        ],
                        "Number": 4,
                        "Times": [
                            81,
                            18,
                            3,
                            10
                        ]
                    },
                    {
                        "Moves": [
                            "Nk4xm5+",
                            "Nc9-d11",
                            "Qh11-j11+#"
                        ],
                        "Number": 5,
                        "Times": [
                            117,
                            7,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "Nm5-k4",
                            "Nd11xe13+",
                            "Kg14-h14"
                        ],
                        "Number": 6,
                        "Times": [
                            132,
                            2,
                            7
                        ]
                    },
                    {
                        "Moves": [
                            "Bi1-j2",
                            "Ra11-a10",
                            "d13-d12"
                        ],
                        "Number": 7,
                        "Times": [
                            144,
                            12,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "O-O",
                            "Ne13-d11",
                            "g13-g12"
                        ],
                        "Number": 8,
                        "Times": [
                            164,
                            2,
                            28
                        ]
                    },
                    {
                        "Moves": [
                            "g2-g4",
                            "b8-c8+",
                            "Bf14-g13"
                        ],
                        "Number": 9,
                        "Times": [
                            201,
                            7,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "g4-g5",
                            "Ba9-b8",
                            "Qj11-i11"
                        ],
                        "Number": 10,
                        "Times": [
                            220,
                            1,
                            2
                        ]
                    },
                    {
                        "Moves": [
                            "g5-g6",
                            "Na5-c6",
                            "g12-g11"
                        ],
                        "Number": 11,
                        "Times": [
                            227,
                            5,
                            7
                        ]
                    },
                    {
                        "Moves": [
                            "g6-g7",
                            "Nd11-c9",
                            "Bi14-g12"
                        ],
                        "Number": 12,
                        "Times": [
                            242,
                            17,
                            6
                        ]
                    },
                    {
                        "Moves": [
                            "g7-g8=Q",
                            "Ba6-b5",
                            "f13-f12"
                        ],
                        "Number": 13,
                        "Times": [
                            268,
                            2,
                            5
                        ]
                    },
                    {
                        "Moves": [
                            "Bf1-h3",
                            "b11-d11",
                            "Nj14-h13"
                        ],
                        "Number": 14,
                        "Times": [
                            286,
                            2,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "Ne1-f3",
                            "b7-d7",
                            "Kh14-i13"
                        ],
                        "Number": 15,
                        "Times": [
                            296,
                            2,
                            7
                        ]
                    },
                    {
                        "Moves": [
                            "Nf3-h4",
                            "Qa7-b7",
                            "Bg13-h12"
                        ],
                        "Number": 16,
                        "Times": [
                            322,
                            14,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "f2-f3",
                            "O-O-O",
                            "Ne14-g13"
                        ],
                        "Number": 17,
                        "Times": [
                            358,
                            6,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "Rd1-e1",
                            "d7-e7",
                            "Rd14-e14"
                        ],
                        "Number": 18,
                        "Times": [
                            378,
                            9,
                            3
                        ]
                    },
                    {
                        "Moves": [
                            "Qg8-j5",
                            "e7-f7",
                            "Nh13-j12"
                        ],
                        "Number": 19,
                        "Times": [
                            411,
                            4,
                            19
                        ]
                    },
                    {
                        "Moves": [
                            "Nh4-i6",
                            "f7-g7",
                            "Rk14-h14"
                        ],
                        "Number": 20,
                        "Times": [
                            440,
                            3,
                            7
                        ]
                    },
                    {
                        "Moves": [
                            "Ni6xg7",
                            "Qb7xNg7",
                            "Ki13-j14"
                        ],
                        "Number": 21,
                        "Times": [
                            452,
                            4,
                            8
                        ]
                    },
                    {
                        "Moves": [
                            "Qg1xQg7",
                            "Ra7xQg7",
                            "Ng13-h11"
                        ],
                        "Number": 22,
                        "Times": [
                            468,
                            2,
                            9
                        ]
                    },
                    {
                        "Moves": [
                            "Qj5-i4",
                            "Ra10-a7",
                            "Qi11-j11"
                        ],
                        "Number": 23,
                        "Times": [
                            483,
                            7,
                            5
                        ]
                    },
                    {
                        "Moves": [
                            "Qi4-h4",
                            "Nc9-b7",
                            "Rh14-h13"
                        ],
                        "Number": 24,
                        "Times": [
                            522,
                            20,
                            24
                        ]
                    },
                    {
                        "Moves": [
                            "Qh4-i5",
                            "Nb7-d6",
                            "Rh13-f13"
                        ],
                        "Number": 25,
                        "Times": [
                            569,
                            5,
                            6
                        ]
                    },
                    {
                        "Moves": [
                            "Nk4-i3",
                            "Ka6-a5",
                            "Nh11-i9"
                        ],
                        "Number": 26,
                        "Times": [
                            591,
                            3,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "k2-k4",
                            "Rg7-f7",
                            "f12-f11"
                        ],
                        "Number": 27,
                        "Times": [
                            606,
                            15,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "Qi5-k3",
                            "b9-d9",
                            "f11-f10"
                        ],
                        "Number": 28,
                        "Times": [
                            630,
                            7,
                            2
                        ]
                    },
                    {
                        "Moves": [
                            "Bh3-i4",
                            "Rf7-c7",
                            "g11-g10"
                        ],
                        "Number": 29,
                        "Times": [
                            652,
                            5,
                            3
                        ]
                    },
                    {
                        "Moves": [
                            "Ni3-g4",
                            "c8-d8",
                            "g10-g9"
                        ],
                        "Number": 30,
                        "Times": [
                            672,
                            5,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "h2-h4",
                            "d8-e8",
                            "h10-h9"
                        ],
                        "Number": 31,
                        "Times": [
                            699,
                            3,
                            3
                        ]
                    },
                    {
                        "Moves": [
                            "h4-h5",
                            "Rc7-d7",
                            "h9-h8"
                        ],
                        "Number": 32,
                        "Times": [
                            708,
                            20,
                            3
                        ]
                    },
                    {
                        "Moves": [
                            "Qk3-i5",
                            "Nc6-d8",
                            "Nj12-h11"
                        ],
                        "Number": 33,
                        "Times": [
                            738,
                            15,
                            22
                        ]
                    },
                    {
                        "Moves": [
                            "Ng4-f6",
                            "Rd7-b7",
                            "g9-g8"
                        ],
                        "Number": 34,
                        "Times": [
                            783,
                            9,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "h5-h6",
                            "Nd8-f9",
                            "Qj11-h9"
                        ],
                        "Number": 35,
                        "Times": [
                            813,
                            3,
                            7
                        ]
                    },
                    {
                        "Moves": [
                            "Qi5-l5",
                            "Bb8-a9",
                            "Qh9xQl5"
                        ],
                        "Number": 36,
                        "Times": [
                            835,
                            30,
                            8
                        ]
                    },
                    {
                        "Moves": [
                            "k4xQl5",
                            "Nf9xh8",
                            "Rf13-f12"
                        ],
                        "Number": 37,
                        "Times": [
                            876,
                            3,
                            7
                        ]
                    },
                    {
                        "Moves": [
                            "l5-l6",
                            "Nh8-f9",
                            "Nh11-j12"
                        ],
                        "Number": 38,
                        "Times": [
                            900,
                            3,
                            31
                        ]
                    },
                    {
                        "Moves": [
                            "Bj2-i3",
                            "Nd6-f5",
                            "Bg12-j9"
                        ],
                        "Number": 39,
                        "Times": [
                            959,
                            8,
                            15
                        ]
                    },
                    {
                        "Moves": [
                            "l6xm7",
                            "Nf5-e3",
                            "Bh12xm7"
                        ],
                        "Number": 40,
                        "Times": [
                            1002,
                            2,
                            21
                        ]
                    },
                    {
                        "Moves": [
                            "Bi3-j2",
                            "Rb7xBm7",
                            "Re14-h14"
                        ],
                        "Number": 41,
                        "Times": [
                            1039,
                            4,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "Bj2-k3",
                            "Ba9-b8",
                            "Rf12-h12"
                        ],
                        "Number": 42,
                        "Times": [
                            1058,
                            11,
                            5
                        ]
                    },
                    {
                        "Moves": [
                            "Kj1-k2",
                            "Rm7-k7",
                            "Rh14-h13"
                        ],
                        "Number": 43,
                        "Times": [
                            1087,
                            3,
                            4
                        ]
                    },
                    {
                        "Moves": [
                            "T",
                            "Rk7xBk3",
                            "Rh12-h7"
                        ],
                        "Number": 44,
                        "Times": [
                            1129,
                            17,
                            6
                        ]
                    },
                    {
                        "Moves": [
                            "Nf9-g7",
                            "Ni9-g10"
                        ],
                        "Number": 45,
                        "Times": [
                            1158,
                            15
                        ]
                    },
                    {
                        "Moves": [
                            "Rk3xKk2",
                            "Ng10-f8"
                        ],
                        "Number": 46,
                        "Times": [
                            1183,
                            2
                        ]
                    },
                    {
                        "Moves": [
                            "Ne3-f5",
                            "Nj12-i10"
                        ],
                        "Number": 47,
                        "Times": [
                            1193,
                            10
                        ]
                    },
                    {
                        "Moves": [
                            "Bb8-c7",
                            "Rh13-h10"
                        ],
                        "Number": 48,
                        "Times": [
                            1207,
                            5
                        ]
                    },
                    {
                        "Moves": [
                            "Bc7-d6",
                            "Rh10-h8"
                        ],
                        "Number": 49,
                        "Times": [
                            1224,
                            18
                        ]
                    },
                    {
                        "Moves": [
                            "Bd6xNf8",
                            "Ni10-g9"
                        ],
                        "Number": 50,
                        "Times": [
                            1245,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "d4-e4",
                            "i12-i11"
                        ],
                        "Number": 51,
                        "Times": [
                            1253,
                            8
                        ]
                    },
                    {
                        "Moves": [
                            "e4-f4",
                            "i11-i10"
                        ],
                        "Number": 52,
                        "Times": [
                            1264,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "f4-g4",
                            "i10-i9"
                        ],
                        "Number": 53,
                        "Times": [
                            1266,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "g4-h4=Q",
                            "i9-i8"
                        ],
                        "Number": 54,
                        "Times": [
                            1268,
                            1
                        ]
                    },
                    {
                        "Moves": [
                            "Qh4-j6",
                            "i8-i7=Q"
                        ],
                        "Number": 55,
                        "Times": [
                            1284,
                            13
                        ]
                    },
                    {
                        "Moves": [
                            "Qj6xBj9",
                            "Ng9-i10"
                        ],
                        "Number": 56,
                        "Times": [
                            1301,
                            10
                        ]
                    },
                    {
                        "Moves": [
                            "R"
                        ],
                        "Number": 57,
                        "Times": [
                            1311
                        ]
                    }
                ],
                "RuleVariants": "PromoteTo=D",
                "Site": "www.chess.com/4-player-chess",
                "Termination": "Game over. (Yellow +20)",
                "TimeControl": "1+15D",
                "Variant": "FFA",
                "Yellow": "rook6431",
                "YellowElo": "2028"
            }] # construct sample game data
    return game

# test adding two additional lists for keeping track of added and dropped players to each game of the data
def test_add_dropped_active(data):
    game = data
    out = add_dropped_active(game)
    for g in out:
        assert g["dropped_players"] == []
        assert g["active_players"] == [1, 2, 3, 4]

def test_initial_board():
    b = initial_board() # construct board
    # now test if all the pieces of each player are on the board
    # remember the player encodings 1, 2, 3 and 4 for each color
    assert sum([b[1] for b in b.values()]) == 16*1 + 16*2 + 16*3 + 16*4 # 16 pieces for each player
    assert sum([b[0] for b in b.values()]) == 4*6 + 4*5 + 8*4 + 8*3 + 8*2 + 4*8 # each piece of every player together

def test_delete_corners():
    b = initial_board()
    l_b = len(b) # store the lengths of the board
    delete_corners(b) # delete corners
    assert (l_b - len(b)) == 3*3*4 # assert if all corners are deleted

def test_clean_moves(data):
    game = data
    b = initial_board() # construct initial board
    rounds = game[0]["Rounds"] # extract the rounds including all the moves
    for i in range(len(rounds)):
        moves = rounds[i]["Moves"]
        active_players = [1, 2, 3, 4] # does not matter for testing purposes
        b, cleaned = clean_moves(b, moves, active_players)
        assert len(cleaned) == len(moves)
        assert "x" not in str(cleaned)
        assert "-" not in str(cleaned)
        assert "S" not in str(cleaned)
        assert "R" not in str(cleaned)
        assert "T" not in str(cleaned)
        assert "=" not in str(cleaned)
        assert len(cleaned[0]) == 2

def test_perform_castling():
    b = initial_board() # construct initial board
    c_moves = ["O", "O"], ["O", "O", "O"]
    players = [1,2,3,4]
    for p in players:
        for m in c_moves:
            b1 = perform_castling(b, m, p)
            assert b == b1 # check that castling did not happen as it was not possible
            # now, remove all the pieces but king and rooks to perform both castling moves
            b2 = {k:v if v[0] in [2,6] else [0,0] for k,v in b.items()}
            #print(b2)
            b3 = perform_castling(b2, m, p)
            #print(b3)
            if p == 1:
                if m == c_moves[0]:
                    assert (b3["j1"], b3["i1"]) == (b2["h1"], b2["k1"])
                    assert (b3["h1"], b3["k1"]) == ([0, 0], [0, 0])
                elif m == c_moves[1]:
                    assert (b3["f1"], b3["g1"]) == (b2["h1"], b2["d1"])
                    assert (b3["d1"], b3["h1"]) == ([0, 0], [0, 0])
            elif p == 2:
                if m == c_moves[0]:
                    assert (b3["a10"], b3["a9"]) == (b2["a8"], b2["a11"])
                    assert (b3["a11"], b3["a8"]) == ([0, 0], [0, 0])
                elif m == c_moves[1]:
                    assert (b3["a6"], b3["a7"]) == (b2["a8"], b2["a4"])
                    assert (b3["a4"], b3["a8"]) == ([0, 0], [0, 0])
            elif p == 3:
                if m == c_moves[0]:
                    assert (b3["e14"], b3["f14"]) == (b2["g14"], b2["d14"])
                    assert (b3["d14"], b3["g14"]) == ([0, 0], [0, 0])
                elif m == c_moves[1]:
                    assert (b3["i14"], b3["h14"]) == (b2["g14"], b2["k14"])
                    assert (b3["g14"], b3["k14"]) == ([0, 0], [0, 0])
            elif p == 4:
                if m == c_moves[0]:
                    assert (b3["n5"], b3["n6"]) == (b2["n7"], b2["n4"])
                    assert (b3["n4"], b3["n7"]) == ([0, 0], [0, 0])
                elif m == c_moves[1]:
                    assert (b3["n9"], b3["n8"]) == (b2["n7"], b2["n11"])
                    assert (b3["n7"], b3["n11"]) == ([0, 0], [0, 0])

def test_mk_move(data):
    game = data
    game = add_dropped_active(game)
    assert game[0]["dropped_players"] == []
    assert game[0]["active_players"] == [1,2,3,4]
    mk_move(game)
    assert game[0]["dropped_players"] == [1,3,4]
    assert game[0]["active_players"] == [2]
    assert game[0]["Rounds"][-1]["Times"] == [0,1311,0,0]
    assert game[0]["Rounds"][-1]["Moves"] == ["", "R", "", ""]

def test_polish_data(data):
    game = data
    game = polish_data(game)
    assert game[0]["dropped_players"] == [1, 3, 4]
    assert game[0]["active_players"] == [2]
    assert game[0]["Rounds"][-1]["Times"] == [0,1311,0,0]
    assert game[0]["Rounds"][-1]["Moves"] == ["", "R", "", ""]