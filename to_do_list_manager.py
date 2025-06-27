from process import add_task  ,load_task ,remove_task ,mark_task
print(" This is the todo list program, \n Designed by Muhammad Ahmad, \n Thanks for visit my project ")                
def display_menu():
    print(" todo list manager")
    print("1. Add task")
    print("2. Load task")
    print("3. Remove task")
    print("4. Mark task")
while True:
        display_menu()   
        choice = input("Enter your choice  : ")
        if choice == '1':   
            add_task()
        elif choice == '2':
            load_task()
        elif choice == '3':
            remove_task()    
        elif choice == '4':
            mark_task()
            break
        else :
            print("invalid choice. Please enter number from 1 to 4")
        choice = input("Do you want to continue? (Y/N): ")

        if choice.lower()== 'n':
            print("Your program has been stopped")
            break