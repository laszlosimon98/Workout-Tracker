from src.GUI.MainGUI import MainGUI
from src.domain.Person import Person

import customtkinter


class SignUpPage(MainGUI):
    def __init__(self, root, main):
        super().__init__(root, main)

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Sign Up")
        self.label.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.password2_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password2_entry.pack(pady=12, padx=10)

        self.sign_up_button = customtkinter.CTkButton(master=self.frame, text="Sign Up", command=self.sign_up)
        self.sign_up_button.pack(pady=12, padx=10)

        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back",
                                                   command=self.from_sign_up_page_to_login_page)
        self.back_button.pack(pady=12, padx=10)

        self.add_elements(self.frame, self.label, self.username_entry, self.password_entry, self.password2_entry,
                          self.sign_up_button, self.back_button)

    def from_sign_up_page_to_login_page(self):
        self.destroy_elements()
        self.main.to_login_page()

    def sign_up(self):
        message = customtkinter.StringVar()
        print(message)

        username = self.username_entry.get()
        password = self.password_entry.get()
        password2 = self.password2_entry.get()

        wrong_label = customtkinter.CTkLabel(master=self.frame, text=message)
        wrong_label.pack(pady=12, padx=10)
        self.add_elements(wrong_label)

        '''
            TODO:
                A Hiba a label entry mellett jelenjen meg
                ??? szin
        '''

        # if len(username) == 0:
        #     message.set("A felhasználó név nem lehet üres!")
        # elif len(username) > 15:
        #     print("hosszu")
        # elif len(password) == 0:
        #     print("ures")
        # elif len(password) > 15:
        #     print("hosszu")
        # elif len(password2) == 0:
        #     print("ures")
        # elif len(password2) > 15:
        #     print("hosszu")
        # elif password != password2:
        #     print("nem egyezik meg")
        # else:
        #     person = Person(username, password)
        #     self.destroy_elements()
        #     self.main.to_login_page()
