from src.gui.MainGUI import MainGUI
from src.config.settings import LABEL_ENTRY_WIDTH, PADX, PADY

import customtkinter


class LoginPage(MainGUI):
    def __init__(self, root, main):
        super().__init__(root, main)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Login")

        self.username_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username",
                                                     width=LABEL_ENTRY_WIDTH)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*",
                                                     width=LABEL_ENTRY_WIDTH)

        self.remember_me_checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember Me")

        self.login_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login,
                                                    width=LABEL_ENTRY_WIDTH)

        self.sign_up_button = customtkinter.CTkButton(master=self.frame, text="Sign Up",
                                                      command=self.from_login_page_to_sign_up_page,
                                                      width=LABEL_ENTRY_WIDTH)

        self.label.grid(row=1, column=1, pady=PADY, padx=PADX, sticky="n")
        self.username_entry.grid(row=2, column=1, pady=(0, PADY), padx=PADX, sticky="n")
        self.password_entry.grid(row=3, column=1, pady=(0, PADY), padx=PADX, sticky="n")
        self.remember_me_checkbox.grid(row=4, column=1, pady=(0, PADY), padx=PADX, sticky="n")
        self.login_button.grid(row=5, column=1, pady=(0, PADY), padx=PADX, sticky="n")
        self.sign_up_button.grid(row=6, column=1, pady=(0, PADY), padx=PADX, sticky="n")

        self.add_elements(self.label, self.username_entry, self.password_entry, self.login_button,
                          self.remember_me_checkbox, self.sign_up_button)

    def login(self):
        self.destroy_elements()

    def from_login_page_to_sign_up_page(self):
        self.destroy_elements()
        self.main.to_sign_up_page()
