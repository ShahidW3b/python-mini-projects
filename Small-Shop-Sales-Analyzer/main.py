print("========================================")
print("        SMALL SHOP SALES ANALYZER")
print("========================================")

products = []
prices = []
quantities = []
revenues = []

while True:
    print("\n1. Add sale")
    print("2. Show all sales")
    print("3. Search for a product")
    print("4. Remove a sale")
    print("5. Show revenue summary")
    print("6. Show highest-revenue product")
    print("7. Show lowest-revenue product")
    print("8. Exit")
    print("----------------------------------------")

    choice = input("Choose an option (1 - 8): ")

    if choice == "1":
        print("\n---------- ADD SALE ----------")

        product_name = input("Enter product name: ").title()
        product_price = float(input("Enter product price: $"))
        product_quantity = int(input("Enter quantity sold: "))

        products.append(product_name)
        prices.append(product_price)
        quantities.append(product_quantity)

        product_revenue = product_price * product_quantity
        revenues.append(product_revenue)

        print(f"\n{product_name} sale added successfully.")
        print(f"Revenue: ${product_revenue:.2f}")
        print("----------------------------------------")

    elif choice == "2":
        print("\n---------- ALL SALES ----------")

        if len(products) == 0:
            print("No sales available.")

        else:
            for i in range(len(products)):
                print(f"\nSale {i + 1}")
                print(f"Product:  {products[i]}")
                print(f"Price:    ${prices[i]:.2f}")
                print(f"Quantity: {quantities[i]}")
                print(f"Revenue:  ${revenues[i]:.2f}")
                print("----------------------------------------")

    elif choice == "3":
        print("\n---------- SEARCH PRODUCT ----------")

        search = input("Enter product to search: ").title()

        if search in products:
            index = products.index(search)

            print("\nProduct found.")
            print(f"Product:  {products[index]}")
            print(f"Price:    ${prices[index]:.2f}")
            print(f"Quantity: {quantities[index]}")
            print(f"Revenue:  ${revenues[index]:.2f}")

        else:
            print("Product not found.")

        print("----------------------------------------")

    elif choice == "4":
        print("\n---------- REMOVE SALE ----------")

        remove = input("Enter product to remove: ").title()

        if remove in products:
            index = products.index(remove)

            products.pop(index)
            prices.pop(index)
            quantities.pop(index)
            revenues.pop(index)

            print(f"{remove} was removed successfully.")

        else:
            print("Product not found.")

        print("----------------------------------------")

    elif choice == "5":
        print("\n---------- REVENUE SUMMARY ----------")

        if len(products) == 0:
            print("No sales available.")

        else:
            for i in range(len(products)):
                print(f"{products[i]}: ${revenues[i]:.2f}")

            print("----------------------------------------")
            print(f"Total revenue: ${sum(revenues):.2f}")

    elif choice == "6":
        print("\n---------- HIGHEST-REVENUE PRODUCT ----------")

        if len(revenues) == 0:
            print("No sales available.")

        else:
            highest_revenue = max(revenues)
            index = revenues.index(highest_revenue)

            print(f"Product:  {products[index]}")
            print(f"Price:    ${prices[index]:.2f}")
            print(f"Quantity: {quantities[index]}")
            print(f"Revenue:  ${revenues[index]:.2f}")

        print("----------------------------------------")

    elif choice == "7":
        print("\n---------- LOWEST-REVENUE PRODUCT ----------")

        if len(revenues) == 0:
            print("No sales available.")

        else:
            lowest_revenue = min(revenues)
            index = revenues.index(lowest_revenue)

            print(f"Product:  {products[index]}")
            print(f"Price:    ${prices[index]:.2f}")
            print(f"Quantity: {quantities[index]}")
            print(f"Revenue:  ${revenues[index]:.2f}")

        print("----------------------------------------")

    elif choice == "8":
        print("\n========================================")
        print("Thank you for using Small Shop Sales Analyzer.")
        print("Goodbye!")
        print("========================================")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 8.")
