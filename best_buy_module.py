import tkinter as tk
from tkinter import messagebox
import base

class BestBuyModule(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

    # def set_BB_url(bbLinkEntry, bbLinkLabel):
    #     if base.checkUrl(bbLinkEntry):
    #         bbLinkLabel.config(text=bbLinkEntry.get())
    #     else:
    #         print("Not a valid URL")
    # def set_BB_url(bbLinkLabel, bbLinkEntry):
    #     bbLinkLabel.config(text=bbLinkEntry.get())

    bestBuyFrame = tk.Frame(relief=tk.RAISED, borderwidth=1)
    bestBuyFrame.grid(row=0 , column=0, padx=5, pady = 5)

    bbLinkSet = tk.Label(master=bestBuyFrame, text="Best Buy Link")
    bbLinkSet.grid(row=0, column=0, sticky="e")

    bbLinkEntry = tk.Entry(master = bestBuyFrame, width=100)
    bbLinkEntry.grid(row=0, column=1, sticky="w")

    bbLinkLabel = tk.Label(master=bestBuyFrame, text=base.bbURL)
    bbLinkLabel.grid(row=1, column=1)

    bbLinkBtn = tk.Button(master = bestBuyFrame, text="Update")
    bbLinkBtn.grid(row=0, column=2, sticky="w")

    

    




