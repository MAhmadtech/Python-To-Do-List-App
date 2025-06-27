
from datetime import datetime
import os
import json

def add_task():
    tasks=[]   
    task_name = input("What is your task name :")
    description = input("What is your task description :")
    date1 = str(datetime.now().date())
    status = False
    tasks.append({ "task_name" : task_name ,"description" : description ,  "date1" : date1 , "complete" : status })
    print("Task description added successfully")   
    print(tasks)  
    name = "C:\\Users\\Silicon computers\\Desktop\\code\\Todo List project\\Database\\" + task_name + ".json"
    with open(name, 'w') as file:
        json.dump(tasks ,file)
        print("File content added")





def load_task():
    directory_path = "C:\\Users\\Silicon computers\\Desktop\\code\\Todo List project\\Database"
    all_files = os.listdir(directory_path)
    file_names = [f for f in all_files if os.path.isfile(os.path.join(directory_path,f))]
    
    index = 1
    tasks = {}
    for i in file_names:
        file_names = i[:-4]
        print(index,file_names)
        tasks[file_names]= os.path.join(directory_path, i)
        index = index + 1 
    open_file = input("Which task you want to open: ")
    if open_file in tasks:
        task_path = tasks[open_file]
        with open(task_path, 'r') as file:
            content = file.read()
            print(f"Content of {open_file}.json:\n{content}")
    else:
        print("Task not found.") 





def remove_task():
    directory_path = "C:\\Users\\Silicon computers\\Desktop\\code\\Todo List project\\Database"
    all_files = os.listdir(directory_path)
    file_names = [f for f in all_files if os.path.isfile(os.path.join(directory_path,f))]
    index = 1
    tasks = {}
    for i in file_names:
        file_names = i[:-4]
        print(index,file_names)
        tasks[file_names]= os.path.join(directory_path, i)
        index = index + 1    
    close_file = input("Which task you want to remove : ")
    if  close_file in tasks:
        task_path = tasks[close_file]
        if os.path.exists(task_path):
            os.remove(task_path)
            print("Your task has been removed successfully")
        else:
            print(f"Task path does not exist: {task_path}")               
    else:
        print(f"Task '{close_file}' not found")   

def update():

    tasks = []
    update = []
    directory_path = "C:\\Users\\Silicon computers\\Desktop\\code\\Todo List project\\Database\\"
 
    for filename in os.listdir(directory_path):
        tasks.append(filename)
    # print(tasks)
    for i in tasks:
        directory_path = "C:\\Users\\Silicon computers\\Desktop\\code\\Todo List project\\Database\\"+ i 
        with open (directory_path , 'r') as file:
            tasks = json.load(file)
            if tasks[0]["complete"] == False:
                update.append(i)
    return update                            






def mark_task():
    index = 1
    for i in update():       
        file_names = i[:-4]
        print(index,file_names)
        index = index + 1        
    upper_file = input("Which task you want to be completed : ")
    directory_path = "C:\\Users\\Silicon computers\\Desktop\\code\\Todo List project\\Database\\" + upper_file + ".json"
    with open(directory_path, 'r+') as file:       
            tasks = json.load(file) 
            tasks[0]["complete"] = True
            file.seek(0)
            json.dump(tasks ,file)
            file.truncate()
            print("Your task has been marked as completed, ")