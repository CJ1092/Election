# !/usr/bin/python
import os
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox

def login_success():
    tkinter.messagebox.showinfo("Login Success", "You have Logged in successfully")
    options()

def incorrect_password():
    tkinter.messagebox.showinfo("Login Failed", "Incorrect password or username")

def user_not_found():
    tkinter.messagebox.showinfo("Unknown User", "User not identified")

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successful", fg="green", font=("calibri", 11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("640x480")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text="Username ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="30", command=register_user).pack()

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    path = "C:\Users\Cyriac\PycharmProjects\SchoolElection"
    list_of_files = os.listdir(path)
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            incorrect_password()
    else:
        user_not_found()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("640x480")
    Label(screen2, text="Please enter details below to Login").pack()
    Label(screen2, text=" ").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width="30", height="3", command=login_verify).pack()

def options():

    screen4 = Toplevel(screen)
    screen4.geometry("720x640")

    Label(screen4, text="").pack()
    Button(screen4, text="Head Boy", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Head Girl", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Assistant Head Boy", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Assistant Head Girl", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Sports Captain", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Sports Vice Captain", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Cultural Captain", width="40", height="3").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Assistant Cultural Captain", width="40", height="3").pack()


def headboy():

    global screen3

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def headgirl():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def asstheadboy():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def asstheadgirl():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def sportcap():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def sportsvicecap():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def culturalcap():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0

def asstcultcap():

    Label(screen3, text="C1 ").pack()
    Label(screen3, text="C2 ").pack()
    Label(screen3, text="C3 ").pack()
    Label(screen3, text="C4 ").pack()
    candidates = []
    counter = 0



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("720x640")
    screen.title("Choice School Election 2019-20")

    photo = ImageTk.PhotoImage(Image.open("logo.png"))
    Label(image=photo).pack()

    Label(text="Student Council Election 2019-20", bg = "grey", width="720", height="3", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="40", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="40", command=register).pack()

    screen.mainloop()

main_screen()


