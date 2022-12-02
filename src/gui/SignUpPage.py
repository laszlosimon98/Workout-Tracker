import re

import customtkinter

from src.config.settings import LABEL_ENTRY_WIDTH, PADX, PADY
from src.domain.Person import Person
from src.gui.MainGUI import MainGUI
from src.database.Database import Database


class SignUpPage(MainGUI):
    def __init__(self, root, main):
        super().__init__(root, main)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Sign Up", width=LABEL_ENTRY_WIDTH)

        self.username_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username",
                                                     width=LABEL_ENTRY_WIDTH)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*",
                                                     width=LABEL_ENTRY_WIDTH)

        self.password2_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*",
                                                      width=LABEL_ENTRY_WIDTH)

        self.sign_up_button = customtkinter.CTkButton(master=self.frame, text="Sign Up", command=self.sign_up,
                                                      width=LABEL_ENTRY_WIDTH)

        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back",
                                                   command=self.from_sign_up_page_to_login_page,
                                                   width=LABEL_ENTRY_WIDTH)

        self.label.grid(row=1, column=1, pady=PADY, padx=PADX, sticky="nswe")
        self.username_entry.grid(row=2, column=1, pady=(0, PADY), padx=PADX, sticky="ns")
        self.password_entry.grid(row=3, column=1, pady=(0, PADY), padx=PADX, sticky="ns")
        self.password2_entry.grid(row=4, column=1, pady=(0, PADY), padx=PADX, sticky="ns")
        self.sign_up_button.grid(row=5, column=1, pady=(0, PADY), padx=PADX, sticky="ns")
        self.back_button.grid(row=6, column=1, pady=(0, PADY), padx=PADX, sticky="n")

        self.wrong_username_label = customtkinter.CTkLabel(master=self.frame, text_color="red", text='')
        self.wrong_password_label = customtkinter.CTkLabel(master=self.frame, text_color="red", text='')
        self.wrong_password2_label = customtkinter.CTkLabel(master=self.frame, text_color="red", text='')

        self.wrong_username_label.grid(row=2, column=2, sticky="nw")
        self.wrong_password_label.grid(row=3, column=2, sticky="nw")
        self.wrong_password2_label.grid(row=4, column=2, sticky="nw")

        self.password_hint_label0 = customtkinter.CTkLabel(master=self.frame, text="Jelszó:")
        self.password_hint_label1 = customtkinter.CTkLabel(master=self.frame, text_color="red",
                                                           text="Minimum 1 nagybetű!")
        self.password_hint_label2 = customtkinter.CTkLabel(master=self.frame, text_color="red",
                                                           text="Minimum 2 szám!")
        self.password_hint_label3 = customtkinter.CTkLabel(master=self.frame, text_color="red",
                                                           text="Minimum 8 karakter hosszú!")

        self.password_hint_label0.grid(row=1, column=0, sticky="ne")
        self.password_hint_label1.grid(row=2, column=0, sticky="ne")
        self.password_hint_label2.grid(row=3, column=0, sticky="ne")
        self.password_hint_label3.grid(row=4, column=0, sticky="ne")

        self.add_elements(self.label, self.username_entry, self.password_entry,
                          self.password2_entry, self.sign_up_button, self.back_button, self.wrong_password_label,
                          self.wrong_password2_label, self.wrong_username_label, self.password_hint_label0,
                          self.password_hint_label1, self.password_hint_label2, self.password_hint_label3)

        self.db = Database()

    def from_sign_up_page_to_login_page(self):
        self.destroy_elements()
        self.main.to_login_page()

    @staticmethod
    def one_capital(password):
        one_capital_letter = r"[A-Z]{1,}"
        return re.search(one_capital_letter, password)

    @staticmethod
    def two_number(password):
        two_number = r"^[^\d]*(\d+)[^\d]*(\d+)"
        return re.search(two_number, password)

    @staticmethod
    def length_8(password):
        length = r"^[\w]{8,}$"
        return re.match(length, password)

    def inputs_are_valid(self, username, password, password2=None):
        if len(username) == 0:
            self.wrong_username_label.configure(text="Kötelező!")
            self.username_entry.configure(border_color="red")
        elif len(username) > 15:
            self.wrong_username_label.configure(text="Hosszú, max 15!")
            self.username_entry.configure(border_color="red")
        else:
            self.wrong_username_label.configure(text="")
            self.username_entry.configure(border_color="green")

        if len(password) == 0:
            self.wrong_password_label.configure(text="Kötelező!")
        elif len(password) > 15:
            self.wrong_password_label.configure(text="Hosszú, max 15!")
        else:
            self.wrong_password_label.configure(text="")

        if len(password2) == 0:
            self.wrong_password2_label.configure(text="Kötelező!")
        elif len(password2) > 15:
            self.wrong_password2_label.configure(text="Hosszú, max 15!")
        else:
            self.wrong_password2_label.configure(text="")

        if password != password2:
            self.wrong_password_label.configure(text="A jelszavaknak meg\n kell egyeznie!")
            self.wrong_password2_label.configure(text="A jelszavaknak meg\n kell egyeznie!")

        if len(password) == 0 or len(password2) == 0 or len(password) > 15 or len(password2) > 15 or \
                str(password) != str(password2) or not self.one_capital(str(password)) or \
                not self.two_number(str(password)) or not self.length_8(str(password)):
            self.password_entry.configure(border_color="red")
            self.password2_entry.configure(border_color="red")
        else:
            self.password_entry.configure(border_color="green")
            self.password2_entry.configure(border_color="green")

        if self.one_capital(str(password)):
            self.password_hint_label1.configure(text_color="green")
        else:
            self.password_hint_label1.configure(text_color="red")
        if self.two_number(str(password)):
            self.password_hint_label2.configure(text_color="green")
        else:
            self.password_hint_label2.configure(text_color="red")

        if self.length_8(str(password)):
            self.password_hint_label3.configure(text_color="green")
        else:
            self.password_hint_label3.configure(text_color="red")

        return self.wrong_username_label.text == '' and self.wrong_password_label.text == '' and \
               self.wrong_password2_label.text == ''

    def sign_up(self):
        if self.inputs_are_valid(self.username_entry.get(), self.password_entry.get(), self.password2_entry.get()):
            username = str(self.username_entry.get())
            password = str(self.password_entry.get())
            person = Person(username, password)
            self.db.insert_user_into_table("Users", person)
            self.db.get_data_from_table("Users")
            self.destroy_elements()
            self.main.to_login_page()
