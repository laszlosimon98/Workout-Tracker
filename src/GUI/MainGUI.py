class MainGUI:
    def __init__(self, root, main):
        self.root = root
        self.main = main
        self.elements = list()

    def destroy_elements(self):
        for element in self.elements:
            element.destroy()
        self.elements.clear()

    def add_elements(self, *args):
        for element in args:
            self.elements.append(element)
