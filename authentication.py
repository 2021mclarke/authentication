##Get User input, name and password

## Check to see if name and password match my record

#If so ill print a msecret message
#If not print a hint

name = input("Username")
password = input("Password")

if name == "John Doe":
    print("Welcome to the Matrix.")
if password == "Matrix":
    print("you passed");
else:
    print("Incorrect")