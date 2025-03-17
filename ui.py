import tkinter as tk
from tkinter import messagebox, scrolledtext
import base

def ui_run_scraper():
    results_box.insert("1.0", stock_status)  # Adds new results at the top
    results_box.yview_moveto(0)

def update_best_buy():  
    stock_status = base.check_BB.bbUrl
    




window=tk.Tk()
window.geometry("960x540")
window.title("Poke Scraper")

bestBuyFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
bestBuyFrame.grid(row=0 , column=0, padx=5, pady = 5)

bbLinkLabel = tk.Label(master=bestBuyFrame, text="Best Buy Link")
bbLinkLabel.grid(row=0, column=0, sticky="e")

bbLinkEntry = tk.Entry(master = bestBuyFrame, width=100)
bbLinkEntry.grid(row=0, column=1, sticky="w")

bbLinkBtn = tk.Button(master = bestBuyFrame, text="submit", command=update_best_buy)
bbLinkBtn.grid(row=0, column=2, sticky="w")


results_box = scrolledtext.ScrolledText(width=70, height=15, wrap=tk.WORD, font=("Arial", 12))
results_box.grid(row=1, column=0)

window.mainloop()