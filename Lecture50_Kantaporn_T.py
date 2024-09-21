n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def plusNumber(n1, n2):
    return n1 + n2
def minusNumber(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divideNumber(n1, n2):
    if n2 != 0:
        return n1 // n2
    else:
        return "n2 = zero"

print("+ : ", plusNumber(n1, n2))
print("- : ", minusNumber(n1, n2))
print("* : ", multiply(n1, n2))
print("/ : ", divideNumber(n1, n2))
