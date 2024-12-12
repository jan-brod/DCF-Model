import dcf as dcf
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x350")

def login():
    print("Test successful!")

frame = ctk.CTkFrame(master=root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = ctk.CTkLabel(master = frame, text = "TEST", )

root.mainloop()