def addTodo() : 
    try :
        taskInp = input("Enter a value: ")
        tasks.append(taskInp)
        print("Task added successfully")
        print(f"Updated List => {tasks}")
    except ValueError :
        print("Please Enter Number , not string")


def deleteTask() : 
    try :
        indexInp = int(input(f"Enter a number from 1 to {len(tasks)} : " )) - 1
        if indexInp >= 0 and indexInp <= len(tasks)  :
            try :
                tasks.pop(indexInp)
                print("Task Deleted successfully")
                print(f"Updated List => {tasks}")
            except IndexError:
                print("Incorrect Index")
        else : 
            print("Please Correct Index")
    except ValueError:
        print("Please Enter Number , not string")

        
def updateTask() : 
    try :
        indexInp = int(input(f"Enter a number from 1 to {len(tasks)} : " )) - 1
        if indexInp >= 0 and indexInp <= len(tasks)  :
            try :
                updateTask = input(f"Enter new task to update {tasks[indexInp]} : ")
                tasks[indexInp] = updateTask
                print("Task Updated successfully")
                print(f"Updated List => {tasks}")
            except IndexError :
                print("Incorrect Index")

        else : 
            print("Please Correct Index")
    except ValueError:
        print("Please Enter Number , not string")        
        
def loadTaskFromFile() :
    try :
        with open("tasks.txt", "r+") as f :
            tasks = [line.strip() for line in f.readlines()]
        
        return tasks
    except FileNotFoundError :
        return []

def saveToFile() :
    try :
        with open("tasks.txt", "w") as f:
            for task in tasks :
                f.write(task + "\n")
        
        print("saved task to file successfully")
    except :
        print("Can't Saved")
    
    
    
tasks = loadTaskFromFile()    
print(tasks)

while True :
    try : 
        action = int(input("1-AddTask \n2-RemoveTask \n3-UpdateTask \n0-End Exit \n>>"))
        if action == 1 :
            addTodo()
        elif action == 2 :
            deleteTask()   
        elif action == 3 :
            updateTask()
        elif action == 0 :
            print("Task Exit")
            break
        else :
            print("Please Correct Number")
            action = int(input("1- AddTask \n 2-RemoveTask \n 3-UpdateTask \n"))
        saveToFile()
    except ValueError:
        print("Please Enter Number , not string")

        




