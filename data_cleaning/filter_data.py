import datetime
import re
import traceback


def filter_data(file_str):
    try:
        with open(file_str) as f:
            content = f.read()
            games = content.splitlines()
            cleaned = []
            iteration = 0
            try:
                def get_param(name, pointer=0):
                    match = re.search(fr'\[{name} "([^"]*)', game[pointer:])
                    result = match.group(1)
                    pointer += match.regs[0][1] + 2
                    return result, pointer

                def get_time(pointer=0):
                    date = re.search(r"date=(\d\d\d\d-\d\d-\d\d)", game[pointer:])
                    time = re.search(r"T(\d\d:\d\d:\d\d)[^}]*}", game[pointer:])
                    result = datetime.datetime.strptime(date.group(1) + time.group(1), "%Y-%m-%d%H:%M:%S")
                    pointer += time.regs[0][1] - 1
                    return result, pointer

                def get_move(pointer):
                    match = re.search(r'([a-z0-9A-Z-+=#]+) ', game[pointer:])
                    result = match.group(1)
                    pointer += match.regs[0][1] - 1
                    return result, pointer

                def get_round(pointer, n, time):
                    match = re.search(rf"{n}\.", game[pointer:])
                    if not match:
                        return None, pointer, time

                    round = {"Moves": [], "Times": [], "Number": n}
                    pointer += match.regs[0][1] - 1

                    move, pointer = get_move(pointer)
                    round["Moves"] += [move]

                    # get time, and then put the delta from the previous time
                    time2, pointer = get_time(pointer)
                    round["Times"] += [int((time2 - time).total_seconds())]

                    # While there are more moves on this round
                    while True:
                        try:
                            next_move = re.search(r"\.\.", game[pointer:]).regs[0][0]
                            next_round = re.search(rf"{n + 1}\.", game[pointer:]).regs[0][0]
                        except AttributeError:
                            break

                        # if the next move is ahead of the next round pointer, break
                        if next_move > next_round:
                            break

                        move, pointer = get_move(pointer)
                        round["Moves"] += [move]

                        # get time string, and then put the delta from the previous time
                        time = time2
                        time2, pointer = get_time(pointer)
                        round["Times"] += [int((time2 - time).total_seconds())]

                    return round, pointer, time2

                for game in games:
                    iteration += 1
                    data = {}

                    result, _ = get_param("GameNr")
                    data["GameNr"] = result

                    result, _ = get_param("Variant")
                    data["Variant"] = result

                    result, _ = get_param("RuleVariants")
                    data["RuleVariants"] = result

                    result, _ = get_param("Result")
                    data["Result"] = result

                    result, _ = get_param("Termination")
                    data["Termination"] = result

                    result, _ = get_param("Red")
                    data["Red"] = result

                    result, _ = get_param("RedElo")
                    data["RedElo"] = result

                    result, _ = get_param("Blue")
                    data["Blue"] = result

                    result, _ = get_param("BlueElo")
                    data["BlueElo"] = result

                    result, _ = get_param("Yellow")
                    data["Yellow"] = result

                    result, _ = get_param("YellowElo")
                    data["YellowElo"] = result

                    result, _ = get_param("Green")
                    data["Green"] = result

                    result, _ = get_param("GreenElo")
                    data["GreenElo"] = result

                    result, _ = get_param("TimeControl")
                    data["TimeControl"] = result

                    result, _ = get_param("Site")
                    data["Site"] = result

                    result, _ = get_param("Date")
                    data["Date"] = result

                    data["Rounds"] = []

                    n = 1

                    start_time, _ = get_time()

                    end_time = re.search(r'\[Date "(... ... \d\d \d\d\d\d \d\d:\d\d:\d\d)', game).group(1)
                    end_time = datetime.datetime.strptime(end_time, "%a %b %d %Y %H:%M:%S")

                    data["Duration"] = str(int((end_time - start_time).total_seconds()))
                    pointer = 0
                    while True:
                        round, pointer, time = get_round(pointer, n, start_time)
                        if not round:
                            break
                        data["Rounds"] += [round]
                        n += 1

                    cleaned.append(data)

                return cleaned

            except Exception:
                print(traceback.format_exc())
                print(data["GameNr"])
                print(iteration)
    except Exception as Ex:
        print(Ex)

