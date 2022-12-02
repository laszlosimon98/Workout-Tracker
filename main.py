from src.gui.LoginPage import LoginPage
from src.gui.SignUpPage import SignUpPage
from src.database.Database import Database

import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class Main:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.state("zoomed")
        self.root.title("Workout Diary")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.db = Database()
        self.db.create_table("Users")
        self.db.get_data_from_table("Users")

        self.current_page = LoginPage(self.root, self)

    def to_sign_up_page(self):
        self.current_page = SignUpPage(self.root, self)

    def to_login_page(self):
        self.current_page = LoginPage(self.root, self)

    def run(self):
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()


if __name__ == '__main__':
    m = Main()
    m.run()
