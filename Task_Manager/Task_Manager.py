def Task_Manager():
    Task_List = []
    print("---------WELCOME TO THE TASK MANAGER---------")

    # Task_Len = int(input("Fill The Number Of Tasks You Want to Add\n")) Error if no integer
    while True:
        try:
            Task_Len = int(input("Fill The Number Of Tasks You Want to Add\n"))
            break
        except ValueError:
            print("Please enter a valid integer")

    for Task in range(1,Task_Len+1):
        Task_Name= input(f"Enter Your Task Number {Task} Here\t")
        Task_List.append(Task_Name)
    print("Task Added To The List")

    while True:
        Operation = str(input(f"Click A to Add Task\nClick R to Replace Task\nClick D to Delete\nClick V to Add View\nClick E to End Task\n"))
        if Operation == "A" or Operation == "a" :
            New_Task = input("Enter The New Task\n")
            if New_Task in Task_List:
                print("Task Already Exist")
            elif New_Task not in Task_List:
                Task_List.append(New_Task)
                print(f"The Task {New_Task} Has Been Added To The List")

        elif Operation == "R" or Operation == "r" :
            Task_Replace= input("Register The Task You Want To Replace\n")
            if Task_Replace in Task_List:
                Task_Replaced = input("Register New Task\n")
                Task_Replace_Index = Task_List.index(Task_Replace)
                Task_List[Task_Replace_Index] = Task_Replaced
                print(f"Task {Task_Replace} Got Replaced by {Task_Replaced} At {Task_Replace_Index}")

            elif Task_Replace not in Task_List:
                print(f"No Such Task Called : {Task_Replace} Found")
            
        elif Operation == "D" or Operation == "d" :
            Task_Delete=input("Enter The Task To Delete\n")
            if Task_Delete in Task_List:
                Deleted_Index = Task_List.index(Task_Delete)
                del Task_List[Deleted_Index]
                # Task_List.pop(Deleted_Index)
                print(f"Task Deleted : {Task_Delete}")
            elif Task_Delete not in Task_List:
                print("No Such Task Is Assigned")
        elif Operation == "V" or Operation == "v" :
            print("The Tasks Are")
            for task in Task_List:
                print(task)
        elif Operation == "E" or Operation == "e" :
            print("Closing.....")
            break
        else:
            print("Invalid Input")



Task_Manager()