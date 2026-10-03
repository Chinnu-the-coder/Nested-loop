while True:
    total=0
    name=input("Name of customer: ")
    while True:
        print("Enter cost of items and quantity:")
        amount=float(input("Item cost: "))
        qty=int(input("Quantity: "))
        total=total+(amount*qty)
        repeat=input("Do you want to add more items (y/n)? ").lower()
        if repeat=="n":
            break
    print("="*30)
    print(f"Name: {name}")
    print(f"Total bill amount: {total}")
    print()
    print("**********Happy Shopping**********")
    print("="*30)
    morePeople=input("Go to next person(y/n): ").lower()
    if morePeople=="n":
        break