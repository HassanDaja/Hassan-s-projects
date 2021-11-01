
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            website, user, psw = data.split("|")
            print("website:",website, "user:",user, "| password:",psw)
def add():
    website=input("the website name:")
    user=input("input the user:")
    passowrd1=input("input the password for the acc:")
    with open("password.txt",'a') as f:
        f.write(website+"|"+user+"|"+ passowrd1+"\n")



while True:
    mode = input("enter the mode that u want?(view,add,quit)")
    if mode=="view":
        view()
    elif mode=="add":
        add()
    elif mode=="quit":
        break
    else:
        print("enter valid input please:")
        continue