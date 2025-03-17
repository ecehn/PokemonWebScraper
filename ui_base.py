import tkinter as tk
from tkinter import messagebox, scrolledtext
from best_buy_module import BestBuyModule
from target_module import TargetModule

def ui_run_scraper():
    results_box.insert("1.0", stock_status)  # Adds new results at the top
    results_box.yview_moveto(0)


# def set_BB_url():
#     if checkUrl(bbLinkEntry):
#         bbLinkLabel.config(text=bbLinkEntry.get())

root=tk.Tk()
root.geometry("960x540")
root.title("Poke Scraper")

best_buy_module = BestBuyModule(root)
best_buy_module.grid(row=0 , column=0, padx=5, pady = 5)

target_module = TargetModule(root)
target_module.grid(row=1 , column=0, padx=5, pady = 5)


results_box = scrolledtext.ScrolledText(width=70, height=15, wrap=tk.WORD, font=("Arial", 12))
results_box.grid(row=2, column=0)

root.mainloop()