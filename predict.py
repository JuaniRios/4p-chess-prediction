from lstm_model.final_model import interface_call
import pandas as pd
import numpy as np



players = ["Radon", "vrdtmr", "ccoppola"]
moves = [["h2-h3 Ne1-f3 Qg1-k5 Bi1-h2 Nj1-i3"], ["b7-c7 Qa7-b7 Na5-c6 Qb7-d9 b11-d11"],
         ["m9-l9 m8-l8 Qn8-m8 Nn5-l6 Qm8-l7"]]

prediction = interface_call(players, moves, 5)

print(prediction)