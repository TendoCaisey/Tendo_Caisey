inventory = {}

while True:
    print("\nInventory Menu:")
    print("1. Add item")
    print("2. View inventory")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        name = input("Item name: ")
        qty = input("Quantity: ")
        inventory[name] = qty
        print(f"{name} added with quantity {qty}.")

    elif choice == '2':
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for item, qty in inventory.items():
                print(f"{item}: {qty}")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
