total=0
expenses={}
while True:
    print("1.add expense\n2.view expence\n3.delete expence\n4.exit")
    choice= int(input("enter a valid number from the above options;"))
    if choice == 1:
        print("enter the expence to be added and the amount")
        exp=input("expence")
        value=float(input("amount"))
        expenses[exp]=value
        total+=value

        print("expence added successfully")
    elif choice == 2:
        for exp,value in expenses.items():
            print("expence:",exp,"amount:",value)
        print("total amount is: ",total)
    elif choice == 3:
        exp=input("enter the expence to be deleted")
        if exp in expenses:
            total-=expenses[exp]
            del expenses[exp]
            print("expence deleted successfully")
        else:
            print("expence not found")
    elif choice == 4:
        break
    else:
        print("invalid choice, please try again")