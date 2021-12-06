import pandas as pd
import numpy as np
import json


def to_hdf(data):
    moves_full = []
    for game in data["data"]:
        try:
            gamenr = game["GameNr"]
            moves_list = []

            red = [game["Red"], gamenr]
            blue = [game["Blue"], gamenr]
            yellow = [game["Yellow"], gamenr]
            green = [game["Green"], gamenr]

            for rnd in game["Rounds"]:
                moves_list.append(rnd["Moves"])

            for b in moves_list:
                red.append(b[0])
                blue.append(b[1])
                yellow.append(b[2])
                green.append(b[3])

            moves_full.append(red)
            moves_full.append(blue)
            moves_full.append(yellow)
            moves_full.append(green)
        except:
            print("Skipped a row due to error!")
            pass


    # data has to be the same length for each move so we choose every game less than "length" moves
    length = 110
    final = []
    for a in moves_full:
        if len(a) < length:
            final.append(a)

    # fill moves with zeroes until 120 moves are
    for a in final:
        if len(a) < length:
            a.extend((length-len(a))*"0")

    # write to dataframe, so we can later query the h5-file.
    df = pd.DataFrame(final)
    df = df.rename(columns={0:"player", 1:"gamenr"})
    df.columns = df.columns.astype(str)
    df = df.replace({"..":"0"})

    df.to_hdf("data_set.h5",key='df', mode='w', format='t', data_columns=True)
    print("Writing finished")

    return