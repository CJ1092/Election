# !/usr/bin/python
import os
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from collections import Counter


def screendestroy(screen):
    screen.destroy()

def login_success(): # message box to display login successful message
    tkinter.messagebox.showinfo("Login Success", "You have Logged in successfully")
    screendestroy(screen2)
    options() # function to display the Candidate options

def incorrect_password(): # message box to display password error
    tkinter.messagebox.showinfo("Login Failed", "Incorrect password or username")

def user_not_found(): # message box to display unknown user
    tkinter.messagebox.showinfo("Unknown User", "User not identified")

def register_user(): # function to record the registered user into the list
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successful", fg="green", font=("calibri", 11)).pack()

def register(): # function to register new users
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

def login_verify(): # function to verify the login credentials

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

def login(): # function to login for each user
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


def options(): # function to display the Posts

    screen4 = Toplevel(screen)
    screen4.geometry("720x640")

    Label(screen4, text="").pack()
    Button(screen4, text="Head Boy", width="40", height="2", command=headboy).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Head Girl", width="40", height="2", command=headgirl).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Assistant Head Boy", width="40", height="2", command=asstheadboy).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Assistant Head Girl", width="40", height="2", command=asstheadgirl).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Sports Captain", width="40", height="2", command=sportcap).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Sports Vice Captain", width="40", height="2", command=sportsvicecap).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Cultural Captain", width="40", height="2", command=culturalcap).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Assistant Cultural Captain", width="40", height="2", command=asstcultcap).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Houses", width="50", height="2", command=houses).pack()

####HeadBoy Counter####

def counterHB1():
    counterHB1 = 0
    counterHB1 = counterHB1 + 1

def counterHB2():
    counterHB2 = 0
    counterHB2 = counterHB2+1

def counterHB3():
    counterHB3 = 0
    counterHB3 = counterHB3+1

def counterHB4():
    counterHB4 = 0
    counterHB4 = counterHB4+1

####HeadGirl Counter####
def counterHG1():
    counterHG1 = 0

def counterHG2():
    counterHG2 = 0

def counterHG3():
    counterHG3 = 0

def counterHG4():
    counterHG4 = 0

####AsstHeadBoy Counter####
def counterAHB1():
    counterAHB1 = 0

def counterAHB2():
    counterAHB2 = 0

def counterAHB3():
    counterAHB3 = 0

def counterAHB4():
    counterAHB4 = 0

####AsstHeadGirl Counter####
def counterAHG1():
    counterAHG1 = 0

def counterAHG2():
    counterAHG2 = 0

def counterAHG3():
    counterAHG3 = 0

def counterAHG4():
    counterAHG4 = 0

####Sports Captain Counter####
def counterSC1():
    counterSC1 = 0

def counterSC2():
    counterSC2 = 0

def counterSC3():
    counterSC3 = 0

def counterSC4():
    counterSC4 = 0

####AsstSports Captain Counter####
def counterASC1():
    counterASC1 = 0

def counterASC2():
    counterASC2 = 0

def counterASC3():
    counterASC3 = 0

def counterASC4():
    counterASC4 = 0

####Cultural Secretary Counter####
def counterCS1():
    counterCS1 = 0

def counterCS2():
    counterCS2 = 0

def counterCS3():
    counterCS3 = 0

def counterCS4():
    counterCS4 = 0

####AsstCultural Secretary Counter####
def counterACS1():
    counterACS1 = 0

def counterACS2():
    counterACS2 = 0

def counterACS3():
    counterACS3 = 0

def counterACS4():
    counterACS4 = 0

def houses():
    global screen6
    screen6 = Toplevel(screen)
    screen6.geometry("640x480")
    screen6.title("Houses")

    Label(screen6, text="**** PLEASE SELECT ONLY YOUR RESPECTIVE HOUSE ****").pack()

    Label(screen6, text="").pack()
    Button(screen6, text="Cauvery", width="40", height="2").pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Gangotri", width="40", height="2").pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Narmada", width="40", height="2").pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Periyar", width="40", height="2").pack()

def cauvery():
    counterHC = 0
    counterHVC = 0
    counterJrHC = 0

def gangotri():
    counterHC = 0
    counterHVC = 0
    counterJrHC = 0

def narmada():
    counterHC = 0
    counterHVC = 0
    counterJrHC = 0

def periyar():
    counterHC = 0
    counterHVC = 0
    counterJrHC = 0

def headboy(): # function to display the candidates

    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Head Boy Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1", command=counterHB1).grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1", command=counterHB2).grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1", command=counterHB3).pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1", command=counterHB4).pack()
    candidates = []

def headgirl(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Head Girl Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1", command=counterHG1).grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1", command=counterHG2).grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1", command=counterHG3).pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1", command=counterHG4).pack()
    candidates = []

def asstheadboy(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Assistant Head Boy Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1", command=counterAHB1).grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1", command=counterAHB2).grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1", command=counterAHB3).pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1", command=counterAHB4).pack()
    candidates = []

def asstheadgirl(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Assistant Head Girl Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1", command=counterAHG1).grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1", command=counterAHG2).grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1", command=counterAHG3).pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1", command=counterAHG4).pack()
    candidates = []

def sportcap(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Sports Captain Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1").grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1").grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1").pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1").pack()
    candidates = []

def sportsvicecap(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Sports Vice Captain Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1").grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1").grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1").pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1").pack()
    candidates = []

def culturalcap(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Cultural Captain Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1").grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1").grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1").pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1").pack()
    candidates = []

def asstcultcap(): # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("640x480")
    screen5.title("Assistant Cultural Captain Candidates List")

    Label(screen5, text="C1 ").grid() # grid have left intentation
    Button(screen5, text="C1").grid()
    Label(screen5, text="C2 ").grid()
    Button(screen5, text="C1").grid()
    Label(screen5, text="C3 ").pack() # pack has central intentation
    Button(screen5, text="C1").pack()
    Label(screen5, text="C4 ").pack()
    Button(screen5, text="C1").pack()
    candidates = []


def main_screen(): # main opening screen with logo.
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


