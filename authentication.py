import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import requests
import json

LARGE_FONT= ("Verdana", 12)
#VARIABLES
username=""
url='https://eflask-api.herokuapp.com'
class authentication(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self,default='icon.ico')
        tk.Tk.wm_title(self, 'Authentication')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage ,StartPage, logIn, signUp):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="signUp",
                            command=lambda: controller.show_frame(signUp))
        button.pack()

        button2 = ttk.Button(self, text="logIn",
                            command=lambda: controller.show_frame(logIn))
        button2.pack()




class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Welcome Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Logout",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



def login(username,password):
    #request get(fetching request)
    r=requests.post(f"{url}/<String:{username.get()}>/<String:{password.get()}>")
    response=r.json()
    if response["message"]=="ACCESS GRANTED":
        app.show_frame(WelcomePage)
        msg.showinfo("",'You have successfully logined !')
    else:
        msg.showinfo("",'ACCESS DENIED')


class logIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="LogIn Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        user= ttk.Entry(self, text="USERNAME", font=LARGE_FONT)
        user.pack(pady=10,padx=10)
        loginpass= ttk.Entry(self, text="PASSWORD", font=LARGE_FONT,show ="*")
        loginpass.pack(pady=10,padx=10)
        submit= ttk.Button(self, text="check",
                            command=lambda: login(user,loginpass))
        submit.pack()
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="SignUP",
                            command=lambda: controller.show_frame(signUp))
        button2.pack()



def signup(username,password):
    #print('username : '+username.get(),"password : "+password.get())
    r=requests.post(f"{url}/adduser/{username}/{password})").json()
    if r['message']=='done!!!!!!':
        msg.showinfo("",'Your account has been created !')
        app.show_frame(logIn)
    else:
        msg.showinfo("",'Failed')
class signUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="SignUp", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        username= ttk.Entry(self, text="USERNAME", font=LARGE_FONT)
        username.pack(pady=10,padx=10)
        password= ttk.Entry(self, text="PASSWORD", font=LARGE_FONT,show ="*")
        password.pack(pady=10,padx=10)
        submit = ttk.Button(self, text="SUBMIT",
                            command=lambda: signup(username.get(),password.get()))
        submit.pack()



        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="logIn",
                            command=lambda: controller.show_frame(logIn))
        button2.pack()




app = authentication()
app.geometry("300x200")
app.mainloop()
