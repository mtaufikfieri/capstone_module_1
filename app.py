# Capstone Module 1 - M. Taufik Fieri - Penjualan Barang Toko
products = {
    'nasiputih': {
        'product_name': 'Nasi Putih',
        'category_id': 'Makanan',
        'stock': 100,
        'unit_type': 'Porsi',
        'price': 6000,
    },
    'rendang': {
        'product_name': 'Rendang',
        'category_id': 'Makanan',
        'stock': 75,
        'unit_type': 'Porsi',
        'price': 25000,
    },
    'gulaiayam': {
        'product_name': 'Gulai Ayam',
        'category_id': 'Makanan',
        'stock': 50,
        'unit_type': 'Porsi',
        'price': 99000,
    },
    'aqua': {
        'product_name': 'Teh Hangat',
        'category_id': 'Minuman',
        'stock': 100,
        'unit_type': 'Gelas',
        'price': 6000,
    },
    'tehbotol': {
        'product_name': 'Es Teh',
        'category_id': 'Minuman',
        'stock': 100,
        'unit_type': 'Gelas',
        'price': 10000,
    }
}

cart = []

# Shows All Products
def showProducts():
    # If total products is equal to zero
    if len(products) == 0:
        print("There are no available products")
    else:
        print("|Product Name \t| Category \t| Stock \t| Unit Type \t| Price")
        # Loop through product dictionary keys to show all of the items
        for key in products.keys():
            print("|{} \t| {} \t| {} \t\t| {} \t| {}".format(products[key]["product_name"],products[key]["category_id"],products[key]["stock"],products[key]["unit_type"],products[key]["price"]))
# Shows Specific Product
def showProduct():
    search = input("Enter the product name you wish to be showed: ")
    print("|Product Name \t| Category \t| Unit Type \t| Stock \t| Price")
    # Loop through product dictionary keys looking for the specific keys entered in the input form
    for key in products.keys():
        if search.lower() in products[key]["product_name"].lower():
            print("|{} \t| {} \t| {} \t| {} \t\t| {}".format(products[key]["product_name"],products[key]["category_id"],products[key]["unit_type"],products[key]["stock"],products[key]["price"]))
        else:
            continue
# Add Product Items
def addProduct():
    while True:
        inputName = input("Enter new product name: ")
        newProduct = inputName.replace(" ","")

        # Check if the input is more than 25 characters
        while len(inputName) > 25:
            print("Max 25 characters. Please re-enter value!")
            inputName = input("Enter new product name: ")
            newProduct = inputName.replace(" ","")

        # Check if the new product is not in products dictionary keys
        if newProduct.lower() not in products.keys():
            inputUnitType = input("Enter unit type: ")

            # Check if the input is more than 25 characters
            while len(inputUnitType) > 25:
                print("Max 25 characters. Please re-enter value!")
                inputUnitType = input("Enter new unit type for the product: ")
            
            inputCategory = input("Enter new category for the product: ")

            # Check if the input is more than 25 characters
            while len(inputCategory) > 25:
                print("Max 25 characters. Please re-enter value!")
                inputCategory = input("Enter new category for the product: ")
            
            inputQty = int(input("Enter new stock amount for the product: "))
            inputPrice = int(input("Enter new price for the product: "))

            # Making sure if you really want to add the product that you already inputed
            print("|Product Name \t| Category \t| Stock \t| Unit Type \t| Price")
            print("|{} \t| {} \t| {} \t| {} \t\t| {}".format(inputName,inputCategory,inputUnitType,inputQty,inputPrice))
            checker = input('Are you sure you want to add this product (Y/N): ')

            # If the checker is not equal to Y/y (yes), it will add the new product into the dictionary
            if checker != "Y".lower():
                break
            
            # Add the new product from the new input form into the dictionary
            else:
                products[newProduct.lower()] = {
                    "product_name":inputName.capitalize(),
                    "unit_type":inputUnitType.capitalize(),
                    "category_id":inputCategory.capitalize(),
                    "stock":inputQty,
                    "price":inputPrice
                    }
                showProducts()
                break

        # If the product that you wish to add is already existed
        else:
            print("Product already exist, process cannot be proceeded.")
            break
# Update Product Items
def updateProduct():
    inputProductName = input("Enter product name that will be updated: ")
    updateProduct = inputProductName.replace(" ","")

    while updateProduct.lower() in products.keys():
        print('''
    ##### Update Categories #####

    1. Product Name
    2. Unit Type
    3. Category
    4. Stock
    5. Price
    6. Back To Update Menu
            ''')
        inputOptions = input('Enter an option: ')
        
        # If you chooses to update the product name
        if (inputOptions == '1'):
            new_product = input("Enter new product name: ")
            new_name = new_product.replace(" ","")

            # A while loop to check if the length of the input is more than 25 characters
            while len(new_product) > 25:
                print("Max 25 characters. Please re-enter value!")
                new_product = input("Enter new product name: ")
                new_name = new_product.replace(" ","")
            
            # A while loop to check if the name is already a key in the dictionary
            while new_name.lower() in products.keys():
                print("The name of the product already existed, enter another value!")
                new_product = input("Enter new product name: ")
                new_name = new_product.replace(" ","")

            # Check if you really want to update the specific product or not
            checkerName = input("Are you sure you want to update {} into {}? (Y/N): ".format(inputProductName, new_product))
            if checkerName != "Y".lower():
                break

            # Updating specific value of the product inside the dictionary
            else:
                products[new_name.lower()] = products[updateProduct.lower()]
                del products[updateProduct.lower()]
                products[new_name.lower()]["product_name"] = new_product.capitalize()
                showProducts()
                break
        
        # If you chooses to update the product unit type
        elif (inputOptions == '2'):
            new_unit_type = input("Enter new unit type for the product: ")

            # A while loop to check if the length of the input is more than 25 characters
            while len(new_unit_type) > 25:
               print("Max 25 characters. Please re-enter value!") 
               new_unit_type = input("Enter new unit type for the product: ")

            # Check if you really want to update the specific product or not
            checkerType = input("Are you sure you want to update the unit type for {} into {}? (Y/N): ".format(inputProductName, new_unit_type))
            if checkerType != "Y".lower():
                break
            
            # Updating specific value of the product inside the dictionary
            else:
                products[updateProduct.lower()]["unit_type"] = new_unit_type.capitalize()
                showProducts()
                break
        
        # If you chooses to update the product category
        elif (inputOptions == '3'):
            new_category = input("Enter new category for the product: ")

            # A while loop to check if the length of the input is more than 25 characters
            while len(new_category) > 25:
               print("Max 25 characters. Please re-enter value!") 
               new_category = input("Enter new category for the product: ")

            # Check if you really want to update the specific product or not
            checkerCategory = input("Are you sure you want to update the category for {} into {}? (Y/N): ".format(inputProductName, new_category))
            if checkerCategory != "Y".lower():
                break

            # Updating specific value of the product inside the dictionary
            else:
                products[updateProduct.lower()]["category_id"] = new_category.capitalize()
                showProducts()
                break

        # If you chooses to update the product stocks
        elif (inputOptions == '4'):
            new_stock = int(input("Enter new stock amount for the product: "))

            # Check if you really want to update the specific product or not
            checkerStock = input("Are you sure you want to update the stock of {} into {}? (Y/N): ".format(inputProductName, new_stock))
            if checkerStock != "Y".lower():
                break

            # Updating specific value of the product inside the dictionary
            else:
                products[updateProduct.lower()]["stock"] = new_stock
                showProducts()
                break
        
        # If you chooses to update the product price
        elif (inputOptions == '5'):
            new_price = int(input("Enter new price for the product: "))

            # Check if you really want to update the specific product or not
            checkerPrice = input("Are you sure you want to update the price for {} into {}? (Y/N): ".format(inputProductName, new_price))
            if checkerPrice != "Y".lower():
                break

            # Updating specific value of the product inside the dictionary
            else:
                products[updateProduct.lower()]["price"] = new_price
                showProducts()
                break
        
        # If you chooses to go back into the update menu
        elif(inputOptions == '6'):
            break

        # If you chooses the wrong input number
        else:
            print('Invalid Input')

    # If you enter a product name that is not inside the dictionary
    else:
        print("Item yang anda masukkan tidak ada di list, update tidak bisa dilakukan.")
# Delete Product Items
def delProduct():
    showProducts()
    deleteProduct = input("Enter product name that will be deleted: ")
    # Making sure you really want to delete the product
    checker = input("Are you sure you want to delete the {} product? (Y/N): ".format(deleteProduct))
    while checker != "Y".lower():
        break
    # Delete the desired product from the dictionary
    else:
        nama_delete = deleteProduct.replace(" ","")
        del products[nama_delete.lower()]
        showProducts()
# Transaction Controller
def transaction():
    showProducts()
    while True:
        userInput = input("Enter product name that you want to buy: ")
        buyInput = userInput.replace(" ","")
        # If the name you inputed and already cleared from whitespaces is not in dictionary keys
        if buyInput.lower() not in products.keys():
            print("Product not found")

        # Proceed the transactions
        else:
            product_qty = int(input("Enter amount that you want to buy: "))

            # If the product quantity you inputed is lower than the stock available inside the dictionary key item
            if product_qty > products[buyInput.lower()]["stock"]:
                print("Not enough stock. Product Name: {} Stock left: {}".format(products[buyInput.lower()]["product_name"],products[buyInput.lower()]["stock"]))
            
            # If you inputed the quantity number zero
            elif product_qty <= 0:
                print("Quantity must be higher than 0")
            
            # Add/append the cart with the product details coming from dictionary key, and add new "key" into the list
            else:
                cart.append(
                    [
                        products[buyInput.lower()]["product_name"], 
                        products[buyInput.lower()]["unit_type"], 
                        product_qty, 
                        products[buyInput.lower()]["price"], 
                        products[buyInput.lower()]["product_name"].replace(" ","")
                    ])
            print("Cart Products \n\t")
            print('|Product Name \t| Unit Type \t| Qty \t| Price \t| Total Price')
            
            # Loop through the cart and show the product inside that you already add
            for item in cart:
                print("|{} \t| {} \t| {} \t| {}    \t| {}".format(item[0], item[1], item[2], item [3], item[2] * item[3]))
            
            # Check if you still want to add another product (Y/y) or continue with the transaction (N/n)
            checker=input("Do you want to buy another product? (Y/N): ")
            
            # If checker is equal to Y/y repeat the while loop and add another item into the product list
            if checker.upper() != "Y":
                break
    
    # While cart product length is equal to zero break from the loop
    while len(cart) == 0:
        break

    print('Cart Products: ')
    print('Product Name  \t| Quantity | Product Price\t| Total Price')
    
    # Total price variable
    totalPrice = 0
    
    # Loop through product inside the cart to find the value for the total price, and also shows the cart details
    for item in cart:
        print('{} \t| {}\t   | {}\t\t| {}'.format(item[0], item[2], item[3], item[2] * item[3]))
        totalPrice += item[2] * item[3]
    while True:
        print('Total must be paid = {}'.format(totalPrice))
        inputMoney = int(input('Enter amount of money : '))
        
        # If the money is bigger than the total price
        if inputMoney > totalPrice:
            change = inputMoney - totalPrice
            print('Thank you for visiting our restaurant \n\nYour change : {}'.format(change))
            
            # Loop through cart item and subtract the specific product (stock) from product dictionary with the cart item quantity
            for item in cart :
                products[item[4].lower()]["stock"] -= item[2]
            
            # Clear the cart products (list) and break from the transaction
            cart.clear()
            break
        
        # If the money is equal to the total price
        elif inputMoney == totalPrice:
            print('Thank you for visiting our restaurant')
            
            # Loop through cart item and subtract the specific product (stock) from product dictionary with the cart item quantity
            for item in cart :
                products[(item[4].lower())]["stock"] -= item[2]
            
            # Clear the cart products (list) and break from the transaction
            cart.clear()
            break
        
        # If The money is lower than the total price
        elif inputMoney < totalPrice :
            deficiency = totalPrice - inputMoney
            print('The shortage of money is: {}'.format(deficiency))
        else:
            print('Please enter the correct input')

#################################

while True:
    print('''
    ##### Welcome To Our Restaurant #####

    1. Customer
    2. Admin
    3. Exit Program
    ''')
    userAuth = input('Enter an options: ')
    
    # Customer
    if(userAuth == '1'):
        while True:
            print('''
    ##### Welcome Customer ######

    1. Show List of Products
    2. Transaction
    3. Back To Main Menu
            ''')
            user_input = input('Enter an option: ')

            # Read Products Menu
            if(user_input == '1'):
                while True:
                    print('''
    ##### Welcome Customer ######

    1. Show List of Products
    2. Search Product
    3. Back To Customer Menu
                    ''')
                    user_input = input('Enter an option: ')

                    # Read All Products
                    if(user_input == '1'):
                        showProducts()

                    # Read Specific Product
                    elif(user_input == '2'):
                        showProduct()

                    # Back To Customer Menu
                    elif(user_input == '3'):
                        break
                    # Invalid Input
                    else:
                        print('Invalid Input')
            # Transaction
            elif(user_input == '2'):
                transaction()
            elif(user_input == '3'):
                break
            else:
                print('Invalid Input')
    
    # Admin
    elif(userAuth == '2'):
        while True:
            print('''
    ##### Welcome Admin ######

    1. Show List of Products
    2. Add Product
    3. Update Product
    4. Back To Main Menu
            ''')
            user_input = input('Enter an option: ')
            
            # Read Function
            if(user_input == '1'):
                while True:
                    print('''
    ##### Welcome Customer ######

    1. Show List of Products
    2. Search Product
    3. Back To Admin Menu
                    ''')
                    user_input = input('Enter an option: ')
                    
                    # Read All Products
                    if(user_input == '1'):
                        showProducts()
                    
                    # Read Specific Product
                    elif(user_input == '2'):
                        showProduct()
                    
                    # Exit To Admin Menu
                    elif(user_input == '3'):
                        break
                    # Invalid Input
                    else:
                        print('Invalid Input')
            
            # Create Function
            elif(user_input == '2'):
                addProduct()
            
            # Update & Delete Function
            elif(user_input == '3'):
                print('''
    ##### Update Products #####

    1. Update product
    2. Delete product
    3. Back To Admin Menu
                ''')
                update_input = input('Enter an option: ')
                
                # Update Products
                if(update_input == '1'):
                    updateProduct()
                
                # Delete Products
                elif(update_input == '2'):
                    delProduct()
                
                # Return To Admin Menu
                elif(update_input == '3'):
                    break
                # Invalid Input
                else:
                    print('Invalid Input')
            # Back To Main Menu
            elif(user_input == '4'):
                break
            # Invalid Input
            else:
                print('Invalid Input')

    # Exit The Program
    elif(userAuth == '3'):
        break
    
    # Invalid Input
    else:
        print('Invalid Input')
    

print('Thank You For Visiting!')