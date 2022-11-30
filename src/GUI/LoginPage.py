from src.GUI.MainGUI import MainGUI

import customtkinter


class LoginPage(MainGUI):
    def __init__(self, root, main):
        super().__init__(root, main)

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Login")
        self.label.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.remember_me_checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember Me")
        self.remember_me_checkbox.pack(pady=12, padx=10)

        self.login_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=12, padx=10)

        self.sign_up_button = customtkinter.CTkButton(master=self.frame, text="Sign Up",
                                                      command=self.from_login_page_to_sign_up_page)
        self.sign_up_button.pack(pady=12, padx=10)

        self.add_elements(self.frame, self.label, self.username_entry, self.password_entry, self.login_button,
                          self.remember_me_checkbox)

    def login(self):
        self.destroy_elements()

    def from_login_page_to_sign_up_page(self):
        self.destroy_elements()
        self.main.to_sign_up_page()
