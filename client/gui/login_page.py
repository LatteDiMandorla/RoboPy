import customtkinter as ctk

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.configure(fg_color="#141B66")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.welcome_label = ctk.CTkLabel(self, text="", font=("Consolas", 26), text_color="#948979")
        self.welcome_label.grid(row=0, column=0, pady=2)
        self.text = "Welcome back! Please log in."
        self.current_text = ""
        self.index = 0

        self.after(100, self.type_writer)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=200)
        self.username_entry.grid(row=1, column=0, pady=10, padx=50)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=200)
        self.password_entry.grid(row=2, column=0, pady=10, padx=50)

        self.login_button = ctk.CTkButton(self, text="Login")
        self.login_button.grid(row=3, column=0, pady=10)

        self.forgot_password = ctk.CTkButton(self, text="Forgot password?", text_color="#808AFF", fg_color="transparent")
        self.forgot_password.grid(row=4, column=0, pady=5)

    # Simple function that allows the animation.
    def type_writer(self):
        if self.index < len(self.text):
            self.current_text += self.text[self.index]
            self.welcome_label.configure(text=self.current_text)
            self.index += 1
            self.after(100, self.type_writer)


