# 7th  wa menu driven python program wherew the user can add items, remove items, view cart and exit 


cart = []

while True:
    print("\n1.Add  2.Remove  3.View  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        cart.append(input("Enter item: "))
    elif ch == 2:
        cart.remove(input("Enter item: "))
    elif ch == 3:
        print("Cart:", cart)
    elif ch == 4:
        break
    else:
        print("Invalid choice")

