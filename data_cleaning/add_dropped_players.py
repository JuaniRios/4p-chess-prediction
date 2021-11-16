### this file will add information about the dropped players within a game to the json game data file ###

# we will use the existing function check_dropped and check_kings of the inital board state file
# go through file
# when game starts, make initial board statement (outer loop)
# store moves in list, change board state (mk_move)
# if red has dropped, insert at index 0, blue drops - insert index 1, yellow index 2, green index 4 (append)

# load necessary functions
from InitialBoardState import *
import json

# sample data:
games = {
    "data": [
        {
            "Blue": "NDimitrij",
            "BlueElo": "1911",
            "Date": "Thu Dec 27 2018 12:44:29 GMT+0000 (UTC)",
            "Duration": "1709",
            "GameNr": "675283",
            "Green": "your_master_is_here",
            "GreenElo": "1950",
            "Red": "Koloso598",
            "RedElo": "1886",
            "Result": "Koloso598: 24 - NDimitrij: 59 - LoyalOpposite: 25 - your_master_is_here: 78",
            "Rounds": [
                {
                    "Moves": [
                        "g2-g4",
                        "b7-d7",
                        "i13-i11",
                        "m4-k4"
                    ],
                    "Number": 1,
                    "Times": [
                        0,
                        3,
                        4,
                        2
                    ]
                },
                {
                    "Moves": [
                        "k2-k3",
                        "d7-e7",
                        "Qh14-i13",
                        "m11-k11"
                    ],
                    "Number": 2,
                    "Times": [
                        18,
                        4,
                        6,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Bf1-g2+",
                        "b6-c6",
                        "g13-g12",
                        "Nn5-l6"
                    ],
                    "Number": 3,
                    "Times": [
                        42,
                        2,
                        46,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Ne1-f3",
                        "e7-f7",
                        "Nj14-i12",
                        "m10-l10"
                    ],
                    "Number": 4,
                    "Times": [
                        112,
                        3,
                        6,
                        5
                    ]
                },
                {
                    "Moves": [
                        "g4-g5",
                        "f7-g7",
                        "h13-h12",
                        "m5-l5"
                    ],
                    "Number": 5,
                    "Times": [
                        127,
                        8,
                        1,
                        4
                    ]
                },
                {
                    "Moves": [
                        "g5-g6",
                        "Na10-c9",
                        "Bi14-h13",
                        "Bn6-m5"
                    ],
                    "Number": 6,
                    "Times": [
                        142,
                        3,
                        2,
                        3
                    ]
                },
                {
                    "Moves": [
                        "d2-d3",
                        "b8-c8",
                        "Ni12-h10",
                        "Kn7-n6"
                    ],
                    "Number": 7,
                    "Times": [
                        155,
                        3,
                        9,
                        2
                    ]
                },
                {
                    "Moves": [
                        "j2-j4",
                        "b11-c11",
                        "Bf14-g13",
                        "Bn9-m10"
                    ],
                    "Number": 8,
                    "Times": [
                        174,
                        1,
                        10,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Nj1-i3",
                        "Ba9-b8",
                        "e13-e12",
                        "Nn10-l11"
                    ],
                    "Number": 9,
                    "Times": [
                        193,
                        4,
                        3,
                        8
                    ]
                },
                {
                    "Moves": [
                        "Bi1-j2",
                        "b4-d4",
                        "f13-f11",
                        "Nl11-k9"
                    ],
                    "Number": 10,
                    "Times": [
                        210,
                        8,
                        2,
                        2
                    ]
                },
                {
                    "Moves": [
                        "e2-e4",
                        "Na5-b7",
                        "Rk14-j14",
                        "Rn11-n9"
                    ],
                    "Number": 11,
                    "Times": [
                        223,
                        5,
                        12,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Kh1-i1",
                        "Nb7-c5",
                        "Ne14-f12",
                        "Nk9-l11"
                    ],
                    "Number": 12,
                    "Times": [
                        261,
                        5,
                        14,
                        1
                    ]
                },
                {
                    "Moves": [
                        "Ki1-j1",
                        "Nc5-d7",
                        "Rj14-k14",
                        "m9-k9"
                    ],
                    "Number": 13,
                    "Times": [
                        293,
                        6,
                        4,
                        14
                    ]
                },
                {
                    "Moves": [
                        "h2-h4",
                        "Nd7-f8",
                        "Nf12-h11",
                        "k9-j9"
                    ],
                    "Number": 14,
                    "Times": [
                        320,
                        7,
                        15,
                        5
                    ]
                },
                {
                    "Moves": [
                        "h4-h5",
                        "O-O",
                        "Nh11-i9",
                        "Rn4-m4"
                    ],
                    "Number": 15,
                    "Times": [
                        352,
                        26,
                        7,
                        22
                    ]
                },
                {
                    "Moves": [
                        "Nf3-h4",
                        "Nf8-d9",
                        "Nh10-g8",
                        "Nl11-k9"
                    ],
                    "Number": 16,
                    "Times": [
                        414,
                        4,
                        18,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Nh4-i6",
                        "c6-d6",
                        "Rd14-e14",
                        "Bm10xNi6"
                    ],
                    "Number": 17,
                    "Times": [
                        443,
                        5,
                        11,
                        2
                    ]
                },
                {
                    "Moves": [
                        "h5xBi6",
                        "d6-e6",
                        "e12-e11",
                        "Nk9-i8"
                    ],
                    "Number": 18,
                    "Times": [
                        469,
                        2,
                        3,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Qg1-f1",
                        "Nc9-b11",
                        "Qi13-h14",
                        "Ni8-k7"
                    ],
                    "Number": 19,
                    "Times": [
                        496,
                        4,
                        13,
                        12
                    ]
                },
                {
                    "Moves": [
                        "Bg2-f3",
                        "Nd9-f8",
                        "d13-d11",
                        "Nk7-j5"
                    ],
                    "Number": 20,
                    "Times": [
                        535,
                        4,
                        5,
                        10
                    ]
                },
                {
                    "Moves": [
                        "Ni3xNj5",
                        "Nf8xg6",
                        "Re14-e12",
                        "Nl6xNj5"
                    ],
                    "Number": 21,
                    "Times": [
                        578,
                        3,
                        22,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Bf3-h5",
                        "Ng6-f4",
                        "Kg14-f13",
                        "Kn6-n5"
                    ],
                    "Number": 22,
                    "Times": [
                        616,
                        14,
                        3,
                        10
                    ]
                },
                {
                    "Moves": [
                        "Bh5-i4",
                        "b5-c5",
                        "g12-g11",
                        "m8-k8"
                    ],
                    "Number": 23,
                    "Times": [
                        653,
                        8,
                        10,
                        29
                    ]
                },
                {
                    "Moves": [
                        "Rk1-k2",
                        "Ba6-b5",
                        "Rk14-j14",
                        "k8-j8"
                    ],
                    "Number": 24,
                    "Times": [
                        711,
                        7,
                        3,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Kj1-k1",
                        "Bb5-f9",
                        "Ni9-h7",
                        "j8-i8"
                    ],
                    "Number": 25,
                    "Times": [
                        730,
                        4,
                        10,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Bi4xNj5",
                        "Bf9xNg8",
                        "j13-j11",
                        "k4xBj5"
                    ],
                    "Number": 26,
                    "Times": [
                        765,
                        2,
                        6,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Qf1xj5",
                        "Bg8-f7",
                        "Bh13-g12",
                        "i8xNh7"
                    ],
                    "Number": 27,
                    "Times": [
                        782,
                        20,
                        2,
                        5
                    ]
                },
                {
                    "Moves": [
                        "i6-i7",
                        "Nb11-c9",
                        "Qh14-d14",
                        "Rn9-k9"
                    ],
                    "Number": 28,
                    "Times": [
                        820,
                        5,
                        11,
                        3
                    ]
                },
                {
                    "Moves": [
                        "i2-i4",
                        "Nc9-b11",
                        "Qd14-d13",
                        "m7-l7"
                    ],
                    "Number": 29,
                    "Times": [
                        850,
                        4,
                        5,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Rd1-g1",
                        "Nf4-h3",
                        "Rj14-e14",
                        "j9-i9"
                    ],
                    "Number": 30,
                    "Times": [
                        874,
                        4,
                        12,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Rg1xg7",
                        "Nh3xBj2",
                        "i11-i10",
                        "Bm5xk3"
                    ],
                    "Number": 31,
                    "Times": [
                        896,
                        5,
                        1,
                        18
                    ]
                },
                {
                    "Moves": [
                        "Rg7xh7",
                        "Nj2xi4",
                        "Bg12-i14",
                        "Bk3-m5"
                    ],
                    "Number": 32,
                    "Times": [
                        953,
                        3,
                        3,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Rk2xRk9",
                        "Bb8-c9+",
                        "d11-d10",
                        "Rm4xj4"
                    ],
                    "Number": 33,
                    "Times": [
                        972,
                        6,
                        9,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Kk1-k2",
                        "Bc9-b8",
                        "Kf13-g12",
                        "Rj4xQj5"
                    ],
                    "Number": 34,
                    "Times": [
                        1012,
                        25,
                        2,
                        2
                    ]
                },
                {
                    "Moves": [
                        "i7-i8=Q",
                        "Ni4-g5+",
                        "k13-k12",
                        "Qn8xQi8"
                    ],
                    "Number": 35,
                    "Times": [
                        1049,
                        17,
                        11,
                        8
                    ]
                },
                {
                    "Moves": [
                        "Rh7xBf7",
                        "Ng5xRf7",
                        "Qd13-d11",
                        "l10xRk9"
                    ],
                    "Number": 36,
                    "Times": [
                        1087,
                        18,
                        6,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Kk2-k1",
                        "Qa7-e7+",
                        "Qd11xRj5",
                        "Qi8-k8+#"
                    ],
                    "Number": 37,
                    "Times": [
                        1126,
                        5,
                        3,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Ra4-a5",
                        "Qj5-d11",
                        "i9-h9"
                    ],
                    "Number": 38,
                    "Times": [
                        1157,
                        13,
                        9
                    ]
                },
                {
                    "Moves": [
                        "e6-f6",
                        "f11-f10",
                        "k9-j9"
                    ],
                    "Number": 39,
                    "Times": [
                        1182,
                        5,
                        10
                    ]
                },
                {
                    "Moves": [
                        "f6-g6",
                        "Kg12-f13",
                        "j9xi10"
                    ],
                    "Number": 40,
                    "Times": [
                        1199,
                        17,
                        3
                    ]
                },
                {
                    "Moves": [
                        "g6-h6=Q",
                        "Bi14-g12",
                        "Qk8-n8"
                    ],
                    "Number": 41,
                    "Times": [
                        1221,
                        2,
                        16
                    ]
                },
                {
                    "Moves": [
                        "c5-d5",
                        "j11xi10",
                        "h9-g9=Q"
                    ],
                    "Number": 42,
                    "Times": [
                        1245,
                        6,
                        2
                    ]
                },
                {
                    "Moves": [
                        "d5-e5",
                        "Re14-i14",
                        "Qg9-l4"
                    ],
                    "Number": 43,
                    "Times": [
                        1262,
                        10,
                        27
                    ]
                },
                {
                    "Moves": [
                        "e5-f5",
                        "i10-i9",
                        "Ql4-n4"
                    ],
                    "Number": 44,
                    "Times": [
                        1306,
                        6,
                        10
                    ]
                },
                {
                    "Moves": [
                        "Nf7-e5",
                        "Qd11-e10",
                        "Qn8-n7"
                    ],
                    "Number": 45,
                    "Times": [
                        1325,
                        2,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Qe7xQe10",
                        "Bg12xQe10",
                        "l7-k7"
                    ],
                    "Number": 46,
                    "Times": [
                        1337,
                        2,
                        6
                    ]
                },
                {
                    "Moves": [
                        "f5-g5",
                        "i9-i8",
                        "Qn4-m4"
                    ],
                    "Number": 47,
                    "Times": [
                        1348,
                        4,
                        14
                    ]
                },
                {
                    "Moves": [
                        "Ra5-a7",
                        "Be10-g12",
                        "Qm4xe4"
                    ],
                    "Number": 48,
                    "Times": [
                        1368,
                        2,
                        8
                    ]
                },
                {
                    "Moves": [
                        "g5-h5=Q",
                        "h12-h11",
                        "Qe4xd4"
                    ],
                    "Number": 49,
                    "Times": [
                        1383,
                        3,
                        5
                    ]
                },
                {
                    "Moves": [
                        "c11xd10",
                        "e11-e10",
                        "Qd4-m4"
                    ],
                    "Number": 50,
                    "Times": [
                        1415,
                        8,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Qh5-g6",
                        "g11-g10",
                        "Bm5-n4"
                    ],
                    "Number": 51,
                    "Times": [
                        1435,
                        8,
                        1
                    ]
                },
                {
                    "Moves": [
                        "Nb11-c9",
                        "Re12-d12",
                        "Qm4-m5"
                    ],
                    "Number": 52,
                    "Times": [
                        1453,
                        6,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Nc9-e8",
                        "Bg13-h12",
                        "Qn7-l7"
                    ],
                    "Number": 53,
                    "Times": [
                        1463,
                        18,
                        14
                    ]
                },
                {
                    "Moves": [
                        "Qg6-f6",
                        "f10-f9",
                        "Ql7-n7"
                    ],
                    "Number": 54,
                    "Times": [
                        1499,
                        6,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Ne8-c9",
                        "Bh12-g11",
                        "Qn7-n8"
                    ],
                    "Number": 55,
                    "Times": [
                        1520,
                        4,
                        14
                    ]
                },
                {
                    "Moves": [
                        "Nc9xe10",
                        "Bg12xNe10",
                        "Qn8-n7"
                    ],
                    "Number": 56,
                    "Times": [
                        1540,
                        4,
                        11
                    ]
                },
                {
                    "Moves": [
                        "Qh6xh11+",
                        "Kf13-f12",
                        "Qn7-n8"
                    ],
                    "Number": 57,
                    "Times": [
                        1559,
                        1,
                        13
                    ]
                },
                {
                    "Moves": [
                        "Qh11-h6",
                        "i8-i7=Q",
                        "k11-j11"
                    ],
                    "Number": 58,
                    "Times": [
                        1576,
                        8,
                        11
                    ]
                },
                {
                    "Moves": [
                        "Ra7xQi7",
                        "Ri14xRi7",
                        "j11-i11"
                    ],
                    "Number": 59,
                    "Times": [
                        1599,
                        2,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Qh6xRi7",
                        "Kf12-e13",
                        "i11-h11"
                    ],
                    "Number": 60,
                    "Times": [
                        1609,
                        22,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Qi7-g9",
                        "Rd12xd10",
                        "Qn8-n10"
                    ],
                    "Number": 61,
                    "Times": [
                        1652,
                        2,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Bb8xRd10",
                        "Bg11xk7",
                        "Qm5xBk7+"
                    ],
                    "Number": 62,
                    "Times": [
                        1678,
                        2,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Qg9-e11+",
                        "R",
                        "Qk7xKe13"
                    ],
                    "Number": 63,
                    "Times": [
                        1701,
                        1,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Qe11xQe13"
                    ],
                    "Number": 64,
                    "Times": [
                        1709
                    ]
                }
            ],
            "RuleVariants": "PromoteTo=D",
            "Site": "www.chess.com/4-player-chess",
            "Termination": "Game over. (Blue +20)",
            "TimeControl": "1+15D",
            "Variant": "FFA",
            "Yellow": "LoyalOpposite",
            "YellowElo": "1886"
        },
        {
            "Blue": "kyamites",
            "BlueElo": "1892",
            "Date": "Thu Dec 27 2018 13:30:33 GMT+0000 (UTC)",
            "Duration": "2041",
            "GameNr": "675395",
            "Green": "NDimitrij",
            "GreenElo": "1904",
            "Red": "luna4422",
            "RedElo": "1955",
            "Result": "luna4422: 23 - kyamites: 52 - LoyalOpposite: 14 - NDimitrij: 64",
            "Rounds": [
                {
                    "Moves": [
                        "g2-g4",
                        "b8-c8",
                        "i13-i11",
                        "m7-l7"
                    ],
                    "Number": 1,
                    "Times": [
                        0,
                        8,
                        8,
                        3
                    ]
                },
                {
                    "Moves": [
                        "g4-g5",
                        "b4-d4",
                        "Qh14-i13",
                        "m8-k8"
                    ],
                    "Number": 2,
                    "Times": [
                        30,
                        8,
                        2,
                        3
                    ]
                },
                {
                    "Moves": [
                        "g5-g6",
                        "Ba9-c7",
                        "Qi13-j12",
                        "k8-j8"
                    ],
                    "Number": 3,
                    "Times": [
                        54,
                        7,
                        29,
                        5
                    ]
                },
                {
                    "Moves": [
                        "g6-g7",
                        "b11-d11",
                        "k13-k11",
                        "j8-i8"
                    ],
                    "Number": 4,
                    "Times": [
                        100,
                        18,
                        3,
                        3
                    ]
                },
                {
                    "Moves": [
                        "g7-g8=Q",
                        "Na5-c6",
                        "g13-g12",
                        "Nn5-l6"
                    ],
                    "Number": 5,
                    "Times": [
                        127,
                        4,
                        4,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Nj1-i3",
                        "b9-c9",
                        "Nj14-i12",
                        "m9-l9"
                    ],
                    "Number": 6,
                    "Times": [
                        156,
                        9,
                        3,
                        9
                    ]
                },
                {
                    "Moves": [
                        "j2-j3",
                        "Qa7-b8",
                        "h13-h12",
                        "m4-l4"
                    ],
                    "Number": 7,
                    "Times": [
                        184,
                        1,
                        3,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Qg8-g2",
                        "Qb8-b9",
                        "Qj12-i13",
                        "i8-h8"
                    ],
                    "Number": 8,
                    "Times": [
                        197,
                        2,
                        18,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Bi1-j2",
                        "Na10-b8",
                        "Bi14-h13",
                        "m10-k10"
                    ],
                    "Number": 9,
                    "Times": [
                        222,
                        1,
                        6,
                        6
                    ]
                },
                {
                    "Moves": [
                        "e2-e4",
                        "b10-d10",
                        "Ne14-g13",
                        "Bn6-m7"
                    ],
                    "Number": 10,
                    "Times": [
                        239,
                        5,
                        2,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Bf1-e2",
                        "Nc6-e5",
                        "Ni12-h10",
                        "Bn9-m10"
                    ],
                    "Number": 11,
                    "Times": [
                        253,
                        2,
                        2,
                        7
                    ]
                },
                {
                    "Moves": [
                        "f2-f4",
                        "Ne5-c6",
                        "Ng13-i12",
                        "Nn10-m8"
                    ],
                    "Number": 12,
                    "Times": [
                        268,
                        4,
                        2,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Ni3-h5",
                        "d11-e11",
                        "Bh13-i14",
                        "l9-k9"
                    ],
                    "Number": 13,
                    "Times": [
                        296,
                        9,
                        16,
                        3
                    ]
                },
                {
                    "Moves": [
                        "k2-k4",
                        "Nb8-d7",
                        "d13-d12",
                        "m11-l11"
                    ],
                    "Number": 14,
                    "Times": [
                        334,
                        6,
                        2,
                        10
                    ]
                },
                {
                    "Moves": [
                        "O-O",
                        "Nd7-c5",
                        "Kg14-h14",
                        "Nm8-k7"
                    ],
                    "Number": 15,
                    "Times": [
                        355,
                        2,
                        12,
                        3
                    ]
                },
                {
                    "Moves": [
                        "d2-d3",
                        "Nc5-d7",
                        "f13-f11",
                        "k9-j9"
                    ],
                    "Number": 16,
                    "Times": [
                        377,
                        4,
                        2,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Ne1-f3",
                        "Ka8-a7",
                        "Qi13-g13",
                        "Bm10xNh5"
                    ],
                    "Number": 17,
                    "Times": [
                        392,
                        4,
                        17,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Rd1-d2",
                        "b5-c5",
                        "Bi14-h13",
                        "j9-i9"
                    ],
                    "Number": 18,
                    "Times": [
                        427,
                        4,
                        2,
                        5
                    ]
                },
                {
                    "Moves": [
                        "f4-f5",
                        "Qb9-a9",
                        "Bh13-g14",
                        "i9-h9"
                    ],
                    "Number": 19,
                    "Times": [
                        444,
                        3,
                        2,
                        25
                    ]
                },
                {
                    "Moves": [
                        "Ri1-h1",
                        "Ba6-b5",
                        "d12xe11",
                        "Rn11-n9"
                    ],
                    "Number": 20,
                    "Times": [
                        477,
                        3,
                        3,
                        22
                    ]
                },
                {
                    "Moves": [
                        "h2-h4",
                        "Ra11xe11",
                        "Kh14-i14",
                        "h9-g9=Q"
                    ],
                    "Number": 21,
                    "Times": [
                        525,
                        2,
                        15,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Qg1-f1",
                        "Qa9-a11",
                        "Bg14-h13",
                        "h8-g8=Q"
                    ],
                    "Number": 22,
                    "Times": [
                        558,
                        3,
                        3,
                        22
                    ]
                },
                {
                    "Moves": [
                        "Qg2-f2",
                        "Ka7-a6",
                        "g12-g11",
                        "Qg8-j8"
                    ],
                    "Number": 23,
                    "Times": [
                        603,
                        3,
                        20,
                        8
                    ]
                },
                {
                    "Moves": [
                        "Nf3-g5",
                        "Ka6-a5",
                        "Rk14-k13",
                        "Bh5xBe2"
                    ],
                    "Number": 24,
                    "Times": [
                        645,
                        3,
                        13,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Qf2xBe2",
                        "Bc7-b8",
                        "Ki14-j14",
                        "Qg9-j6"
                    ],
                    "Number": 25,
                    "Times": [
                        667,
                        8,
                        3,
                        19
                    ]
                },
                {
                    "Moves": [
                        "Ng5-i4",
                        "Ka5-b4",
                        "Bh13-i14",
                        "Qj6-j4"
                    ],
                    "Number": 26,
                    "Times": [
                        704,
                        4,
                        8,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Qe2-h2",
                        "Nd7-e5",
                        "Qg13-g14",
                        "Nl6-m4"
                    ],
                    "Number": 27,
                    "Times": [
                        749,
                        21,
                        4,
                        3
                    ]
                },
                {
                    "Moves": [
                        "Qh2-h3",
                        "Ra4-a7",
                        "Rd14-d13",
                        "Qj8xRd2"
                    ],
                    "Number": 28,
                    "Times": [
                        788,
                        11,
                        6,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Kj1-k1",
                        "Kb4-a5",
                        "Bf14-g13",
                        "Qd2-j8"
                    ],
                    "Number": 29,
                    "Times": [
                        814,
                        4,
                        3,
                        4
                    ]
                },
                {
                    "Moves": [
                        "f5-f6",
                        "Re11-c11",
                        "Bg13-f12",
                        "Nm4-k3"
                    ],
                    "Number": 30,
                    "Times": [
                        829,
                        5,
                        3,
                        14
                    ]
                },
                {
                    "Moves": [
                        "Ni4xNk3",
                        "Bb8-c7",
                        "Nh10-g12",
                        "l4xNk3"
                    ],
                    "Number": 31,
                    "Times": [
                        855,
                        6,
                        4,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Bj2-i1",
                        "Qa11-a10",
                        "Ni12-h10",
                        "Bm7-k5"
                    ],
                    "Number": 32,
                    "Times": [
                        874,
                        6,
                        2,
                        25
                    ]
                },
                {
                    "Moves": [
                        "h4-h5",
                        "Bc7-b8",
                        "Ng12-f14",
                        "Bk5-l4"
                    ],
                    "Number": 33,
                    "Times": [
                        917,
                        4,
                        3,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Kk1-k2",
                        "Rc11-a11",
                        "Qg14-g13",
                        "Bl4-k5"
                    ],
                    "Number": 34,
                    "Times": [
                        933,
                        4,
                        4,
                        23
                    ]
                },
                {
                    "Moves": [
                        "Bi1xk3",
                        "Qa10-a8",
                        "Bi14-h13",
                        "Qj4-j6"
                    ],
                    "Number": 35,
                    "Times": [
                        971,
                        4,
                        9,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Qf1-e2",
                        "Qa8-a10",
                        "Bh13-g14",
                        "Bk5-l4"
                    ],
                    "Number": 36,
                    "Times": [
                        1009,
                        2,
                        4,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Bk3xBl4",
                        "Nc6-d8",
                        "Bg14xk10+",
                        "l11xBk10"
                    ],
                    "Number": 37,
                    "Times": [
                        1025,
                        4,
                        19,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Bl4xm5",
                        "Nd8-f7",
                        "g11-g10",
                        "Rn4-n5"
                    ],
                    "Number": 38,
                    "Times": [
                        1062,
                        11,
                        6,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Bm5-j2",
                        "Nf7-e9",
                        "e13-e12",
                        "Qj8-j12"
                    ],
                    "Number": 39,
                    "Times": [
                        1094,
                        6,
                        8,
                        21
                    ]
                },
                {
                    "Moves": [
                        "Qh3-f5",
                        "Ne9-f7",
                        "Nh10-i12",
                        "Qj12-j9"
                    ],
                    "Number": 40,
                    "Times": [
                        1134,
                        7,
                        3,
                        8
                    ]
                },
                {
                    "Moves": [
                        "Qf5-h3",
                        "Qa10-a8",
                        "Ni12-j10",
                        "Nk7-l9"
                    ],
                    "Number": 41,
                    "Times": [
                        1155,
                        4,
                        3,
                        6
                    ]
                },
                {
                    "Moves": [
                        "h5-h6",
                        "Ra11-a10",
                        "j13-j12",
                        "Nl9xNj10"
                    ],
                    "Number": 42,
                    "Times": [
                        1173,
                        5,
                        2,
                        4
                    ]
                },
                {
                    "Moves": [
                        "h6-h7",
                        "d10-e10",
                        "i11xNj10",
                        "Qn8-m9"
                    ],
                    "Number": 43,
                    "Times": [
                        1188,
                        5,
                        10,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Qe2-f1",
                        "Bb8-c7",
                        "Rk13-i13",
                        "Qm9-k7"
                    ],
                    "Number": 44,
                    "Times": [
                        1223,
                        9,
                        14,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Rh1-j1",
                        "Ra7-a6",
                        "Bf12xQk7",
                        "Qj6xBk7"
                    ],
                    "Number": 45,
                    "Times": [
                        1259,
                        1,
                        2,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Bj2-h4",
                        "c9-d9",
                        "Qg13-h13",
                        "Qk7-k5"
                    ],
                    "Number": 46,
                    "Times": [
                        1273,
                        2,
                        40,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Bh4-i3",
                        "Bc7-d6",
                        "Kj14-j13",
                        "Qk5-k8"
                    ],
                    "Number": 47,
                    "Times": [
                        1325,
                        10,
                        10,
                        4
                    ]
                },
                {
                    "Moves": [
                        "Bi3-h2",
                        "Qa8-a7",
                        "Kj13-k13",
                        "Qj9-e14"
                    ],
                    "Number": 48,
                    "Times": [
                        1358,
                        3,
                        2,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Qh3-h4",
                        "e10xf11",
                        "Ri13-i14",
                        "Qe14-j9"
                    ],
                    "Number": 49,
                    "Times": [
                        1384,
                        4,
                        2,
                        15
                    ]
                },
                {
                    "Moves": [
                        "Bh2-i1",
                        "f11xg10",
                        "Rd13-d11",
                        "Qj9-l9"
                    ],
                    "Number": 50,
                    "Times": [
                        1418,
                        3,
                        10,
                        10
                    ]
                },
                {
                    "Moves": [
                        "Qh4-h3",
                        "g10-h10=Q",
                        "Ri14-j14",
                        "Qk8-e14"
                    ],
                    "Number": 51,
                    "Times": [
                        1449,
                        5,
                        7,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Qf1-h1",
                        "Qa7-a8",
                        "Rd11-i11",
                        "Qe14-k8"
                    ],
                    "Number": 52,
                    "Times": [
                        1472,
                        15,
                        3,
                        9
                    ]
                },
                {
                    "Moves": [
                        "Bi1-k3",
                        "Qa8-a7",
                        "Qh13-i13",
                        "Ql9-l11"
                    ],
                    "Number": 53,
                    "Times": [
                        1504,
                        5,
                        3,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Bk3-l4",
                        "Ka5-b4",
                        "Nf14-h13",
                        "Qk8-m10"
                    ],
                    "Number": 54,
                    "Times": [
                        1523,
                        10,
                        11,
                        3
                    ]
                },
                {
                    "Moves": [
                        "h7-h8=Q",
                        "Nf7xQh8",
                        "Qi13-i14",
                        "Ql11xQi14"
                    ],
                    "Number": 55,
                    "Times": [
                        1550,
                        2,
                        10,
                        6
                    ]
                },
                {
                    "Moves": [
                        "Bl4xNh8",
                        "Qh10xh12",
                        "R",
                        "Qi14-k12"
                    ],
                    "Number": 56,
                    "Times": [
                        1571,
                        17,
                        16,
                        10
                    ]
                },
                {
                    "Moves": [
                        "Bh8-g7",
                        "Qh12-i13",
                        "Qk12xKk13"
                    ],
                    "Number": 57,
                    "Times": [
                        1623,
                        7,
                        2
                    ]
                },
                {
                    "Moves": [
                        "Qh3-i3",
                        "Qi13xQk13",
                        "Rn9-j9"
                    ],
                    "Number": 58,
                    "Times": [
                        1640,
                        4,
                        9
                    ]
                },
                {
                    "Moves": [
                        "Qh1-g1",
                        "Qk13xNh13",
                        "Qm10-m8"
                    ],
                    "Number": 59,
                    "Times": [
                        1656,
                        12,
                        17
                    ]
                },
                {
                    "Moves": [
                        "Qi3-l6",
                        "Bb5-e8",
                        "Rj9-k9"
                    ],
                    "Number": 60,
                    "Times": [
                        1692,
                        16,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Kk2-j2",
                        "Qh13-h4+",
                        "Rk9xk4"
                    ],
                    "Number": 61,
                    "Times": [
                        1727,
                        7,
                        14
                    ]
                },
                {
                    "Moves": [
                        "Ql6-i3",
                        "Qh4-h7",
                        "Rk4-k6"
                    ],
                    "Number": 62,
                    "Times": [
                        1750,
                        17,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Rj1-k1",
                        "Qa7-h14",
                        "Rk6xRk1"
                    ],
                    "Number": 63,
                    "Times": [
                        1785,
                        10,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Kj2xRk1",
                        "Qh7-h1+",
                        "Qm8-k8+"
                    ],
                    "Number": 64,
                    "Times": [
                        1802,
                        4,
                        9
                    ]
                },
                {
                    "Moves": [
                        "Kk1-j2",
                        "Qh1-h9",
                        "Qk8-m8"
                    ],
                    "Number": 65,
                    "Times": [
                        1827,
                        11,
                        7
                    ]
                },
                {
                    "Moves": [
                        "Bg7xj10",
                        "Ra10xBj10",
                        "Rn5-n4"
                    ],
                    "Number": 66,
                    "Times": [
                        1857,
                        5,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Qi3-l6",
                        "Be8-c6",
                        "Rn4-n5"
                    ],
                    "Number": 67,
                    "Times": [
                        1876,
                        40,
                        5
                    ]
                },
                {
                    "Moves": [
                        "Ql6-i3",
                        "Qh9-k9",
                        "Rn5-l5"
                    ],
                    "Number": 68,
                    "Times": [
                        1924,
                        9,
                        13
                    ]
                },
                {
                    "Moves": [
                        "Kj2-j1",
                        "Rj10xk10",
                        "m6-l6"
                    ],
                    "Number": 69,
                    "Times": [
                        1950,
                        5,
                        11
                    ]
                },
                {
                    "Moves": [
                        "Qi3-j2",
                        "Rk10-n10+",
                        "R"
                    ],
                    "Number": 70,
                    "Times": [
                        1981,
                        11,
                        14
                    ]
                },
                {
                    "Moves": [
                        "f6-f7",
                        "Rn10xKn7"
                    ],
                    "Number": 71,
                    "Times": [
                        2028,
                        6
                    ]
                },
                {
                    "Moves": [
                        "R"
                    ],
                    "Number": 72,
                    "Times": [
                        2041
                    ]
                }
            ],
            "RuleVariants": "PromoteTo=D",
            "Site": "www.chess.com/4-player-chess",
            "Termination": "Game over. (Blue +20)",
            "TimeControl": "1+15D",
            "Variant": "FFA",
            "Yellow": "LoyalOpposite",
            "YellowElo": "1880"
        }
]
}
# games = jsonify...
moves1 = games["data"][0]["Rounds"][0]["Moves"] # input to function
#print(moves1)
times1 = games["data"][0]["Rounds"][0]["Times"]
#print(times1)
# index 0 is game index 0, outer loop goes through that
# second 0 is index of moves, go through Rounds in inner for loop (for range(len(Rounds)))

moves2 = games["data"][0]["Rounds"][1]["Moves"] # input to function
#print(moves2)
times2 = games["data"][0]["Rounds"][1]["Times"]
#print(times2)

b = initial_board()
#print(b)
#mk_move(moves1, b)
#mk_move(moves2, b)

def mk_move_training(game):
    # change board according to moves
    for g in game["data"]:
        board = initial_board()
        print(f"Game #{game['data'].index(g)}")
        for r in g["Rounds"]:
            print(r)
            dropped = []
            moves = r["Moves"] # [["Re1-e2"],...]
            if len(moves) == 1: # [["R"]]
                continue # continue with next round
            print("Raw Moves:")
            print(moves)
            moves_clean = clean_moves(moves) # clean moves, output: [["e2", "e4"],...]
            print()
            print("Clean moves:")
            print(moves_clean)
            times = r["Times"] # [20, 43, 10, 5]
            dropped = check_dropped(board, moves_clean)  # check dropped players
            for i in range(len(moves_clean)):
                if "castling" not in moves_clean[i] and moves_clean[i] != "dropped":
                    board[moves_clean[i][0]], board[moves_clean[i][1]] = [0, 0], board[moves_clean[i][0]]
            dropped += list(set(check_kings(board)) - set(dropped)) # check kings after moves were made again
            #print(dropped)
            if dropped != []:
                #print("Dropped players: ")
                for i in dropped:
                    #print(player_encoding[i])  # print player colors
                    moves.insert(i-1, "dropped")
                    times.insert(i-1, "dropped")
            print()
            print("Raw moves with dropped:")
            print(moves)
            print(dropped)
            print()
                #print(dropped)
                #print(moves)
                #print(times)
                #print(r)

mk_move_training(games)

# when castling, player apparently drops! Move is not changed to "kcastling"


#f = open("solo_pretty.json")
#data = json.load(f)
#mk_move_training(data)

#for g in data["data"]:
#    board = initial_board()
#    print(f"Game #{data['data'].index(g)}")
#    for r in g["Rounds"]:
#        moves = r["Moves"]
#        for m in moves:
#            if len(m) == 1:
#                print(m)