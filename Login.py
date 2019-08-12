status=""
createname=""
createpassword=""
name=""
password=""
def displaymenu():
    status=input("already have an account ?Y/N ?Press Q to quit")
    if status=="Y":
        olduser()
    elif status=="N":
        newuser()

def newuser():
    createname=input("enter your name")
    createpassword=input("enter password")
    if createname in users:
        print("name already exists...enter other username")
        createname=input("enter other username")
    users[createname]=createpassword
    print("registered successfully\n")


def olduser():
    name=input("enter username")
    password=input("enter password")
    if name in users and users[name]==password:
        print("login successful")
    
while status!='Q':
    displaymenu()
