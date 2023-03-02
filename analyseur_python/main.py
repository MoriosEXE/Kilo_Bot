import tkinter as tk
import fonction as fc

data = fc.data_read("test2")
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


def refresh_bot(self):
    print(adjustable_zoom.get())
    canvas.delete(f"bot")
    i = 0
    for step in data:
        for bot in step:

            canvas.create_oval(((bot[1] * adjustable_zoom.get()) + width // 2),
                               (bot[2] * adjustable_zoom.get()) + length // 2,
                               (bot[1] * adjustable_zoom.get()) + width // 2,
                               (bot[2] * adjustable_zoom.get()) + length // 2, tags=f"bot")

        i += 1


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
