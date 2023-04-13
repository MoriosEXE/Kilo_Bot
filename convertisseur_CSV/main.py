from collections import OrderedDict

from pyexcel_ods3 import *

def data_read(name,type_data = True):
    data_by_time = [["step","ID","pos_X","pos_Y","Angle","Opinion","Puissance","etat"]]
    data_by_robot = []

    f = open(f"{name}.txt", "r")
    raw_line = f.read().split("step")

    for raw_data in raw_line:
        if raw_data != "":
            brut_line = raw_data.split("\n")

            step = brut_line[0]

            #step_dt = []
            for bot in brut_line:
                if "ID" in bot:
                    id_bot = bot.split("=")[1].split(" ")[1]
                    pos_x = float ((bot.split("=")[2].split(" ")[1]))
                    pos_y = float ((bot.split("=")[3].split(" ")[1]))
                    angle = float((bot.split("=")[4].split(" ")[1]))
                    opinion = int((bot.split("=")[5].split(" ")[1]))
                    puissance = int((bot.split("=")[6].split(" ")[1]))
                    etat = bot.split("=")[7]

                    data_by_time.append([step,id_bot, pos_x, pos_y, angle,opinion,puissance,etat])

    if type_data:
        return data_by_time
    else:
        return data_by_robot


nom = "test_nbRencontre_list_03"
data = data_read("test")

analyse = [["step", "opinion_1", "somme_1", "opinion_2", "somme_2","puissance_1","puissance_2","etat"]]

actual_step = 0
line = [0,0,0,0,0,0,0,0]
value = (0,0,0,0,0)
for i in data[1:]:
    if (actual_step != int(i[0])):

        value = (line[2],line[4],line[5],line[6],line[7])
        line = [actual_step,10,value[0],11,value[1],value[2]/value[0],value[3]/value[1],value[4]]

        actual_step = int(i[0])
        analyse.append(line)
        value = (0,0,0,0,0)
        line = [0,0,0,0,0,0,0,0]
    else:

        if(int(i[5]) % 2 == 0 ):
            value = (line[2]+1,line[4],int(i[6]) + line[5],line[6],line[7])
        line = [actual_step, 10, value[0], 11, value[1], value[2], value[3], value[4]]
        if(int(i[5]) %2 != 0):
            value = (line[2] , line[4]+1,line[5], line[6]+ int(i[6]),line[7])
        line = [actual_step, 10, value[0], 11, value[1], value[2], value[3],value[4]]

        if ("KO" in i[7]):
            value = (line[2],line[4],line[5],line[6],line[7] + 1)
        line = [actual_step, 10, value[0], 11, value[1], value[2], value[3], value[4]]




my_ods = OrderedDict() # from collections import OrderedDict
my_ods.update({"donnée_brut": data})
my_ods.update({"analyse": analyse})
save_data(f"D:/Kilo_Bot/statAetudier/{nom}.ods", my_ods)