from lstm_model.final_model import interface_call
import pandas as pd
import numpy as np



players = ["Radon", "vrdtmr", "ccoppola"]

moves = [["h2-h3 b7-c7 m9-l9"],
         ["Ne1-f3 Qa7-b7 m8-l8"],
         ["Qg1-k5 Na5-c6 Qn8-m8"],
         ["Bi1-h2 Qb7-d9 Nn5-l6"],
         ["Nj1-i3 b11-d11 Qm8-l7"]]

prediction = interface_call(players, moves, 5)

print(prediction)