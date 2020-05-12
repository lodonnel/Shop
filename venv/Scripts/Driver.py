from FileHandling import *
from Input import menu_option
from Menu import Menu
from Shopping_Cart import ShoppingCart
from manage_items import ManageItems

mi = ManageItems()
sc = ShoppingCart()

# file constants
DRINK = "../Data/Drink.csv"
FOOD = "../Data/Food.csv"
SHOPPING_CART = "../Data/ShoppingCart.csv"
TRANSACTIONS = "../Data/Transactions.csv"


def main():
    main_menu = Menu("main")
    staff = Menu("staff")
    customer = Menu("customer")

    load_data()

    option = 0
    import sys
    while option < main_menu.maximum:
        print("main menu")
        print('\n'.join(main_menu.menu))
        option = menu_option(main_menu)

        if option is not None:
            if option == 1:
                print("staff menu")
                staff_menu(staff)
            elif option == 2:
                print("customer menu")
                customer_menu(customer)
            else:
                save_data()
                sys.exit()
        else:
            save_data()
            sys.exit()


# --------------------------------------------------------------------------
# menus and menu methods start here

def load_data():
    mi.add_all(rw_file(DRINK), "drink")
    mi.add_all(rw_file(FOOD), "food")
    # sc.add_all(rw_file(TRANSACTIONS), "transactions")
    # mi.add_all(rw_file(SHOPPING_CART), "ShoppingCart")


def save_data():
    rw_file(DRINK, mi.list_items("drink"))
    rw_file(FOOD, mi.list_items("food"))
    # rw_file(SHOPPING_CART, sc.cart_items.to_csv())


def staff_menu(staff):
    option = 0
    while option < staff.maximum:
        # show menu
        # accept input
        print(staff.menu)
        print('\n'.join(staff.menu))
        option = menu_option(staff)
        if option is not None:
            if option == 1:
                add_food()
            elif option == 2:
                add_drink()
            elif option == 3:
                list_food()
            elif option == 4:
                list_drink()
            elif option == 5:
                add_stock()
        else:
            option = staff.maximum  # ie exit


def customer_menu(customer):
    option = 0
    manage_cart = Menu("manage cart")
    while option < customer.maximum:
        print(customer)
        print('\n'.join(customer.menu))
        option = menu_option(customer)
        if option is not None:
            if option == 1:
                customer1()
            elif option == 2:
                customer2()
            elif option == 3:
                manage_cart_menu(manage_cart)
            elif option == 4:
                customer4()
            elif option == 5:
                customer5()
            elif option == 6:
                manage_cart_menu(manage_cart)
        else:
            option = customer.maximum  # ie exit


def add_food():
    print("staff1")
    mi.add_food()


def add_drink():
    print("staff2")
    mi.add_drink()


def list_food():
    mi.list_food()


def list_drink():
    mi.list_drink()


def add_stock():
    print("staff3")
    mi.add_stock()


def customer1():
    print("customer1")


def customer2():
    print("customer2")


def customer3():
    print("customer3")


def customer4():
    print("customer4")


def customer5():
    print("customer5")


def manage_cart_menu(manage_cart):
    print("Manage Cart Menu")
    option = 0

    while option < manage_cart.maximum:
        print(manage_cart)
        print('\n'.join(manage_cart.menu))
        option = menu_option(manage_cart)
        if option is not None:  # ie cancel was clicked
            if option == 1:
                cart1()
            elif option == 2:
                cart2()
            elif option == 3:
                cart3()
            elif option == 4:
                cart4()
            elif option == 5:
                cart5()
        else:
            option = manage_cart.maximum  # ie exit


def cart1():
    pass


def cart2():
    pass


def cart3():
    pass


def cart4():
    pass


def cart5():
    pass


def cart6():
    pass


if __name__ == '__main__': main()
