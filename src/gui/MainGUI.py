import customtkinter


class MainGUI:
    def __init__(self, root, main):
        self.root = root
        self.main = main
        self.elements = list()

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.left_frame = customtkinter.CTkFrame(master=self.root, corner_radius=0)
        self.middle_frame = customtkinter.CTkFrame(master=self.root, corner_radius=0)
        self.right_frame = customtkinter.CTkFrame(master=self.root, corner_radius=0)

        self.left_frame.grid(row=0, column=0, sticky="nswe")
        self.middle_frame.grid(row=0, column=1, sticky="nswe")
        self.right_frame.grid(row=0, column=2, sticky="nswe")

        self.left_frame.rowconfigure(0, minsize=100)

        self.middle_frame.columnconfigure(0, weight=1)
        self.middle_frame.rowconfigure(0, weight=1)
        self.middle_frame.rowconfigure(6, weight=1)

        self.right_frame.rowconfigure(0, weight=1)
        self.right_frame.rowconfigure(5, weight=1)
        # self.right_frame.rowconfigure(0, minsize=95)
        # self.right_frame.rowconfigure(2, minsize=25)
        # self.right_frame.rowconfigure(4, minsize=25)

        self.add_elements(self.left_frame, self.middle_frame, self.right_frame)

    def destroy_elements(self):
        for element in self.elements:
            element.destroy()
        self.elements.clear()

    def add_elements(self, *args):
        for element in args:
            self.elements.append(element)
