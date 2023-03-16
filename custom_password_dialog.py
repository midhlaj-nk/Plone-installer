from typing import Union

import customtkinter as ctk
import tkinter as tk


class PasswordDialogBox(ctk.CTkToplevel):
    def __init__(self, parent, width=230, text="Please enter administartor your password"):
        ctk.CTkToplevel.__init__(self, parent)
        self.parent = parent
        self.text = text
        self.password = tk.StringVar()
        self.password_entry = ctk.CTkEntry(self, show='*',
                                           textvariable=self.password,
                                           width=width)
        self.confirm_button = ctk.CTkButton(self, text='Confirm',
                                            command=self.confirm_password)
        self.cancel_button = ctk.CTkButton(self, text='Cancel',
                                           command=self.cancel)
        self._user_input: Union[str, None] = None
        self.init_gui()

    def init_gui(self):
        self.title(' ')
        self.geometry('350x150')
        self.resizable(False, False)

        ctk.CTkLabel(self, text=self.text).grid(row=0,
                                                                   column=0,
                                                                   padx=10,
                                                                   pady=10)
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")
        self.confirm_button.grid(row=2, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")
        self.cancel_button.grid(row=2, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.grab_set()
        self.parent.wait_window(self)

    def confirm_password(self):
        self._user_input = self.password_entry.get()
        self.destroy()

    def cancel(self):
        self.password.set('')
        self.destroy()

    def get_input(self):
        return self._user_input

