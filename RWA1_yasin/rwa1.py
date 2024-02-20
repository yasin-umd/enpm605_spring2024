products = {"laptop": 10.5, "ipcam": 15.7, "battery": 20.99}
text_colour = {"success" : "\033[92m", "warning" : "\033[93m", "danger" : "\033[91m", "reset" : "\033[0m"}

def menu():
    m = f"""Menu : Select a, r, e or q
        {text_colour['success']}a. Add a product
        {text_colour['danger']}r. Remove a product
        {text_colour['warning']}e. Edit Price
        {text_colour['reset']}q. Quit
        """

    print(m)
    user_intention = input("Please select a option: ")

    return user_intention


def add_product():
    name = input("Please insert product name: ")
    try:
        price = float(input("Please insert product price: "))
        products.update({name: price})
    except ValueError:
        print(f"{text_colour['danger']}Invalid price, please try again. {text_colour['reset']}")
        return

    print(f"{text_colour['success']}{name} was added to database. {text_colour['reset']}")

    print(products)
    return


def product_not_found(key):
    print(f"{text_colour['danger']}{key} not found in the database.{text_colour['reset']}")


def remove_product():
    # print("\033[91mRed text\033[0m")

    pName = input(f"{text_colour['danger']}Please insert product name/key to remove product: {text_colour['reset']}")
    products.pop(pName, product_not_found(pName))
    print(products)
    return


def edit_price():
    name = input("Please insert product name to update price: ")

    # If product key is not available in database then void operation and return
    if products.get(name, product_not_found(name)) is None:
        return

    try:
        price = float(input("Please insert new product price: "))
        products.update({name: price})
    except ValueError:
        print(f"{text_colour['danger']}Invalid price format. Please try again. {text_colour['reset']}")
        return

    print(products)
    return


def main():
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
            print(f"{text_colour['danger']}Please select a valid menu option:  {text_colour['reset']}")
            selected_option = menu()

    return


main()
