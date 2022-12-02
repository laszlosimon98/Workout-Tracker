from src.gui.MainGUI import MainGUI

import customtkinter


class LoginPage(MainGUI):
    def __init__(self, root, main):
        super().__init__(root, main)

        # self.temp = customtkinter.CTkLabel(master=self.left_frame, text="")
        # self.temp2 = customtkinter.CTkLabel(master=self.right_frame, text="")

        self.left_frame.destroy()
        self.right_frame.destroy()

        self.label = customtkinter.CTkLabel(master=self.middle_frame, text="Login")
        self.label.grid(row=1, column=0, pady=15, padx=10, sticky="ns")

        self.username_entry = customtkinter.CTkEntry(master=self.middle_frame, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, pady=(0, 15), padx=10, sticky="ns")

        self.password_entry = customtkinter.CTkEntry(master=self.middle_frame, placeholder_text="Password", show="*")
        self.password_entry.grid(row=3, column=0, pady=(0, 15), padx=10, sticky="ns")

        self.remember_me_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame, text="Remember Me")
        self.remember_me_checkbox.grid(row=4, column=0, pady=(0, 20), padx=10, sticky="ns")

        self.login_button = customtkinter.CTkButton(master=self.middle_frame, text="Login", command=self.login)
        self.login_button.grid(row=5, column=0, pady=(0, 10), padx=10, sticky="ns")

        self.sign_up_button = customtkinter.CTkButton(master=self.middle_frame, text="Sign Up",
                                                      command=self.from_login_page_to_sign_up_page)
        self.sign_up_button.grid(row=6, column=0, pady=(0, 10), padx=10, sticky="ns")

        # self.temp.grid(row=1, column=1, sticky="e")
        # self.temp2.grid(row=1, column=0, sticky="w")

        self.add_elements(self.label, self.username_entry, self.password_entry, self.login_button,
                          self.remember_me_checkbox)

    def login(self):
        self.destroy_elements()

    def from_login_page_to_sign_up_page(self):
        self.destroy_elements()
        self.main.to_sign_up_page()
