from src.GUI.LoginPage import LoginPage
from src.GUI.SignUpPage import SignUpPage

import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class Main:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.root.title("Workout Diary")

        self.current_page = LoginPage(self.root, self)

    def to_sign_up_page(self):
        self.current_page = SignUpPage(self.root, self)

    def to_login_page(self):
        self.current_page = LoginPage(self.root, self)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    m = Main()
    m.run()

    # database = Database()
    # database.createTable("Test")
    # database.insert_into_table("Test")
    # database.get_data_from_table("Test")
