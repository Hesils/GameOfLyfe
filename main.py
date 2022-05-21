import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        x_coord = int(self.winfo_screenwidth() / 2) - 600
        y_coord = int(self.winfo_screenheight() / 2 - 410)
        self.geometry("{}x{}+{}+{}".format(1200, 750, x_coord, y_coord))
        # Win elements
        self.canvastemperature = tk.Canvas(self, width=590, height=750, bg='white')
        self.canvastemperature.grid(row=0, column=0, padx=5)
        self.canvaschimie = tk.Canvas(self, width=590, height=750, bg='white')
        self.canvaschimie.grid(row=0, column=1)


if __name__ == '__main__':
    root = App()
    root.mainloop()
