def calculate_discount(product_code, order_amount):
    # Initialize discount to 0
    discount = 0
    
    # Check for the type of toy and calculate discount
    
    # Battery-based toys
    if product_code == 1:  
        if order_amount > 1000:
            discount = 0.10 * order_amount
            
    # Key-based toys
    elif product_code == 2:  
        if order_amount > 100:
            discount = 0.05 * order_amount
            
    # Electrical charging based toys
    elif product_code == 3:  
        if order_amount > 500:
            discount = 0.10 * order_amount
    else:
        print("Invalid product code!")
        
        # Exit the function for invalid product code
        return None  
    
    # Calculate the net amount after discount
    net_amount = order_amount - discount
    return net_amount

# Input from the user
product_code = int(input("Enter the product code (1 for Battery-based, 2 for Key-based, 3 for Electrical charging based): "))
order_amount = float(input("Enter the order amount: "))

# Calculate the net amount
net_amount = calculate_discount(product_code, order_amount)

# Display the result if the product code is valid
if net_amount is not None:
    print(f"The net amount to be paid is: Rs. {net_amount:.2f}")
