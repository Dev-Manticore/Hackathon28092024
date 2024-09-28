from server import *

print(server.userNames)

while True:
    username = input("username\n")
    password = input("password\n")

    index = login(username, password)

    if index:
        break
    else:
        print("invalid Login")
    


#only lose hp on urgent tasks
#lose happiness on others

fileName = "C:/code/hackathon/Characters/" + "username.txt"

characterFile = open(fileName, "w+")    