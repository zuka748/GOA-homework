tasks = []
def show_tasks():
    if not tasks:  
        print(" დავალებები ჯერ არ არის.")
    else:
        print("\n შენი დავალებები:")
        for i, task in enumerate(tasks):  
            print(f"{i + 1}. {task}")  
def add_tasks():
    input_text = input("ჩაწერე რამდენიმე დავალება (გამოყავი მძიმით): ")
    new_tasks = [task.strip() for task in input_text.split(",") if task.strip()]
    
    if new_tasks: 
        tasks.extend(new_tasks) 
        print(f" {len(new_tasks)} დავალება დაემატა.") 
    else:
        print(" არაფერი დაგმატებულა.")  
def delete_task():
    show_tasks()  
    try:
        index = int(input(" რომელი წავშალოთ? (ნომერი): ")) - 1  
        if 0 <= index < len(tasks):  
            removed = tasks.pop(index)  
            print(f" '{removed}' წაიშალა.")  
        else:
            print(" არასწორი ოპრაცია.") 
    except ValueError:
        print(" გთხოვ შეიყვანე რიცხვი.")
while True:
    print("\n მენიუ:")
    print("1. დავალებების ნახვა")
    print("2. დავალების დამატება")
    print("3. დავალების წაშლა")
    print("0. გამოსვლა")

   
    choice = input(" აირჩიე ოპცია: ")

   
    if choice == "1":
        show_tasks() 
    elif choice == "2":
        add_tasks()  
    elif choice == "3":
        delete_task()  
    elif choice == "0":
        print(" ნახვამდის!")  
        break
    else:
        print(" არასწორი ოპერაციაა აირჩიე ნაჩვენები ოპერაციიდან.")

