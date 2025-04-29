import customtkinter as ctk
from login_page import LoginFrame


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RoboPY")
        self.geometry("600x500")
        self.resizable(False, False)
        self.configure(fg_color="#141B66")
        self.active_frame = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_login()


    # Checks if there is an active frame. If this is the case, then destroys the frame,
    # otherwhise, show LoginFrame.
    def show_login(self):
        if self.active_frame is not None:
            self.active_frame.destroy()

        self.active_frame = LoginFrame(self)
        self.active_frame.grid(row=0, column=0, sticky="ew")


    def close_app(self):
        app.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()

