username_Input = input("Username: ")
password_Input = input("Password: ")
if username_Input == "Praw" and password_Input == "1997":
    print("------ Welcome to my Shop YO ------")
    print(">> Select item you want to buy !")
    print("1. Toy Dog        20 THB")
    print("2. Food dog       30 THB")
    userSelected = int(input("Select an option: "))
    prices = {
        1: 20,
        2: 30,
    }
    if userSelected in prices:
        quantity = int(input("Quantity :"))
        totalQuantity = prices[userSelected] * quantity
        vat = 7 / 100
        totalVat = totalQuantity * vat
        totalPrice = totalVat + totalQuantity
        print("Your price is: ", totalQuantity , "THB")
        print("Vat 7%:", totalVat)
        print("Your total price is:", totalPrice, "THB")
    else:
        print("Invalid option")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Thank you")
else:
    print(">> Invalid username or password")
