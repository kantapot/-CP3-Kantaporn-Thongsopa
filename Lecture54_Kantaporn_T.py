def login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "1234":
        print(">> Done, Welcome !")
        return True
    else:
        print(">> Wrong username or password !")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userChoice = int(input("Select an option: "))
    return userChoice

def vatCalculate():
    price = int(input("Price of product : "))
    vat = 7/100
    result = price + (price * vat)
    return result

def vatTotal(totalPrice):
    vat = 7/100
    result = totalPrice + (totalPrice * vat)
    return result

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    return vatTotal(totalPrice)

if login() == True:
    showMenu()
    selects = menuSelect()
    if selects == 1:
        print(".............................................................")
        print("Total price (vat7%):", vatCalculate(), "฿")
    elif selects == 2:
        print("............................................................")
        print("Total price (vat7%):", priceCalculate(), "฿")
    else:
        print("Wrong selection !")
print("..............Thank you..............")
