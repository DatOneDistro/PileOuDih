import random 
import tkinter as tk

def PileOuDih():

    callRd = random.choice(["Pile !", "Dih !"])
    labelRd.config(text=callRd)

windowApp = tk.Tk()
windowApp.title("Pile ou Dih !")

labelRd = tk.Label(windowApp, text="", font=("Helvetica", 48))
labelRd.pack(pady=20)

actionButton = tk.Button(windowApp, text="Affronte ton destin !", command=PileOuDih)
actionButton.pack(pady=20)

windowApp.mainloop()   
