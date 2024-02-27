#This color dictionary is used to set the color for terminal texts.
TEXT_COLOR = {"success" : "\033[92m", "warning" : "\033[93m", "danger" : "\033[91m", "reset" : "\033[0m"}
#Preset products dictionary
products = {"laptop": 899.0, "ipcam": 15.7, "battery": 55.99, "iphone": 13.9}


def menu()-> str: 
    '''
    menu Load Menu User

    Prints out the menu in the console and allows user to choose from given option

    :return: Returns user's selected option from the menu
    :rtype: str
    '''
    # Menu string
    sMenu = f"""Menu : Select a, r, e or q
        {TEXT_COLOR['success']}a. Add a product
        {TEXT_COLOR['danger']}r. Remove a product
        {TEXT_COLOR['warning']}e. Edit Price
        {TEXT_COLOR['reset']}q. Quit
        """

    # Print the menu in console and take user's input as menu selection
    print(sMenu)
    user_intention = input("Please select a option: ")

    #Returning stripped string so that unwanted blank spaces can be ignored for the purpose of usability.
    return user_intention.strip()


def add_product():
    '''
    add_product Add a product

    Allow user to add a new product with product name and product price
    '''
    name = input("Please insert product name: ").strip()
    if name == "":
        print(f"{TEXT_COLOR['danger']}Invalid product name. Please try again.{TEXT_COLOR['reset']}")
        return
        
    # Attempt to add product price. If invalid price value is given, then ValueError exception is handled with a alert msg.
    try:
        price = float(input("Please insert product price: "))
        products.update({name: price})
        print(f"{TEXT_COLOR['success']}{name} was added to database. {TEXT_COLOR['reset']}")
    except ValueError:
        print(f"{TEXT_COLOR['danger']}Invalid price format. Please try again with numeric price format.{TEXT_COLOR['reset']}")
        return
   
    return


def product_not_found(key):
    '''
    product_not_found Product Not Found

    This method is invoked once product is not found by the key.

    :param key: The param is product key in the product dictionary
    :type key: str
    :return: Return error message for not found product
    :rtype: str
    '''
    
    return f"{TEXT_COLOR['danger']}{key} not found.{TEXT_COLOR['reset']}"


def remove_product():
    '''
    remove_product Remove a Product

    Allow a user to remove a product from storage. Once invoked user is asked to provide a product name/key to delete. If the product is found, it will be removed from database.
    '''
    pName = input(f"{TEXT_COLOR['danger']}Please insert product name/key to remove product: {TEXT_COLOR['reset']}")
    
    # Attempt to remove the product from database. If the product is not found invoke product_not_found()
    print(products.pop(pName, product_not_found(pName)))
    return


def edit_price():
    pName = input("Please insert product name to update price: ").strip()

    # If product key is not available in database then print product not found msg and return
    if products.get(pName) is None:
        print(product_not_found(pName))
        return

    # Attempt to edit product price. If invalid price value is given, then ValueError exception is handled with a alert msg.
    try:
        price = float(input(f"{TEXT_COLOR['warning']}Please insert new product price: {TEXT_COLOR['reset']}"))
        products.update({pName: price})
        print(f"{TEXT_COLOR['success']}Price for {pName} was updated to {price}{TEXT_COLOR['reset']}")
    except ValueError:
        print(f"{TEXT_COLOR['danger']}Invalid price format. Please try again with numeric price format.{TEXT_COLOR['reset']}")
        return

    return

def main():
    '''
    main Main Method

    Main method inovokes the menu. 
    It keeps user's selected option from menu to decide the further operation. A while loop is being excecuted until user inputs q. 
    '''
    # Call menu() to print the menu and the returned selected menu option is stored in selected_option
    selected_option = menu()

    while selected_option != "q":
        if selected_option == "a":
            add_product()
            selected_option = menu()
        elif selected_option == "r":
            remove_product()
            selected_option = menu()
        elif selected_option == "e":
            edit_price()
            selected_option = menu()
        else:
            print(f"{TEXT_COLOR['danger']}Please select a valid menu option:  {TEXT_COLOR['reset']}")
            selected_option = menu()
            
    return

# Run the main function
if __name__ == "__main__":
    main()
