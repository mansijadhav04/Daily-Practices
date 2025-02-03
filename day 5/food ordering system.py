# Online Food Ordering System

def display_menu(menu):
    print("\nMenu:")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item_id, item_info in items.items():
            print(f"{item_id}. {item_info['name']} - ₹{item_info['price']}")

def add_to_cart(menu, cart):
    item_id = input("Enter the item number to add to your cart: ")
    for category in menu.values():
        if item_id in category:
            quantity = int(input("Enter the quantity: "))
            if item_id in cart:
                cart[item_id]['quantity'] += quantity
            else:
                cart[item_id] = {'name': category[item_id]['name'], 'price': category[item_id]['price'], 'quantity': quantity}
            print(f"{category[item_id]['name']} added to your cart.")
            return
    print("Invalid item number.")

def view_cart(cart):
    print("\nYour Cart:")
    if not cart:
        print("Your cart is empty.")
    else:
        total = 0
        for item in cart.values():
            item_total = item['price'] * item['quantity']
            total += item_total
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item_total}")
        print(f"Total: ₹{total}")

def place_order(cart):
    if not cart:
        print("Your cart is empty. Add items to place an order.")
    else:
        print("\nOrder placed successfully! Here are your order details:")
        view_cart(cart)
        print("\nFinal Bill:")
        total = 0
        for item in cart.values():
            item_total = item['price'] * item['quantity']
            total += item_total
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item_total}")
        print(f"Grand Total: ₹{total}")
        cart.clear()
        print("Thank you for ordering! Your cart is now empty.")

def main():
    menu = {
        'Starters': {
            '1': {'name': 'Soup', 'price': 149},
            '2': {'name': 'Garlic Bread', 'price': 99}
        },
        'Main Course': {
            '3': {'name': 'Pizza', 'price': 499},
            '4': {'name': 'Burger', 'price': 249},
            '5': {'name': 'Pasta', 'price': 299}
        },
        'Dessert': {
            '6': {'name': 'Ice Cream', 'price': 199},
            '7': {'name': 'Brownie', 'price': 249}
        }
    }
    cart = {}

    while True:
        print("\n--- Online Food Ordering System ---")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            add_to_cart(menu, cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            place_order(cart)
        elif choice == '5':
            print("Thank you for using the Online Food Ordering System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
