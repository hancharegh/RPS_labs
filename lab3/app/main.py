import tkinter as tk
from gui import App
from db import init_db

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
