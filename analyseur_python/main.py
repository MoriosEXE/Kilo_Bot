import tkinter as tk
import fonction as fc


print(fc.data_read("test2"))

a = tk.Tk()
canvas = tk.Canvas(a, width = 1000, height = 1000)
canvas.pack()

canvas.create_rectangle(0,0,100,100, tags="square")
a.mainloop()