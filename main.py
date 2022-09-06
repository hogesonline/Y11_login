'''
Step 1
username = "username"
password = "password"
entered_uname = input("What is your username? ")
entered_pwd = input("What is your password? ")
if username == entered_uname and password == entered_pwd:
  print("You are verified!")
else:
  print("Try again")
'''
#Step 2 - do the same thing with a function
'''
username = "username"
password = "password"

def login():
  #username and password defined in main program
  global username, password
  entered_uname = input("What is your username? ")
  entered_pwd = input("What is your password? ")
  if username == entered_uname and password == entered_pwd:
    print("You are verified!")
  else:
    print("Try again")

login()
'''

#Step 2A

username = "username"
password = "password"


def login(entered_uname, entered_pwd):
    #username and password defined in main program
    global username, password
    if username == entered_uname and password == entered_pwd:
        return True
    else:
        return False


#a = input("What is your username? ")
#b = input("What is your password? ")
print(login("password", "username"))
