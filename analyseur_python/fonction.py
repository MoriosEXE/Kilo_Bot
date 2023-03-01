def data_read(name,type_data = True):
    data_by_time = []
    data_by_robot = []

    f = open(f"{name}.txt", "r")
    raw_line = f.read().split("step")

    for raw_data in raw_line:
        if raw_data != "":
            brut_line = raw_data.split("\n")

            step = brut_line[0]
            step_dt = []
            for bot in brut_line:
                if "ID" in bot:
                    id_bot = bot.split("=")[1].split(" ")[1]
                    pos_x = bot.split("=")[2].split(" ")[1]
                    pos_y = bot.split("=")[3].split(" ")[1]
                    step_dt.append([id_bot, pos_x, pos_y])
            data_by_time.append(step_dt)
    if type_data:
        return data_by_time
    else:
        return data_by_robot
