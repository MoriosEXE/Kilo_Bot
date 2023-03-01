import tkinter as tk
import fonction as fc

data = fc.data_read("test2")


a = tk.Tk()
canvas = tk.Canvas(a, width = 1000, height = 1000)
canvas.pack()

i = 0
for step in data :
    for bot in step :
        print(bot[1]  )
        try :

            canvas.create_oval((bot[1]*100), (bot[2]*100), (bot[2]*100), (bot[1]*100), tags= f"{i}")
            print("ok")
        except :
            print("fail")
    i += 1

a.mainloop()