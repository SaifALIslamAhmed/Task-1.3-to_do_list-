# For M.I.A electrical trainer a5oya y3m <3
import datetime 
date =datetime.datetime.now()
print(f"*******************{date}*******************")
try:
    tasklist=[]
    readfile=open("TODOlist.txt","r")
    line= readfile.readline()
    while line:
        tasklist.append(line.rstrip("\n"))
        line = readfile.readline()
    readfile.close()
except  FileNotFoundError :
    print("the to-do list file not found"); print("Starting a new to-do list!")
    tasklist = []

choice = 0
while choice != 5:
    print("LIGHTNING MCQUEEN'S TO-DO LIST"); print("Gotta get ready for the big race! Here's what's on deck:")
    print("1.Add a new task")
    print("2.View my to-do list")
    print("3.Mark a task as completed")
    print("4.Remove a task from the to-do list")    
    print("5.Exit the program")
    print("_______________")

    choice = int(input("What's the move, champ?"))

    if choice == 1:
        newtask=input("you got a workout, champ!....What's the task, champ? ------>")
        tasklist.append(newtask)
        
    elif choice == 2:
        print(f"Displaying your to-di list: {tasklist}")
       # for i in range(len(tasklist)):
        #    print(tasklist[i])

    elif choice == 3:

        donetask = int(input("What have you done....?"))
        #taskcompleted.append(donetask)
        tasklist[donetask] = tasklist[donetask] +" - Completed"
    elif choice == 4:
        removedtask= int(input("Enter The Index of the removedtask...:"))
        tasklist.pop(removedtask)
        print(f"task indexed {removedtask} had been removed succefully....")
    elif choice == 5:
        print("Quitting Program...  ")
        #break
    savedfile = open("TODOlist.txt","w")
    for task in tasklist:
        savedfile.write(task +"\n" )
    savedfile.close()