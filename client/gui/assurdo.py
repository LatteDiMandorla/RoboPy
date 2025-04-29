import customtkinter as ctk
import tkinter as tk
from PIL import Image
import time
import threading
import os
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")




first_path = os.path.join(os.path.dirname(__file__), "assets", "send.png")
second_path = os.path.join(os.path.dirname(__file__), "assets", "mic.png")
third_path = os.path.join(os.path.dirname(__file__), "assets", "logout.png")


first_image = ctk.CTkImage(light_image=Image.open(first_path),
                           dark_image=Image.open(first_path), 
                           size=(17,17))

second_image = ctk.CTkImage(light_image=Image.open(second_path),
                            dark_image=Image.open(second_path),
                            size=(24,24))

third_image = ctk.CTkImage(light_image=Image.open(third_path),
                           dark_image=Image.open(third_path),
                           size=(12,12))


class RoboPYApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1000x600")
        self.configure(bg="#1E1E1E")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#111111")
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="RoboPY",
            font=ctk.CTkFont(family="Consolas", size=24),
            text_color="#948979"
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.first_button = ctk.CTkButton(
            self.sidebar_frame,
            text="First Button",
            font=ctk.CTkFont(family="FiraCode")
        )
        self.first_button.grid(row=1, column=0, padx=20, pady=10)

        self.second_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Second Button",
            font=ctk.CTkFont(family="Consolas")
        )
        self.second_button.grid(row=2, column=0, padx=20, pady=10)

        self.close_button = ctk.CTkButton(
            self.sidebar_frame,
            text="",
            fg_color="#950101",
            hover_color="#FF0000",
            text_color="white",
            width=10,
            image=third_image,
            command=self.destroy
        )
        self.close_button.grid(row=5, column=0, padx=20, pady=20, sticky="w")

        # main chat area
        self.console_frame = ctk.CTkFrame(self, fg_color="#1E1E1E")
        self.console_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.console_frame.grid_rowconfigure(0, weight=1)
        self.console_frame.grid_rowconfigure(1, weight=0)
        self.console_frame.grid_columnconfigure(0, weight=1)

        self.messages_frame = ctk.CTkScrollableFrame(
            self.console_frame,
            fg_color="#1E1E1E",
            corner_radius=5
        )
        self.messages_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.messages_frame.grid_columnconfigure(0, weight=1)
        
        # Message counter used to track position of message in the CTkScrollableFrame.
        self.message_counter = 0
        
        self.entry_frame = ctk.CTkFrame(self.console_frame, fg_color="#1E1E1E", corner_radius=0)
        self.entry_frame.grid(row=1, column=0, sticky="sew", padx=30, pady=5)
        self.entry_frame.grid_columnconfigure(0, weight=1)

        self.input_entry = ctk.CTkEntry(
            self.entry_frame,
            placeholder_text="Scrivi un messaggio...",
            fg_color="#414141",
            text_color="#948979",
            font=("FiraCode", 14),
            border_width=1,
            corner_radius=9,
            height=80
        )
        self.input_entry.grid(row=2, column=0, sticky="ew", padx=20)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = ctk.CTkButton(
            self.entry_frame,
            text="",
            command=self.send_message,
            image=first_image,
            width=40, height=30
        )
        self.send_button.grid(row=2, column=1, sticky="n")

        self.register_button = ctk.CTkButton(
            self.entry_frame,
            text="",
            width=40, height=20,
            image=second_image
        )
        self.register_button.grid(row=2, column=1, stick="s")
        
        self.animation_in_progress = False
        self.animation_thread = None

    def send_message(self, event=None):
        msg = self.input_entry.get().strip()
        if not msg:
            return
            
        self.add_message(msg, is_user=True)
        
        response = self.generate_response(msg)
        
        if self.animation_thread and self.animation_thread.is_alive():
            self.animation_in_progress = False
            self.animation_thread.join()
        # Create a thread for scripting animation.
        self.animation_thread = threading.Thread(target=self.animate_response, args=(response,))
        self.animation_thread.daemon = True
        self.animation_thread.start()
        
        self.input_entry.delete(0, "end")

    def add_message(self, message, is_user=False):
        message_frame = ctk.CTkFrame(
            self.messages_frame,
            fg_color="#333333" if is_user else "#2A3B4D",
            corner_radius=10
        )
        
        row_position = self.message_counter
        self.message_counter += 1
        
        # Allign to right if the message is from user,
        # to left if the message is frome RoboPY.
        message_frame.grid(
            row=row_position, 
            column=0, 
            pady=5, 
            padx=10, 
            sticky="e" if is_user else "w"
        )
        
        sender = "You" if is_user else "RoboPY"
        sender_label = ctk.CTkLabel(
            message_frame,
            text=sender,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold"),
            text_color="#CCCCCC",
            anchor="w"
        )
        sender_label.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 0))
        
        message_label = ctk.CTkLabel(
            message_frame,
            text=message,
            font=ctk.CTkFont(family="FiraCode", size=14),
            text_color="#FFFFFF",
            anchor="w",
            justify="left",
            wraplength=600
        )
        message_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 5))
        
        message_frame.grid_columnconfigure(0, weight=1)
        
        self.after(100, self.scroll_to_bottom)
        
        return message_frame, message_label

    def animate_response(self, full_response):
        self.animation_in_progress = True
        self.set_input_state(False)
        message_frame, message_label = self.add_message("", is_user=False)
        
        displayed_text = ""
        for char in full_response:
            if not self.animation_in_progress:
                break
                
            displayed_text += char
            
            self.after(0, lambda t=displayed_text: message_label.configure(text=t))
            
            time.sleep(0.03)
            
        if self.animation_in_progress:
            self.after(0, lambda: message_label.configure(text=full_response))
        
        self.animation_in_progress = False
        self.set_input_state(True)
        self.scroll_to_bottom()
    
    def scroll_to_bottom(self):
        try:
            self.messages_frame._parent_canvas.yview_moveto(1.0)
        except Exception as e:
            print(f"Errore durante lo scrolling: {e}")
            
    def generate_response(self, msg):
        # Just an example of a long response, in order to test layout.
        return "Grazie per il tuo messaggio. Sto elaborando la tua richiesta e ti risponderò a breve. Ecco un messaggio di esempio per dimostrare l'animazione di scrittura carattere per carattere con un testo abbastanza lungo."
     

    def set_input_state(self, enabled=True):
        if enabled:
            self.input_entry.configure(state="normal")
            self.send_button.configure(state="normal")
        else:
            self.input_entry.configure(state="disabled")
            self.send_button.configure(state="disabled")



if __name__ == "__main__":
    app = RoboPYApp()
    app.mainloop()
