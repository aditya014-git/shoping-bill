def generate_bill():
    items = []
    total = 0

    print("Welcome to the Shopping Bill Marker\n")
    num_items = int(input("Enter number of items: "))

    for i in range(num_items):
        print(f"\nItem {i + 1}:")
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        item_total = quantity * price
        items.append((name, quantity, price, item_total))
        total += item_total

    print("\n--- Shopping Bill ---")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))
    for item in items:
        print("{:<15} {:<10} {:<10} {:<10}".format(item[0], item[1], item[2], item[3]))

    print("\nGrand Total: ₹{:.2f}".format(total))

    # Fix: Use UTF-8 to avoid UnicodeEncodeError for ₹
    with open("shopping_bill.txt", "w", encoding="utf-8") as f:
        f.write("--- Shopping Bill ---\n")
        f.write("{:<15} {:<10} {:<10} {:<10}\n".format("Item", "Quantity", "Price", "Total"))
        for item in items:
            f.write("{:<15} {:<10} {:<10} {:<10}\n".format(item[0], item[1], item[2], item[3]))
        f.write("\nGrand Total: ₹{:.2f}".format(total))

generate_bill()