from tkinter import *
from time import strftime

def define_relogio():
    hora_atual = strftime("%H:%M:%S %p")
    relogio.config(text = hora_atual)
    relogio.after(1000, define_relogio)

window = Tk()
window.title("Relógio Digital em Python")

relogio = Label(
    window,
    font = ("Comic Sans", 25, "bold"),
    background = "Light blue",
    foreground = "black"
)

relogio.pack(anchor = "center")

define_relogio()

window.mainloop()