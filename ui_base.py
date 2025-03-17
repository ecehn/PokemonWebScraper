import tkinter as tk
from tkinter import messagebox, scrolledtext
import json


with open("links.json", "r", encoding="utf-8") as file:
    data = json.load(file)

root=tk.Tk()
root.geometry("960x540")
root.title("Poke Scraper")

searching_box = scrolledtext.ScrolledText(width=70, height=15, wrap=tk.WORD, font=("Arial", 8))
searching_box.grid(row=0, column=0)



bestbuy_products = data["Best Buy"]["products"]
target_products = data["Target"]["products"]

for product in bestbuy_products:
    searching_box.insert("1.0", product['product_name'])
    searching_box.yview_moveto(0)


results_box = scrolledtext.ScrolledText(width=70, height=15, wrap=tk.WORD, font=("Arial", 12))
results_box.grid(row=1, column=0)

for product in bestbuy_products:
    results_box.insert("1.0", product)  # Adds new results at the top
    results_box.yview_moveto(0)

root.mainloop()