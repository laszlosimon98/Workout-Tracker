import customtkinter


class MainGUI:
    def __init__(self, root, main):
        self.root = root
        self.main = main
        self.elements = list()

        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.left_frame = customtkinter.CTkFrame(master=self.root, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nswe", padx=(30, 0), pady=20)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, minsize=10)

        self.right_frame = customtkinter.CTkFrame(master=self.root, corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nswe", padx=(0, 30), pady=20)
        self.right_frame.rowconfigure(0, minsize=95)
        self.right_frame.rowconfigure(2, minsize=25)
        self.right_frame.rowconfigure(4, minsize=25)

        self.add_elements(self.left_frame, self.right_frame)

    def destroy_elements(self):
        for element in self.elements:
            element.destroy()
        self.elements.clear()

    def add_elements(self, *args):
        for element in args:
            self.elements.append(element)
