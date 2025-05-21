
# Simple Inventory Management System

# Sample inventory with item names as keys and quantity as values
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}

def display_inventory():
    print("\n--- Current Inventory ---")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_inventory():
    item = input("Enter item name: ").lower()
    qty = int(input("Enter quantity to add/remove (use negative number to remove): "))

    if item in inventory:
        inventory[item] += qty
    else:
        inventory[item] = qty

    # Prevent negative quantities
    if inventory[item] < 0:
        inventory[item] = 0

    print(f"{item} updated. New quantity: {inventory[item]}")

def main():
    while True:
        print("\n1. Display Inventory")
        print("2. Update Inventory")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            display_inventory()
        elif choice == '2':
            update_inventory()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

main()
