import tkinter as tk

window=tk.Tk()
window.geometry("960x540")
window.title("Poke Scraper")

bestBuyFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
bestBuyFrame.grid(row=0 , column=0, padx=10, pady = 10)

bbLinkLabel = tk.Label(master=bestBuyFrame, text="Best Buy Link")
bbLinkLabel.pack()

bbLinkEntry = tk.Entry(master = bestBuyFrame)
bbLinkEntry.pack()

window.mainloop()