try:
    import customtkinter as ctk
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk
    import subprocess
    import getpass
    import os
    import logging
    from tkinter import scrolledtext
    import sys
    from PIL import Image, ImageTk
except ImportError:
    print("One or more dependencies is missing. Installing...")
    subprocess.check_call(['pip', 'install', 'customtkinter'])

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

"""Window Structure"""
# mk_dir_input = False
root = ctk.CTk()
root.geometry("750x450")
root.title("Plone Installer")
root.resizable(False, False)

image_filename = "logo.png"
image = Image.open(image_filename)
# image = image.resize((400, 400))  # Resize the image
photo = ctk.CTkImage(image)  # Create a CTkImage object from the PIL Image

# Create a Label widget to display the image
image_label = ctk.CTkLabel(root, text=" ", image=photo)
image_label.place(x=700, y=17, anchor="ne")

# CybroLabel
label = ctk.CTkLabel(root,
                     text="Copyright © 2023 Cybrosys Technologies. All Rights Reserved.",
                     font=ctk.CTkFont(size=13))
label.place(x=20, y=425, anchor="sw")

# Welcome message label
welcome_label = ctk.CTkLabel(root, text="Plone Installer",
                             font=ctk.CTkFont(size=24))
welcome_label.place(x=20, y=40, anchor="sw")

"""'Installation methods'"""

installation_methods_menu = ctk.CTkOptionMenu(root,
                                              values=[
                                                  "Install Plone 6.0.1 with the latest Volto Frontend",
                                                  "Install latest Volto Frontend (Standalone)",
                                                  "Install Plone 6.0.1 Classic (Standalone)"])
installation_methods_menu.place(relx=0.5, rely=0.5, anchor="center")
installation_methods_menu.set(
    "Select an installation method")  # set initial value


def mk_dir_dialogue_pop_up():
    """"Dialog Box for Make Directory"""
    mk_dir_dialogue = ctk.CTkInputDialog(
        text="Enter the name for Installation Directory",
        title="Installation Directory")
    global mk_dir_input
    mk_dir_input = mk_dir_dialogue.get_input()


def user_pass_pop_up():
    user_pass_dialogue = PasswordDialogBox(root, text="Enter you Admin password")
    global user_pass_input
    user_pass_input = user_pass_dialogue.get_input()

def plone_admin_pass_pop_up():
    plone_admin_pass_dialogue = PasswordDialogBox(root, text="Plone Admin Pass")
    global plone_admin_pass_input
    plone_admin_pass_input = plone_admin_pass_dialogue.get_input()

def install_by_selected_method():
    selected_method = installation_methods_menu.get()

    if selected_method == "Select an installation method":
        messagebox.showwarning("Warning",
                               "Please select an installation method.")
    if selected_method == "Install Plone 6.0.1 with the latest Volto Frontend":
        print("1")
    if selected_method == "Install latest Volto Frontend (Standalone)":
        print("2")
    if selected_method == "Install Plone 6.0.1 Classic (Standalone)":
        # Create installation directory

        mk_dir_dialogue_pop_up()
        user_pass_pop_up()
        plone_admin_pass_pop_up()
        os.mkdir(mk_dir_input)
        os.chdir(mk_dir_input)

        # Create progress window with message
        progress_window = ctk.CTk()
        progress_window.geometry("750x460")
        progress_window.title("Installation Progress")

        message_label = ctk.CTkLabel(progress_window,
                                 text="Please wait while installation is in progress...")

        message_label.place(x=10, y=420)

        # Create a Text widget and configure it to be scrollable
        scroll_widget = tk.scrolledtext.ScrolledText(progress_window,
                                                     wrap=tk.WORD)
        scroll_widget.place(relx=0.5, rely=0.45, anchor=tk.CENTER, width=700,
                            height=400)

        def cancel_process():
            pid = os.getpid()
            os.kill(pid, 9)

        cancel_button = ctk.CTkButton(progress_window, text="Cancel",
                                       font=ctk.CTkFont(size=14), width=70,
                                       height=25,command=cancel_process)
        cancel_button.place(relx=0.96, rely=0.96, anchor=tk.SE)

        commands = [
            'sudo apt-get install build-essential',
            'sudo apt-get install python-dev-is-python3',
            'sudo apt-get install libjpeg-dev',
            'sudo apt-get install libxslt-dev',
            'sudo apt-get install python3.8-dev',
            'python3.9 -m venv .',
            'bin/pip install -r https://dist.plone.org/release/6.0.1/requirements.txt',
            './bin/buildout']

        data = f'''[buildout]
extends = https://dist.plone.org/release/6.0.1/versions.cfg
parts = instance
[instance]
recipe = plone.recipe.zope2instance
eggs =
    Plone
    plone.volto
user = admin:{plone_admin_pass_input}
        '''
        with open("buildout.cfg", "w") as f:
            f.write(data)
        # Iterate through the commands list and display the output in the Text widget
        for cmd in commands:
            # Update message label with current command being executed
            message_label.configure(text=f"Running command: {cmd}")
            progress_window.update()
            if cmd == "./bin/buildout":
                with open('buildout.log', 'w') as log_file:
                    # Run the buildout command
                    process = subprocess.Popen('./bin/buildout',
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.STDOUT,
                                               universal_newlines=True)

                    # Print the output in real-time and write it to the log file
                    for stdout_line in iter(process.stdout.readline, ''):
                        log_file.write(stdout_line)
                        scroll_widget.insert(tk.END, stdout_line)
                        scroll_widget.yview(tk.END)
                        progress_window.update()
                    process.wait()
                    return_code = process.returncode
                    log_file.write(str(return_code))

            elif cmd.startswith("sudo"):
                cmd = cmd.split()
                cmd.insert(1,
                           "-S")  # Add -S flag to read password from standard input
                cmd = " ".join(cmd)
                cmd_password = user_pass_input + "\n"
                result = subprocess.run(cmd.split(), capture_output=True,
                                        text=True,
                                        input=cmd_password)
                output_with_sudo = result.stdout.strip() + "\n" + result.stderr.strip()
                scroll_widget.insert(tk.END, output_with_sudo)
                scroll_widget.insert(tk.END, "\n\n")
                scroll_widget.yview(tk.END)
                progress_window.update()

            else:
                result = subprocess.run(cmd.split(), capture_output=True,
                                        text=True)
                # Display command output in Text widget
                output_without_sudo = result.stdout.strip() + "\n" + result.stderr.strip()

                scroll_widget.insert(tk.END, output_without_sudo)
                scroll_widget.insert(tk.END, "\n\n")
                scroll_widget.yview(tk.END)
                progress_window.update()

        if os.path.isfile("buildout.cfg"):
            scroll_widget.insert(tk.END, "Buildout file created")

        # Destroy progress window when installation is complete
        # progress_window.destroy()


"""Install Button"""
install_button = ctk.CTkButton(root, text="Install",
                               font=ctk.CTkFont(size=14), width=70,
                               height=25, command=install_by_selected_method)
install_button.place(x=650, y=400)

# Main Wrap
root.mainloop()
