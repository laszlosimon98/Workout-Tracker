import customtkinter

from src.config.settings import PADY


class MainGUI:
    def __init__(self, root, main):
        self.root = root
        self.main = main
        self.elements = list()

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(master=self.root, corner_radius=0, highlightthickness=0,
                                                   borderwidth=0, border_width=0, width=10)

        self.frame.grid(row=0, column=0, sticky="nswe")

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=0)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(6, weight=1)

        self.add_elements(self.frame)

    def destroy_elements(self):
        for element in self.elements:
            element.destroy()
        self.elements.clear()

    def add_elements(self, *args):
        for element in args:
            self.elements.append(element)
