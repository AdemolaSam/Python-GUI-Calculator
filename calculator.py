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

screen_txt_var = StringVar(value="")

screen_var = []

input_var = StringVar(value="")

def get_btn_value(btn, screen_var):
    """Get the value of the pressed button
        assign it to the screen_var variable
        assign the screen_var variable to the screen_text_var variable and display it
    """
    key_input = btn.cget("text")
    screen_var.append(str(key_input))
    screen_txt_var.set(" ".join(screen_var))
    print("".join(screen_var))

def evaluate():
    """evaluate the expression on the screen"""
    try:
        result = eval("".join(screen_var))
        screen_txt_var.set(screen_txt_var.get() + "\n" + str(result))
        print(result)
    except Exception as err:
        print(str(err))

def delete():
    """Delete values on the screen"""
    global screen_var
    screen_var = screen_var[:-1]
    screen_txt_var.set(" ".join(screen_var))
    print(screen_txt_var.get())

def clear():
    """Clear values on the screen"""
    global screen_var
    screen_var = []
    screen_txt_var.set(screen_var)

# Fonts
screen_font = ctk.CTkFont(family="Arial", size=20)
btn_font = ctk.CTkFont(family="Arial", size=16)

screen = ctk.CTkLabel(master=frame, 
                        textvariable=screen_txt_var,
                        width=360,
                        height=100,
                        fg_color="grey",
                        font=screen_font,
                        anchor="w")

screen.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

numbers = [1,2,3,4,5,6,7,8,9,0,"*","-","+","/","."]

rel_x = 0.3
for num in numbers[:5]:
    num_btn = ctk.CTkButton(master=frame, text=num, width=50, height=40, font=btn_font)
    num_btn.place(relx=rel_x, rely=0.35, anchor=tk.CENTER)
    num_btn.configure(command=lambda btn=num_btn: get_btn_value(btn, screen_var))
    rel_x += 0.15 

rel_x = 0.3
for num in numbers[5:10]:
    num_btn = ctk.CTkButton(master=frame, text=num, width=50, height=40, font=btn_font)
    num_btn.place(relx=rel_x, rely=0.5, anchor=tk.CENTER)
    num_btn.configure(command=lambda btn=num_btn: get_btn_value(btn, screen_var))
    rel_x += 0.15

rel_x = 0.3
for num in numbers[10::]:
    num_btn = ctk.CTkButton(master=frame, text=num, width=50, height=40, font=btn_font)
    num_btn.place(relx=rel_x, rely=0.65, anchor=tk.CENTER)
    num_btn.configure(command=lambda btn=num_btn: get_btn_value(btn, screen_var))
    rel_x += 0.15

del_btn = ctk.CTkButton(master=frame, text="DEL", width=50, height=40,font=btn_font,command=delete)
del_btn.place(relx=0.15, rely=0.35, anchor=tk.CENTER)

clear_all_btn = ctk.CTkButton(master=frame, text="CLR", width=50, height=40, font=btn_font,command=clear)
clear_all_btn.place(relx=0.15, rely=0.50, anchor=tk.CENTER)

equal_btn = ctk.CTkButton(master=frame, text="=", width=50, height=40, font=btn_font,command=evaluate)
equal_btn.place(relx=0.15, rely=0.65, anchor=tk.CENTER)

app.mainloop()