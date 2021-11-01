class User():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        return (f'{self.name} \n'
                f'{self.age} \n'
                )



class Bank(User):
    def __init__(self,name,age,balance):
        super().__init__(name,age)
        self.balance=balance

    def deposite(self,depamount):
        self.depamount=depamount
        self.balance+=self.depamount
        return self.balance


    def withdraw(self,withamount):
        if withamount<self.balance:
            self.balance-=withamount
            print(f'your balance is {self.balance}')
        else:
             print('not enough money in the account')





    def showbalance(self):
        self.show_details()
        return ((f'Name              {self.name} \n'
                f'Age                  {self.age} \n' 
                f'Balance           {self.balance}'))


from tkinter import *

from PIL import ImageTk, Image
import csv
from itertools import zip_longest
import os
import mysql.connector
from tkinter import messagebox
try:
    db=mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='hlove123H@',
        database="customers_info"



        )
    mycursor = db.cursor()
    #
    names = []
    ages = []
    Genders = []
    Passwords = []


    # with open("C:/Users/GTX/Desktop/sy/Bank.csv", "a") as file:
    #   wr = csv.writer(file)
    #  wr.writerow(["Name","Age","Gender","Password"])
    # login
    def login():
        def depwindow():

            mycursor.execute(f'select * from customer where customer_name="{loginuser}"')
            accbalance = mycursor.fetchone()[2]
            depositeamount = temp_Depositeamount.get()
            if depositeamount > 0:
                accbalance += depositeamount
                mycursor.execute(
                    f"UPDATE customer SET customer_balance = '{accbalance}' WHERE customer_name='{loginuser}'")
                db.commit()

                Label(depostie_screen, text="please Enter Number above 0", fg='white').place(x=45, y=140)
                Label(depostie_screen, text="Done", fg='green', font=('consolas', 14)).place(x=120, y=140)

            else:
                Label(depostie_screen, text="please Enter Number above 0", fg='red').place(x=45, y=140)

        def deposite():
            global depostie_screen
            global temp_Depositeamount
            temp_Depositeamount = IntVar()
            depostie_screen = Toplevel(loginsuc)
            depostie_screen.geometry('300x300')
            depostie_screen.resizable(0, 0)
            r = 0
            pos = 0
            for i in range(100):
                color = str(211110 + r)
                Frame(depostie_screen, width=10, height=700, bg='#' + color).place(x=pos, y=0)
                pos += 10
                r += 1
            Frame(depostie_screen, width=250, height=250, bg='white').place(x=25, y=30)
            Label(depostie_screen, text='Enter the amount', font=('consolas', 14)).place(x=68, y=30)
            Entry(depostie_screen, textvariable=temp_Depositeamount, width=20, border=0, font=1).place(x=60, y=60)
            Frame(depostie_screen, width=182, height=2, bg='black').place(x=60, y=79)
            Button(depostie_screen, text="Deposite", command=depwindow, border=0, bg='#994422', fg="white",
                   font=('consolas', 12), width=25).place(x=35, y=100)

            mainloop()

        def withwindow():
            mycursor.execute(f'select * from customer where customer_name="{loginuser}"')
            accbalance = mycursor.fetchone()[2]
            x = Label(with_screen, font=('calibri', 10))
            x.place(x=55, y=130)
            x1 = Label(with_screen, font=('calibri', 10))
            x1.place(x=55, y=130)

            withdrawamount = temp_withdraw.get()

            if withdrawamount > 0:
                if withdrawamount <= accbalance:
                    accbalance -= withdrawamount
                    mycursor.execute(
                        f"UPDATE customer SET customer_balance = '{accbalance}' WHERE customer_name='{loginuser}'")
                    db.commit()

                    x1.config(text="Please Enter Value over 0 ", fg='white')
                    x.config(text="Done", fg='green')

                else:
                    x.config(text="The account balance \n not enough to continue the process ", fg='red')

            if withdrawamount == 0:
                x.config(text="The account balance \n not enough to continue the process ", fg='white')
                x1.config(text="Please Enter Value over 0 ", fg='red')

        global withdraw

        def withdraw():

            global with_screen
            global temp_withdraw
            temp_withdraw = IntVar()
            with_screen = Toplevel(loginsuc)
            with_screen.geometry('300x300')
            with_screen.resizable(0, 0)
            r = 0
            pos = 0
            for i in range(100):
                color = str(211110 + r)
                Frame(with_screen, width=10, height=700, bg='#' + color).place(x=pos, y=0)
                pos += 10
                r += 1
            Frame(with_screen, width=250, height=250, bg='white').place(x=25, y=30)
            Label(with_screen, text='Enter the amount', font=('consolas', 14)).place(x=68, y=30)
            Entry(with_screen, textvariable=temp_withdraw, width=20, border=0, font=1).place(x=60, y=60)
            Frame(with_screen, width=182, height=2, bg='black').place(x=60, y=79)
            # Button(with_screen,text="Withdraw",command=withwindow).grid(row=3)
            Button(with_screen, text="Withdraw", command=withwindow, border=0, bg='#994422', fg="white",
                   font=('consolas', 12), width=25).place(x=35, y=100)

            mainloop()

        # login funcs
        def back():
            window.deiconify()
            login_screen.withdraw()

        def show2():

            mycursor.execute(f'SELECT * FROM customer where customer_name ="{loginuser}"')
            data = mycursor.fetchone()

            customer = Bank(data[0], data[1], data[2])
            Label(loginsuc, text=customer.showbalance(), font=('calibri', 13)).place(x=100, y=315)
            Frame(loginsuc, width=2, height=101, bg='#994422').place(x=180, y=310)
            Frame(loginsuc, width=230, height=2, bg='#994422').place(x=63, y=335)
            Frame(loginsuc, width=230, height=2, bg='#994422').place(x=63, y=358)
            Frame(loginsuc, width=230, height=2, bg='#994422').place(x=63, y=378)

        def des1():
            window.deiconify()
            loginsuc.withdraw()

        def loginbutton():
            global loginuser
            loginuser = temp_loginuser.get()
            loginpass = temp_loginpass.get()
            global temp_Depositeamount
            temp_Depositeamount = StringVar()

            if loginpass == "" or loginuser == "":
                notify.config(fg='red', text="All fields required *")

            global stat1
            stat1 = BooleanVar()
            mycursor.execute(f'SELECT * FROM customer where customer_name ="{loginuser}"')
            data = mycursor.fetchall()
            rcount = mycursor.rowcount
            if rcount == 0:
                notify.config(fg='red', text='the account doesnt exist')


            else:
                mycursor.execute(
                    f'SELECT * FROM customer where customer_name ="{loginuser}" and customer_passwd="{loginpass}"')
                data = mycursor.fetchall()
                rcount = mycursor.rowcount
                if rcount > 0:

                    global loginsuc

                    login_screen.destroy()
                    loginsuc = Toplevel(window)
                    loginsuc.columnconfigure(0, weight=1)  # column where the widget is
                    loginsuc.title("Personal Page")
                    loginsuc.geometry("350x500")
                    loginsuc.resizable(0, 0)
                    loginsuc.columnconfigure(0, weight=1)
                    r = 0
                    pos = 0
                    for i in range(100):
                        color = str(211110 + r)
                        Frame(loginsuc, width=10, height=700, bg='#' + color).place(x=pos, y=0)
                        pos += 10
                        r += 1
                    Frame(loginsuc, width=270, height=350, bg='white').place(x=40, y=80)

                    Label(loginsuc, text=f'Welcome Back {loginuser},We hope \n you are doing great',
                          font=('consolas', 14), bg='#211120', fg='white').place(x=60, y=30)
                    Button(loginsuc, text='Show User Details', command=show2, border=0, bg='#994422', fg="white",
                           font=('consolas', 12), width=25).place(x=60, y=110)
                    Button(loginsuc, text='Deposit', command=deposite, border=0, bg='#994422', fg="white",
                           font=('consolas', 12), width=25).place(x=60, y=160)
                    Button(loginsuc, text='WithDraw', command=withdraw, border=0, bg='#994422', fg="white",
                           font=('consolas', 12), width=25).place(x=60, y=210)
                    Button(loginsuc, text='LOGOUT', command=des1, border=0, bg='#994422', fg="white",
                           font=('consolas', 12), width=25).place(x=60, y=260)
                    Frame(loginsuc, width=230, height=2, bg='#994422').place(x=63, y=310)
                    Frame(loginsuc, width=230, height=2, bg='#994422').place(x=63, y=410)
                    Frame(loginsuc, width=2, height=100, bg='#994422').place(x=63, y=310)
                    Frame(loginsuc, width=2, height=102, bg='#994422').place(x=293, y=310)

                    mainloop()


                else:
                    notify.config(fg='red', text="Wrong Password")

        # gui

        global temp_loginuser
        global temp_loginpass

        temp_loginuser = StringVar()
        temp_loginpass = StringVar()

        global login_screen
        login_screen = Toplevel(window)
        login_screen.columnconfigure(0, weight=1)  # column where the widget is
        login_screen.title("Login page")
        login_screen.geometry("350x500")
        login_screen.resizable(0, 0)
        r = 0
        pos = 0
        for i in range(100):
            color = str(211110 + r)
            Frame(login_screen, width=10, height=500, bg='#' + color).place(x=pos, y=0)
            pos += 10
            r += 1
        Frame(login_screen, width=250, height=350, bg='white').place(x=50, y=100)
        # png
        Label(login_screen, image=img1).place(x=140, y=100)

        # Label(login_screen,text="Login",font=('consolas',20),fg='orange').place(x=140,y=150)
        Label(login_screen, text="UserName", bg='white', font=('consolas', 14)).place(x=130, y=200)
        Entry(login_screen, textvariable=temp_loginuser, width=20, border=0, font=1).place(x=80, y=240)
        Frame(login_screen, width=180, height=2, bg='black').place(x=80, y=260)
        # Label(login_screen,).grid(row=3, sticky=N, pady=15)
        Label(login_screen, text="Password", font=('consolas', 14)).place(x=130, y=280)
        Entry(login_screen, textvariable=temp_loginpass, show='*', width=20, border=0, font=1).place(x=80, y=320)
        Frame(login_screen, width=180, height=2, bg='black').place(x=80, y=340)
        Button(login_screen, text='L O G I N', command=loginbutton, fg='white', bg='#994422', border=0).place(x=140,
                                                                                                              y=360)
        Button(login_screen, text='<<', command=back, fg='white', bg='#994422', border=0).place(x=100, y=360)
        notify = Label(login_screen, font=('calibri', 12))
        notify.place(x=110, y=400)
        window.withdraw()
        mainloop()


    # reg
    def register():
        # fun
        def des():
            reg_screen.destroy()

        def finish():
            # var
            name = temp_name.get()
            age = temp_age.get()
            gender = temp_gender.get()
            password = temp_password.get()
            balance = temp_balance1.get()
            y = BooleanVar

            #

            if name == "" or age == "" or password == "":
                notif.config(fg='red', text="All fields required *")
                return

            mycursor.execute(f'SELECT customer_name FROM customer where customer_name ="{name}"')
            data = mycursor.fetchall()
            rcount = mycursor.rowcount
            if rcount > 0:
                notif.config(fg='red', text="account already exist")






            else:

                mycursor.execute(
                    'insert into customer (customer_name,customer_age,customer_balance,customer_passwd) values (%s,%s,%s,%s)',
                    (name, age, balance, password))
                db.commit()
                notif.config(fg="green", text="Account has been created")

        # vars
        global temp_name
        global temp_age
        global temp_gender
        global temp_password
        global notif
        global temp_balance1
        temp_balance1 = StringVar()
        temp_name = StringVar()
        temp_age = StringVar()
        temp_gender = StringVar()
        temp_password = StringVar()

        #
        img2 = Image.open('76.png')
        img2 = img2.resize((95, 95))
        img2 = ImageTk.PhotoImage(img2)

        global reg_screen
        reg_screen = Toplevel(window)
        reg_screen.geometry("350x700")
        reg_screen.resizable(0, 0)
        reg_screen.title("Register Window")

        r = 0
        pos = 0
        for i in range(100):
            color = str(101429 + r)
            Frame(reg_screen, width=10, height=700, bg='#' + color).place(x=pos, y=0)
            pos += 10
            r += 1

        Frame(reg_screen, width=250, height=550, bg='white').place(x=50, y=50)
        Label(reg_screen, image=img2).place(x=120, y=70)
        Label(reg_screen, text="UserName", bg='white', font=('consolas', 14)).place(x=130, y=180)
        Label(reg_screen, text="Age", bg='white', font=('consolas', 14)).place(x=150, y=250)
        Label(reg_screen, text="Balance", bg='white', font=('consolas', 14)).place(x=130, y=330)
        Label(reg_screen, text="Password", bg='white', font=('consolas', 14)).place(x=125, y=390)
        # user Input
        Entry(reg_screen, textvariable=temp_name, width=20, border=0, font=1).place(x=80, y=220)
        Frame(reg_screen, width=180, height=2, bg='black').place(x=80, y=240)
        Entry(reg_screen, textvariable=temp_age, width=20, border=0, font=1).place(x=80, y=290)
        Frame(reg_screen, width=180, height=2, bg='black').place(x=80, y=310)
        Entry(reg_screen, textvariable=temp_balance1, width=20, border=0, font=1).place(x=80, y=355)
        Frame(reg_screen, width=180, height=2, bg='black').place(x=80, y=375)
        Entry(reg_screen, textvariable=temp_password, show='*', width=20, border=0, font=1).place(x=80, y=415)
        Frame(reg_screen, width=180, height=2, bg='black').place(x=80, y=435)

        # SELECT
        Label(reg_screen,
              text='Gender', bg='white', font=('consolas', 14)).place(x=135, y=450)

        Radiobutton(reg_screen,
                    text="Male",
                    font=('consolas', 14),
                    padx=20,
                    variable=temp_gender,
                    value='Male').place(x=70, y=480)

        Radiobutton(reg_screen,
                    text="Female",
                    font=('consolas', 14),
                    padx=20,
                    variable=temp_gender,
                    value='FeMale').place(x=170, y=480)

        def back():
            window.deiconify()
            reg_screen.withdraw()

        Button(reg_screen, text='R E G I S T E R', fg='white', bg='#101429', border=0, font=('consolas', 14),
               command=finish).place(x=110, y=560)
        Button(reg_screen, text='<<', fg='white', bg='#101429', border=0, font=('consolas', 14), command=back).place(
            x=60, y=560)
        # not
        notif = Label(reg_screen, font=('consolas', 10))
        notif.place(x=80, y=510)
        window.withdraw()
        mainloop()


    ###GUI
    global window
    window = Tk()
    window.title('Banking App')
    window.geometry('300x500')
    window.resizable(0, 0)
    r = 0
    pos = 0
    for i in range(100):
        color = str(101420 + r)
        Frame(window, width=10, height=700, bg='#' + color).place(x=pos, y=0)
        pos += 5
        r += 1
    for i in range(9):
        color = str(101429 + r)
        # Frame(window, width=10, height=1, bg='#' + color).place(x=pos, y=0)
        Label(window, text="Islamic Bank", bg='#101445', font=('calibri', 16), fg='white').place(x=88, y=20)
        pos += 10
        r += 1

    ##import img
    img = Image.open('money.jpg')
    window.geometry()
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)

    global img1
    img1 = Image.open('log.PNG')
    img1 = img1.resize((70, 70))
    img1 = ImageTk.PhotoImage(img1)

    Frame(window, height=300, width=250).place(x=27, y=80)

    Label(window, text="Super secured bank", font=('calibri', 10), bg='#101445', fg='white').place(x=90, y=50)
    Label(window, image=img).place(x=100, y=80)
    # buttons
    Button(window, text='REGISTER', fg='white', bg='#101449', border=0, font=('consolas', 14),
           command=register, width=20).place(x=50, y=230)
    Button(window, text='L O G I N', command=login, fg='white', bg='#994422', border=0, font=('consolas', 14),
           width=20).place(x=50, y=290)

    mainloop()

except:
    top = Tk()
    top.geometry("100x100")
    messagebox.askyesno('Cant connect to the server')
    top.mainloop()



