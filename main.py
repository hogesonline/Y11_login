
#Step 1
username = "username"
password = "password"
entered_uname = #get input
entered_pwd = #get input
if <condition to check username> and <condition to check password>:
  #display appropriate message
else:
  #display appropriate message

#Step 2 - do the same thing with a function
'''
username = "username"
password = "password"

def <function name>():
  #username and password defined in main program
  global username, password
  entered_uname = #get input
  entered_pwd = #get input
  if <condition to check username> and <condition to check password>:
    #display appropriate message
  else:
    #display appropriate message

#call the function
login()
'''

#Step 2A
'''
username = "username"
password = "password"


def <function name>(<name of first variable>, <name of second variable>):
  #username and password defined in main program
  global username, password
  if <condition to check username> and <condition to check password>:
    #return appropriate message
  else:
    #return appropriate message


#a = input("What is your username? ")
#b = input("What is your password? ")
#get input and call the function
print(login("password", "username"))
'''