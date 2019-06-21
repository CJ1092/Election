# !/usr/bin/python
import os
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

#  Global counter for headboy
counterHB01 = 0
counterHB02 = 0
counterHB03 = 0

#  Global counter for headgirl
counterHG01 = 0
counterHG02 = 0

#  Global counter for asst headboy
counterAHB01 = 0
counterAHB02 = 0

#  Global counter for asst headgirl
counterAHG01 = 0
counterAHG02 = 0
counterAHG03 = 0

#  Global counter for sports captain
counterSC01 = 0
counterSC02 = 0

#  Global counter for sports vice captain
counterASC01 = 0
counterASC02 = 0
counterASC03 = 0

#  Global counter for cultural captain
counterCS01 = 0

#  Global counter for asst cultural captain
counterACS01 = 0
counterACS02 = 0
counterACS03 = 0
counterACS04 = 0
counterACS05 = 0


def screendestroy(screen):
    screen.destroy()


def login_success():  # message box to display login successful message
    tkinter.messagebox.showinfo("Login Success", "You have Logged in successfully")
    screendestroy(screen2)
    options()  # function to display the Candidate options


def incorrect_password():  # message box to display password error
    tkinter.messagebox.showinfo("Login Failed", "Incorrect password or username")


def user_not_found():  # message box to display unknown user
    tkinter.messagebox.showinfo("Unknown User", "User not identified")


def register_user():  # function to record the registered user into the list
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successful", fg="green", font=("calibri", 11)).pack()


def register():  # function to register new users
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("640x480")

    status = Label(screen1, text="The Choice School", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

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


def login_verify():  # function to verify the login credentials

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    path = "..\SchoolElection"
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


def login():  # function to login for each user
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("%sx%s" % (width, height))

    status = Label(screen2, text="The Choice School", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

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


def options():  # function to display the Posts

    global HB
    global HG
    global AHB
    global AHG
    global SC
    global SVC
    global CS
    global ACS
    global House
    screen4 = Toplevel(screen)
    screen4.geometry("%sx%s" % (width, height))
    screen4.title("Posts")

    # status = Label(screen4, text="The Choice School", bd=1, relief=SUNKEN, anchor=W)
    # status.pack(side=BOTTOM, fill=X)

    Label(screen4, text="").pack()
    HB = Button(screen4, text="Head Boy", width="40", height="2", command=headboy)
    HB.pack()
    Label(screen4, text="").pack()
    HG = Button(screen4, text="Head Girl", width="40", height="2", command=headgirl)
    HG.pack()
    Label(screen4, text="").pack()
    AHB = Button(screen4, text="Assistant Head Boy", width="40", height="2", command=asstheadboy)
    AHB.pack()
    Label(screen4, text="").pack()
    AHG = Button(screen4, text="Assistant Head Girl", width="40", height="2", command=asstheadgirl)
    AHG.pack()
    Label(screen4, text="").pack()
    SC = Button(screen4, text="Sports Captain", width="40", height="2", command=sportcap)
    SC.pack()
    Label(screen4, text="").pack()
    SVC = Button(screen4, text="Sports Vice Captain", width="40", height="2", command=sportsvicecap)
    SVC.pack()
    Label(screen4, text="").pack()
    CS = Button(screen4, text="Cultural Captain", width="40", height="2", command=culturalcap)
    CS.pack()
    Label(screen4, text="").pack()
    ACS = Button(screen4, text="Assistant Cultural Captain", width="40", height="2", command=asstcultcap)
    ACS.pack()
    Label(screen4, text="").pack()
    House = Button(screen4, text="Houses", width="50", height="2", command=houses)
    House.pack()


#   HeadBoy Counter
def counterHB1():
    global counterHB01
    counterHB01 = counterHB01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterHB01)
    filename = open("Kiran Shankar", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterHB2():
    global counterHB02
    counterHB02 = counterHB02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterHB02)
    filename = open("Joel Geemon Korah", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterHB3():
    global counterHB03
    counterHB03 = counterHB03 + 1
    counterhb1fin = []
    counterhb1fin.append(counterHB03)
    filename = open("Arvind Thadi", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   HeadGirl Counter
def counterHG1():
    global counterHG01
    counterHG01 = counterHG01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterHG01)
    filename = open("Ann Maria Dominic", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterHG2():
    global counterHG02
    counterHG02 = counterHG02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterHG02)
    filename = open("Maria Charles", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   AsstHeadBoy Counter
def counterAHB1():
    global counterAHB01
    counterAHB01 = counterAHB01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterAHB01)
    filename = open("Mathew Rajesh", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterAHB2():
    global counterAHB02
    counterAHB02 = counterAHB02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterAHB02)
    filename = open("Siddharth Menon", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   AsstHeadGirl Counter
def counterAHG1():
    global counterAHG01
    counterAHG01 = counterAHG01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterAHG01)
    filename = open("Brooke Mariam George", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterAHG2():
    global counterAHG02
    counterAHG02 = counterAHG02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterAHG02)
    filename = open("Rachel Batra", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterAHG3():
    global counterAHG03
    counterAHG03 = counterAHG03 + 1
    counterhb1fin = []
    counterhb1fin.append(counterAHG03)
    filename = open("Anya Mathew", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   Sports Captain Counter
def counterSC1():
    global counterSC01
    counterSC01 = counterSC01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterSC01)
    filename = open("Elisheba Naveen", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()

def counterSC2():
    global counterSC02
    counterSC02 = counterSC02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterSC02)
    filename = open("Sachin Koshy", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   AsstSports Captain Counter
def counterASC1():
    global counterASC01
    counterASC01 = counterASC01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterASC01)
    filename = open("Hannah Mariam Paul", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterASC2():
    global counterASC02
    counterASC02 = counterASC02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterASC02)
    filename = open("Karthikey Manoj", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterASC3():
    global counterASC03
    counterASC03 = counterASC03 + 1
    counterhb1fin = []
    counterhb1fin.append(counterASC03)
    filename = open("Jaik Kuruvilla Tom", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   Cultural Secretary Counter
def counterCS1():
    global counterCS01
    counterCS01 = counterCS01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterCS01)
    filename = open("Khadija Mehnaaz", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


#   AsstCultural Secretary Counter
def counterACS1():
    global counterACS01
    counterACS01 = counterACS01 + 1
    counterhb1fin = []
    counterhb1fin.append(counterACS01)
    filename = open("Megan Jacob", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterACS2():
    global counterACS02
    counterACS02 = counterACS02 + 1
    counterhb1fin = []
    counterhb1fin.append(counterACS02)
    filename = open("Maria Georgy", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterACS3():
    global counterACS03
    counterACS03 = counterACS03 + 1
    counterhb1fin = []
    counterhb1fin.append(counterACS03)
    filename = open("Anoushka Thiruvilakat", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterACS4():
    global counterACS04
    counterACS04 = counterACS04 + 1
    counterhb1fin = []
    counterhb1fin.append(counterACS04)
    filename = open("Gowri Nair", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def counterACS5():
    global counterACS05
    counterACS05 = counterACS05 + 1
    counterhb1fin = []
    counterhb1fin.append(counterACS05)
    filename = open("Ruth Sara Abraham", 'w')
    filename.write("The number of votes are " + str(counterhb1fin))
    filename.close()


def houses():
    global screen6
    screen6 = Toplevel(screen)
    screen6.geometry("640x480")
    screen6.title("Houses")

    Label(screen6, text="**** PLEASE SELECT ONLY YOUR RESPECTIVE HOUSE ****").pack()

    Label(screen6, text="").pack()
    Button(screen6, text="Cauvery", width="40", height="2", command=cauvery).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Gangotri", width="40", height="2", command=gangotri).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Narmada", width="40", height="2", command=narmada).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Periyar", width="40", height="2", command=periyar).pack()
    House.config(state=DISABLED, text="VOTED", fg="red")


def cauvery():

    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("640x480")
    screen7.title("Cauvery")

    Label(text="").pack()
    Button(text="House Captain", width="30", height="2", command=housecapcav).pack()
    Label(text="").pack()
    Button(text="House Vice Captain", width="30", height="2", command=houseviccapcav).pack()
    Label(text="").pack()
    Button(text="Junior House Captain", width="30", height="2", command=jrhousecapcav).pack()


def gangotri():

    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("640x480")
    screen7.title("Gangotri")

    Label(text="").pack()
    Button(text="House Captain", width="30", height="2", command=housecapgan).pack()
    Label(text="").pack()
    Button(text="House Vice Captain", width="30", height="2", command=houseviccapgan).pack()
    Label(text="").pack()
    Button(text="Junior House Captain", width="30", height="2", command=jrhousecapgan).pack()


def narmada():

    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("640x480")
    screen7.title("Narmada")

    Label(text="").pack()
    Button(text="House Captain", width="30", height="2", command=housecapnar).pack()
    Label(text="").pack()
    Button(text="House Vice Captain", width="30", height="2", command=houseviccapnar).pack()
    Label(text="").pack()
    Button(text="Junior House Captain", width="30", height="2", command=jrhousecapnar).pack()


def periyar():

    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("640x480")
    screen7.title("Periyar")

    Label(text="").pack()
    Button(text="House Captain", width="30", height="2", command=housecapper).pack()
    Label(text="").pack()
    Button(text="House Vice Captain", width="30", height="2", command=houseviccapper).pack()
    Label(text="").pack()
    Button(text="Junior House Captain", width="30", height="2", command=jrhousecapper).pack()


def housecapcav():
    Label(text="").pack()

def housecapgan():
    Label(text="").pack()

def housecapnar():
    Label(text="").pack()

def housecapper():
    Label(text="").pack()

def houseviccapcav():
    Label(text="").pack()

def houseviccapgan():
    Label(text="").pack()

def houseviccapnar():
    Label(text="").pack()

def houseviccapper():
    Label(text="").pack()

def jrhousecapcav():
    Label(text="").pack()
    Button(text="Athulya Rajesh", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Nandini Nair", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Miriya Jimmy", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Saira Celin", width="40", height="2").pack()

def jrhousecapgan():
    Label(text="").pack()
    Button(text="Lakshmi Neeliyath", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Kevin Zavier", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Vaibhav Lal", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Rahul Thanikkan", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Rebecca Harrison", width="40", height="2").pack()

def jrhousecapnar():
    Label(text="").pack()
    Button(text="Ruth", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Vania Eliza", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Neha Jayan", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Tanu George", width="40", height="2").pack()

def jrhousecapper():
    Label(text="").pack()
    Button(text="George Philip", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Gopika Kumar", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Anoushka Panicker", width="40", height="2").pack()
    Label(text="").pack()
    Button(text="Zoha Rashid", width="40", height="2").pack()


def headboy():  # function to display the candidates

    # global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Head Boy Candidates List")
    print ("Functioning")
    Label(screen5, text="Kiran Shankar").grid()  # grid have left intentation
    Button(screen5, text="VOTE", command=counterHB1).grid()
    Label(screen5, text="Joel Geemon Korah").grid()
    Button(screen5, text="VOTE", command=counterHB2).grid()
    Label(screen5, text="Arvind Thadi").pack()  # pack has central intentation
    Button(screen5, text="VOTE", command=counterHB3).grid()
    HB.config(state=DISABLED, text="VOTED", fg="red")


def headgirl():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Head Girl Candidates List")
    Label(screen5, text="Ann Maria Dominic").grid()  # grid have left intentation
    Button(screen5, text="VOTE", command=counterHG1).grid()
    Label(screen5, text="Maria Charles").grid()
    Button(screen5, text="VOTE", command=counterHG2).grid()
    HG.config(state = DISABLED, text="VOTED", fg="red")


def asstheadboy():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Assistant Head Boy Candidates List")

    Label(screen5, text="Mathew Rajesh").grid()  # grid have left intentation
    Button(screen5, text="VOTE", command=counterAHB1).grid()
    Label(screen5, text="Siddharth Menon").grid()
    Button(screen5, text="VOTE", command=counterAHB2).grid()
    AHB.config(state=DISABLED, text="VOTED", fg="red")


def asstheadgirl():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Assistant Head Girl Candidates List")

    Label(screen5, text="Brooke Mariam George").grid()  # grid have left intentation
    Button(screen5, text="VOTE", command=counterAHG1).grid()
    Label(screen5, text="Rachel Batra").grid()
    Button(screen5, text="VOTE", command=counterAHG2).grid()
    Label(screen5, text="Anya Mathew").pack()  # pack has central intentation
    Button(screen5, text="VOTE", command=counterAHG3).grid()
    AHG.config(state=DISABLED, text="VOTED", fg="red")


def sportcap():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Sports Captain Candidates List")

    Label(screen5, text="Elisheba Naveen").grid()  # grid have left intentation
    Button(screen5, text="VOTE", command=counterSC1).grid()
    Label(screen5, text="Sachin Koshy").grid()
    Button(screen5, text="VOTE", command=counterSC2).grid()
    SC.config(state=DISABLED, text="VOTED", fg="red")


def sportsvicecap():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Sports Vice Captain Candidates List")

    Label(screen5, text="Hannah Mariam Paul").grid()  # grid have left intentation
    Button(screen5, text="VOTE", command=counterASC1).grid()
    Label(screen5, text="Karthikey Manoj").grid()
    Button(screen5, text="VOTE", command=counterASC2).grid()
    Label(screen5, text="Jaik Kuruvilla Tom").grid()
    Button(screen5, text="VOTE", command=counterASC2).grid()
    SVC.config(state = DISABLED, text="VOTED", fg="red")

def culturalcap():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Cultural Captain Candidates List")

    Label(screen5, text="Khadija Mehanaaz").grid() # grid have left intentation
    Button(screen5, text="VOTE", command=counterCS1).grid()
    CS.config(state=DISABLED, text="VOTED", fg="red")

def asstcultcap():  # function to display the candidates

    screen5 = Toplevel(screen)
    screen5.geometry("720x640")
    screen5.title("Assistant Cultural Captain Candidates List")

    Label(screen5, text="Megan Jacob").grid() # grid have left intentation
    Button(screen5, text="VOTE", command=counterACS1).grid()
    Label(screen5, text="Maria Georgy").grid() # grid have left intentation
    Button(screen5, text="VOTE", command=counterACS2).grid()
    Label(screen5, text="Anoushka Thiruvillakat").grid() # grid have left intentation
    Button(screen5, text="VOTE", command=counterACS3).grid()
    Label(screen5, text="Gowri Nair").grid() # grid have left intentation
    Button(screen5, text="VOTE", command=counterACS4).grid()
    Label(screen5, text="Ruth Sarah Abraham").grid() # grid have left intentation
    Button(screen5, text="VOTE", command=counterACS5).grid()
    ACS.config(state=DISABLED, text="VOTED", fg="red")

def main_screen():  # main opening screen with logo.
    global screen
    global width
    global height

    screen = Tk()
    width = screen.winfo_screenwidth()
    height = screen.winfo_screenheight()
    screen.geometry("%sx%s" % (width, height))
    screen.title("Choice School Election 2019-20")

    photo = ImageTk.PhotoImage(Image.open("logo.png"))
    Label(image=photo).pack()

    status = Label(text="The Choice School", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    Label(text="Student Council Election 2019-20", bg = "grey", width="720", height="3", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="40", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="40", command=register).pack()

    screen.mainloop()


main_screen()


