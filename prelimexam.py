def get_price_category(price):
    if price < 50:
        return 'Budget'
    elif 50 <= price < 199:
        return 'Mid-range'
    else:
        return 'Premium'
    
def stock_level(stock):
    if stock < 10:
        return 'Low Stock'
    else:
        return 'Stock OK'

def save_product_record(product_name, price, stock, price_category, stock_status):
    with open('D:\\edp_f01100110\\inventory.txt', 'a') as file:
        file.write(f"Product: {product_name} | Price: p {price:.2F} | Stock: {stock} | Price Category: {price_category} | Stock Status: {stock_status}\n")

while True:
    product_name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the stock quantity: "))
    
    price_category = get_price_category(price)
    stock_status = stock_level(stock)
    print(f"Price Category: {price_category}")
    print(f"Stock Status: {stock_status}")
    print("Product saved successfully!") 

    save_product_record(product_name, price, stock, price_category, stock_status)

    choice = input("Do you want to add another product? (yes/no): ").lower()
    if choice != "yes":
        print("Product records saved. Exiting the program.")
        break