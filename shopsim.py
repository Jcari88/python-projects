import random

#dictionary to store the inventory of the shop
inventory = {
    "apple": {"quantity": 10, "price": 0.5},
    "banana": {"quantity": 5, "price": 0.3},
    "orange": {"quantity": 7, "price": 0.4}
}

#function to simulate customer purchase
def customer_purchase(item,quantity):
    if item in inventory:
        if inventory[item]["quantity"]>=quantity:
            inventory[item]["quantity"]-=quantity
            total_sale=inventory[item]["quantity"]*inventory[item]["price"]
            return "Purchase successful, Sale Total: $"+ str(total_sale) +"\nremaining stock of "+item+ " is "+str(inventory[item]["quantity"])
        else:
            return "Purchase failed, Not enough stock of "+item
    else:
        return "Item not found."
    
#function to check the stock of a particular item
def check_stock(item):
    if item in inventory:
        return inventory[item]["quantity"]
    else:
        return "Item not found."

#function to update the stock of a particular item
def update_stock(item, quantity):
    if item in inventory:
        inventory[item]["quantity"] = quantity
        return inventory
    else:
        return "Item not found."

#function to add new items to inventory
def add_item(item,quantity,price):
    inventory[item]={'quantity':quantity,'price':price}
    return "item added successfully"

#function to remove items from inventory
def remove_item(item):
    if item in inventory:
        del inventory[item]
        return "item removed successfully"
    else:
        return "Item not found."

#function to calculate total inventory value
def inventory_value():
    total_value=0
    for item, detail in inventory.items():
        total_value+= detail["quantity"]*detail["price"]
    return total_value

#function to display the inventory of the shop
def display_inventory():
    for item, detail in inventory.items():
        print(item, ":", detail["quantity"]," at price: ",detail["price"])
        
#main menu loop
while True:
    print(" Welcome to the shop simulator!")
    print("--------------------------------")
    print("1. Check stock of an item")
    print("2. Update stock of an item")
    print("3. Add a new item")
    print("4. Remove an item")
    print("5. Display inventory")
    print("6. Calculate total inventory value")
    print("7. Simulate random customer purchase")
    print("8. Simulate manual customer purchase")
    print("9. Exit")
    choice = input("Enter your choice (1-9): ")
    if choice == "1":
        item = input("Enter the item name: ")
        print("Stock:", check_stock(item))
        print("\n")
        
    elif choice == "2":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        print(update_stock(item, quantity))
        print("\n")
    
    elif choice == "3":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price of item:"))
        print(add_item(item,quantity,price))
        print("\n")
        
    elif choice == "4":
        item = input("Enter the item name: ")
        print(remove_item(item))
        print("\n")
        
    elif choice == "5":
        display_inventory()
        print("\n")
        
    elif choice == "6":
        print("Total inventory value is:", inventory_value())
        print("\n")
        
    elif choice == "7":
        item = random.sample(inventory.keys(),1)[0]
        quantity = random.randint(1,20)
        print("Customer wants: " + str(quantity) + " " + str(item)  + "\n"+ customer_purchase(item,quantity))
        print("\n")
    elif choice == "8":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        print("Customer wants: " + str(quantity) + " " + str(item)  + "\n"+ customer_purchase(item,quantity))
        print("\n")
    elif choice == "9":
        break
