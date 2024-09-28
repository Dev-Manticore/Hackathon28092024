# getting log in files
loginsFile = open("Logins.txt", "r+")
placeholder = loginsFile.read().split("\n")
logins = []
for line in placeholder:
    logins.append(line.split(","))
userNames = []
for line in logins:
    userNames.append(line[0])
#log in
def login(username, password):
    if username in userNames:
        index = userNames.index(username)
        if password == logins[index][1]:
            return index
        else:
            return None
    else:
        return None
#add user
def addUser(username, password):
    if "\n" in username or "\n" in password or "," in username or "," in password:
        print("invalid characters used")
    elif username in userNames:
        print("username taken")
    else:
        loginsFile.write("\n"+username+","+password)
#print(logins)
index = 0
'''
#user log in
while True:
    username = input("username\n")
    password = input("password\n")

    index = login(username, password)

    if index or index == 0:
        break
    else:
        print("invalid Login")
'''

'''
-------------------------------------
now logged on
'''


from datetime import datetime
#datetimeobject stores (Yr, M, D, H, M, S)

now = datetime.now()
current_time = now.strftime("%Y %b %d  %H:%M:%S")
print("Current Time =", current_time)

def Addtask(name, doneBy, urgency):
    tasks.append(name, doneBy, urgency)
    #time stored in epoch time
    #urgency levels: Low, Medium, High


def checkTasks(task):
    
    if epochTime > task[1]:
        #task fail
        if task[2] == "Low":
            character[3] -= 1
        elif task[2] == "Medium":
            character[3] -= 2
        elif task[2] == "High":
            character[1] -= 1
        
        if character[3] < 0:
            character[1] -= 1



def completeTask(task):
    taskNames.remove(task[0])
    tasks.remove(task)

# creates/ opens file for users creature
fileName = "users/" + "username.txt"
characterFile = open(fileName, "w+")

character = characterFile.read().split("\n")

#file goes creature, current health, max health, happiness
#then tasks etc

#initialises character
if character == [""]:
    character = ["1,5,5,5", []]
    tasks = []
else:
    tasks = character[1]

taskNames = []
for task in tasks:
    epochTime = datetime.now().timestamp()
    taskNames.append(task[0])

for task in tasks:
    checkTasks(task)


#only lose hp on urgent tasks
#lose happiness on others

#timestamp method