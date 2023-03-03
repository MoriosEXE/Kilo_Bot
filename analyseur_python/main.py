import tkinter as tk
import fonction as fc
import math

data = fc.data_read("test_1")
length = 1000
width = 1000

zoom = 20


state = {
    "grid":False,
    "axe":False
}

fen = tk.Tk()

nb_step = tk.DoubleVar()
nb_step.set(len(data))

adjustable_zoom = tk.DoubleVar()
adjustable_zoom.set(zoom)

canvas = tk.Canvas(fen, width=length, height=width)
canvas.pack(side="left")



# Canvas
def axe_management():
    if state["axe"] :
        canvas.delete("axe")
        state["axe"] = False
    else:
        state["axe"] = True
        # x
        canvas.create_line(0, width / 2, length, width / 2, fill="black", width=2, tags="axe")
        # y
        canvas.create_line(length / 2, 0, length / 2, width, fill="black", width=2, tags="axe")

def grid_management():
    if state["grid"] :
        canvas.delete("grid")
        state["grid"] = False
    else :
        state["grid"] = True
        for i in range(0, width // 10):
            canvas.create_line(0, i * 10, length, i * 10, fill="black", width=1, tags="grid")
        for i in range(0, length // 10):
            canvas.create_line(i * 10, 0, i * 10, width, fill="black", width=1, tags="grid")


def kilobot_draw(posx,posy,next_x = 999,next_y = 999):

    up_left = (posx - 5,posy - 5)
    down_rigth = (posx + 5,posy + 5)


    canvas.create_oval(up_left[0],up_left[1],down_rigth[0],down_rigth[1], tags=f"bot")

    if next_y != 999 and next_x != 999:

        dx = next_x - posx
        dy = next_y - posy
        orientation = math.degrees(math.atan2(dy, dx))
        print(orientation)


def refresh_bot(self):

    canvas.delete(f"bot")

    for i in range(len(data)):

        step = data[i]
        if i != len(data) -1 :
            next_step = data[i+1]
        for j in range(len(step)):

            if i != len(data) -1 :

                next_bot = next_step[i]
                coor_next_bot = (
                (next_bot[1] * adjustable_zoom.get()) + width // 2, (next_bot[2] * adjustable_zoom.get()) + length // 2)
            else :
                coor_next_bot = (999,999)

            bot = step[j]
            coor_bot = ((bot[1]* adjustable_zoom.get()) + width // 2 ,(bot[2] * adjustable_zoom.get()) + length // 2)


            kilobot_draw(coor_bot[0],coor_bot[1],coor_next_bot[0],coor_next_bot[1])



"""            canvas.create_oval(((bot[1] * adjustable_zoom.get()) + width // 2),
                               (bot[2] * adjustable_zoom.get()) + length // 2,
                               (bot[1] * adjustable_zoom.get()) + width // 2,
                               (bot[2] * adjustable_zoom.get()) + length // 2, tags=f"bot")"""



# TOOLS
tools = tk.LabelFrame(fen, text="tools")
tools.pack(side="right")

# coorbutton
show_coor = tk.Checkbutton(tools, text="axe X & Y",command=axe_management)
show_coor.grid(row=0, column=0)

# show grid
show_grid = tk.Checkbutton(tools, text="grille",command=grid_management)
show_grid.grid(row=0, column=1)

# index step
index_step = tk.Scale(tools, variable=nb_step, to=len(data), label="step")
index_step.grid(row=1, column=0)

# ZOOM
zoom = tk.Scale(tools, variable=adjustable_zoom, label="ZOOM",command=refresh_bot)
zoom.grid(row=1, column=1)




fen.mainloop()
