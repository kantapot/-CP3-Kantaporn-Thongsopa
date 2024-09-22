price = int(input("Your Price: "))
def vatCalculate(price):
    result = (price)+(price * 7 / 100)
    return result
print("Total your Price =", vatCalculate(price))
