import random
import tkinter as tk
import os
import sys


def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except Exception:
 
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


lijst1 = ["Slay", "Ice", "Shadow", "Nick", "Monkey", "Nigger", "Wise", "Fire"]
lijst2 = ["Dragon", "Wolf", "Knight", "Her", "Dance", "Kid", "Clock", "Barbie"]

keuze1 = random.choice(lijst1)
keuze2 = random.choice(lijst2)

root = tk.Tk()
root.iconbitmap(resource_path("Monkey.ico"))
root.geometry("500x300")
root.title("Name Gen")
root.configure(bg="pink")


img = tk.PhotoImage(file=resource_path("Monkey.png"))
root.configure(bg="pink")
label_img = tk.Label(root, image=img, bg="pink")
label_img.place(x=0, y=100)


Label = tk.Label(root, text="Click to generate",
                 font=("Arial, 16"), fg=("White"), bg="pink")
Label.pack()


credits = tk.Label(root, text="Tixie/oaya",
                   font=("Arial", 10), fg="white", bg="pink")
credits.place(relx=1, rely=1, anchor="se")


def Genereer():
    keuze1 = random.choice(lijst1)
    keuze2 = random.choice(lijst2)
    Label.config(text=f"Generated Name = {keuze1} {keuze2}", font=(
        "Arial", 15), fg="white", bg="pink")


knop = tk.Button(root, text="Generate name", font=(
    "Arial", 16), command=Genereer, fg="black", bg="pink")

knop.pack()
root.mainloop()
