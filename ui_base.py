import tkinter as tk
from tkinter import messagebox, scrolledtext
import json
import base
import schedule
import time


with open("links.json", "r", encoding="utf-8") as file:
    data = json.load(file)

root=tk.Tk()
root.geometry("960x540")
root.title("Poke Scraper")

searching_box = scrolledtext.ScrolledText(width=70, height=15, wrap=tk.WORD, font=("Arial", 10))
searching_box.grid(row=0, column=0)

stores_list = list(data.keys())

for store in stores_list:
    for product in data[store]["products"]:
        searching_box.insert("1.0", store + ": " + product['custom_name'] +'\n')
        searching_box.yview_moveto(0)

def check_links():
    for store in stores_list:
        for product in data[store]["products"]:
            results_box.insert("1.0", store + ": " + product['custom_name'] + "[" + base.run_check(product["product_link"], data[store]["referer"]) + "]" + '\n')
            results_box.yview_moveto(0)

results_box = scrolledtext.ScrolledText(width=70, height=15, wrap=tk.WORD, font=("Arial", 10))
results_box.grid(row=1, column=0)

run_script_btn = tk.Button(master=root, text="Run Script", command=check_links)
run_script_btn.grid(row=0, column=1, pady=10)


# def run_scraper():
#     schedule.every(5).seconds.do(check_links)

#     while True:
#         schedule.run_pending()
#         time.sleep


root.mainloop()

