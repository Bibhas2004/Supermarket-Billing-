while True:
    name=input("Enter the customer name: ")
    total=0

    while True:
        print("Enter amount & quantity: ")
        amount=float(input("Enter the amount: "))
        quantity=float(input("Enter the quantity: "))
        total+=amount*quantity
        repeat=input("Do you add more items?(yes/no): ")
        if repeat=="no" or repeat=="No":
            break
    
    print("-"*40)
    print("Name: ",name)
    print("Total amount to be paid: ",total)
    print("-"*70)
    print("*****HAPPY SHOPPING*****")

    repeat1=input("Do you want to go next customer?(yes/no): ")
    if repeat1=="no" or repeat1=="No":
        break
