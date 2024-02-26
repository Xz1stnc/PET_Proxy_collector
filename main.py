from List_sites_func import *
import tkinter as tk
from tkinter import messagebox


class ProxyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("900x600")

        self.title("Proxygainer")

        self.proxy_count = 0

        self.label = tk.Label(self, text=f"Proxy count: {self.proxy_count}")
        self.label.place(
            x=10.0,
            y=10.0
        )
        self.label.pack()


app = ProxyApp()
app.mainloop()
