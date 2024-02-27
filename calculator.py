import tkinter as tk
import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("GUI Calculator")
app.geometry("400x500")


frame = ctk.CTkFrame(master=app,
                     width=380,
                     height=460,
                     fg_color="black",
                     corner_radius=10)

frame.pack(padx=0, pady=20)

text_var_screen = StringVar(value="")

screen_var = ""

input_var = StringVar(value="")

def get_btn_value(button):
    value = button.cget("text")
    print(value)

screen = ctk.CTkLabel(master=frame, 
                        textvariable=text_var_screen,
                        width=360,
                        height=100,
                        fg_color="grey")

screen.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

numbers = [1,2,3,4,5,6,7,8,9,0,"*","-","+","/","."]

rel_x = 0.3
for num in numbers[:5]:
    num_btn = ctk.CTkButton(master=frame, text=num, width=50, height=40, command=get_btn_value)
    num_btn.place(relx=rel_x, rely=0.35, anchor=tk.CENTER)
    rel_x += 0.15 

rel_x = 0.3
for num in numbers[5:10]:
    num_btn = ctk.CTkButton(master=frame, text=num, width=50, height=40, command=get_btn_value)
    num_btn.place(relx=rel_x, rely=0.5, anchor=tk.CENTER)
    rel_x += 0.15

rel_x = 0.3
for num in numbers[10::]:
    num_btn = ctk.CTkButton(master=frame, text=num, width=50, height=40, command=get_btn_value)
    num_btn.place(relx=rel_x, rely=0.65, anchor=tk.CENTER)
    rel_x += 0.15

clear_btn = ctk.CTkButton(master=frame, text="CLR", width=50, height=40)
clear_btn.place(relx=0.15, rely=0.35, anchor=tk.CENTER)

clear_all_btn = ctk.CTkButton(master=frame, text="AC", width=50, height=40)
clear_all_btn.place(relx=0.15, rely=0.50, anchor=tk.CENTER)

clear_all_btn = ctk.CTkButton(master=frame, text="=", width=50, height=40)
clear_all_btn.place(relx=0.15, rely=0.65, anchor=tk.CENTER)

app.mainloop()