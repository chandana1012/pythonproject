from tkinter import*
import os
import time

def delete2():
    screen2.destroy()
    

def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()    

def login_success():
    #global screen3
    #screen3=Toplevel(screen)
    #screen3.title("success")
    #screen3.geometry("150x100")
    #Label(screen3,text="Login successfull").pack()
    #Button(screen3,text="OK",command=delete2).pack()
    Label(screen2,text="login successfull...").pack()
    


def password_not_recognised():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("password")
    screen4.geometry("150x100")
    Label(screen4,text="wrong password").pack()
    Button(screen4,text="OK",command=delete3).pack()


def user_not_found():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("user")
    screen5.geometry("150x100")
    Label(screen5,text="user does not exist").pack()
    Button(screen5,text="OK",command=delete4).pack()    
    


def enter_user():
    
    global username_info
    global password_info
    
    username_info=username.get()
    password_info=password.get()
    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    #username_entry.delete(0,END)
    #password_entry.delete(0,END)
    
def submit():
    Label(screen1,text="Registration successful",fg="green",font=("calibri",11)).pack()

def successfull():
    Label(screen3,text="successful......").pack()
def unsuccessfull():
    Label(screen3,text="unsuccessful......").pack()

    
def level2verify():
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
    lt1=[]    
    for i in verify[2::1]:
        lt1.append(i)
    if lt1==lt:
        successfull()
    else:
        unsuccessfull()

        
def appred():
    lt.append(rc)
def appblue():
    lt.append(bc)
def appgreen():
    lt.append(gc)    



def level2password():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("collerpassword")
    screen3.geometry("500x500")
    delete2()
    
    Label(screen3,text="ENTER COLOR PASSWORD ").pack()
    Label(screen3,text="").pack()
    
    global rc,bc,gc
    rc="re0d128"
    bc="blu0e27"
    gc="gree0n9"
    global lt
    lt=[]
    Button(screen3,bg="red",width=8,height=1,command=appred).pack()
    Button(screen3,bg="blue",width=8,height=1,command=appblue).pack()
    Button(screen3,bg="green",width=8,height=1,command=appgreen).pack()
    Label(screen3,text="").pack()
    code=StringVar()
    colorpassword_entry=Entry(screen3,textvariable=code)
    colorpassword_entry.pack()
    Label(screen3,text="").pack()
    Button(screen3,text="verify",width=10,height=1,command=level2verify).pack()

    
def login_verify():
    global username1
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_success()
            level2password()
        else:
            password_not_recognised()
    else:
        user_not_found()

def red_code():
    rc="re0d128"
    file=open(username_info,"a")
    file.write('\n'+rc)
    file.close()
    code.set("*********")
    
def blue_code():
    bc="blu0e27"
    file=open(username_info,"a")
    file.write('\n'+bc)
    file.close()
    code.set("*********")

def green_code():
    gc="gree0n9"
    file=open(username_info,"a")
    file.write('\n'+gc)
    file.close()
    code.set("*********")    

def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x500")
    
    global username
    global password

    global code
    
    global username_entry
    global password_entry

    username=StringVar()
    password=StringVar()

    code=StringVar()
    
    Label(screen1,text="ENTER DETAILS FOR LEVEL 1 AUTHENTICATION").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username * ").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password * ").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="enter",width=10,height=1,command=enter_user).pack()
    Label(screen1,text="").pack()
    
    Label(screen1,text="ENTER COLOR PASSWORD FOR LEVEL 2 AUTHENTICATION").pack()
    Label(screen1,text="").pack()
    
    Button(screen1,bg="red",width=8,height=1,command=red_code).pack()
    Button(screen1,bg="blue",width=8,height=1,command=blue_code).pack()
    Button(screen1,bg="green",width=8,height=1,command=green_code).pack()
    Label(screen1,text="").pack()
    
    colorpassword_entry=Entry(screen1,textvariable=code)
    colorpassword_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="submit",width=10,height=1,command=submit).pack()
    

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x350")

    global username_verify
    global password_verify

    global username_entry1
    global password_entry1

    username_verify=StringVar()
    password_verify=StringVar()

    
    Label(screen2,text="login with valid userid").pack()
    Label(screen2,text="").pack()
    Label(screen2,text="username * ").pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="password * ").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",width=10,height=1,command=login_verify).pack()
    
    
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("500x450")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0",bg="grey",width="300",height="2",font=("calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",bg="yellow",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Register",bg="yellow",height="2",width="30",command=register).pack()
    screen.mainloop()


main_screen()


