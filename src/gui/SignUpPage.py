import customtkinter

from src.gui.MainGUI import MainGUI


class SignUpPage(MainGUI):
    def __init__(self, root, main):
        super().__init__(root, main)

        self.label = customtkinter.CTkLabel(master=self.left_frame, text="Sign Up")
        self.label.grid(row=1, column=0, pady=15, padx=10, sticky="nse")

        self.username_entry = customtkinter.CTkEntry(master=self.left_frame, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, pady=(0, 15), padx=10, sticky="nse")

        self.password_entry = customtkinter.CTkEntry(master=self.left_frame, placeholder_text="Password", show="*")
        self.password_entry.grid(row=3, column=0, pady=(0, 15), padx=10, sticky="nse")

        self.password2_entry = customtkinter.CTkEntry(master=self.left_frame, placeholder_text="Password", show="*")
        self.password2_entry.grid(row=4, column=0, pady=(0, 25), padx=10, sticky="nse")

        self.sign_up_button = customtkinter.CTkButton(master=self.left_frame, text="Sign Up", command=self.sign_up)
        self.sign_up_button.grid(row=5, column=0, pady=(0, 20), padx=10, sticky="nse")

        self.back_button = customtkinter.CTkButton(master=self.left_frame, text="Back",
                                                   command=self.from_sign_up_page_to_login_page)
        self.back_button.grid(row=6, column=0, pady=(0, 10), padx=10, sticky="nse")

        self.wrong_username_label = customtkinter.CTkLabel(master=self.right_frame, text_color="red", width=70, text="")
        self.wrong_password_label = customtkinter.CTkLabel(master=self.right_frame, text_color="red", width=70, text="")
        self.wrong_password2_label = customtkinter.CTkLabel(master=self.right_frame, text_color="red", width=70,
                                                            text="")

        self.wrong_username_label.grid(row=1, column=0, sticky="w")
        self.wrong_password_label.grid(row=3, column=0, sticky="w")
        self.wrong_password2_label.grid(row=5, column=0, sticky="w")

        self.add_elements(self.label, self.username_entry, self.password_entry,
                          self.password2_entry, self.sign_up_button, self.back_button, self.wrong_password_label,
                          self.wrong_password2_label, self.wrong_username_label)

    def from_sign_up_page_to_login_page(self):
        self.destroy_elements()
        self.main.to_login_page()

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password2 = self.password2_entry.get()

        if len(username) == 0:
            self.wrong_username_label.configure(text="Kötelező!")
            self.username_entry.configure(border_color="red")
        elif len(username) > 15:
            self.wrong_username_label.configure(text="Hosszú, max 15!")
            self.username_entry.configure(border_color="red")
        else:
            self.wrong_username_label.configure(text="")
            self.username_entry.configure(border_color="gray32")

        if len(password) == 0:
            self.wrong_password_label.configure(text="Kötelező!")
            self.password_entry.configure(border_color="red")
        elif len(password) > 15:
            self.wrong_password_label.configure(text="Hosszú, max 15!")
            self.password_entry.configure(border_color="red")
        else:
            self.wrong_password_label.configure(text="")
            self.password_entry.configure(border_color="gray32")

        if len(password2) == 0:
            self.wrong_password2_label.configure(text="Kötelező!")
            self.password2_entry.configure(border_color="red")
        elif len(password2) > 15:
            self.wrong_password2_label.configure(text="Hosszú, max 15!")
            self.password2_entry.configure(border_color="red")
        else:
            self.wrong_password2_label.configure(text="")
            self.password2_entry.configure(border_color="gray32")

        if len(password) > 0 and password != password2:
            self.wrong_password_label.configure(text="A jelszavaknak meg\n kell egyeznie!")
            self.wrong_password2_label.configure(text="A jelszavaknak meg\n kell egyeznie!")
            self.password_entry.configure(border_color="red")
            self.password2_entry.configure(border_color="red")

        if self.wrong_username_label.text == "" and self.wrong_password_label.text == "" \
                and self.wrong_password2_label.text == "":
            pass
            # person = Person(username, password)
            # self.destroy_elements()
            # self.main.to_login_page()
