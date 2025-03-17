import tkinter as tk
from tkinter import messagebox
import base

class TargetModule(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

    targetFrame = tk.Frame(relief=tk.RAISED, borderwidth=1)
    targetFrame.grid(row=1 , column=0, padx=5, pady = 5)

    targetLinkSet = tk.Label(master=targetFrame, text="Target Link")
    targetLinkSet.grid(row=1, column=0, sticky="e")

    targetLinkEntry = tk.Entry(master = targetFrame, width=100)
    targetLinkEntry.grid(row=1, column=1, sticky="w")

    targetLinkLabel = tk.Label(master=targetFrame, text=base.targetURL)
    targetLinkLabel.grid(row=2, column=1)

    targetLinkBtn = tk.Button(master = targetFrame, text="Update")
    targetLinkBtn.grid(row=2, column=2, sticky="w")

    

    




