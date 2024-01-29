symbols = ["+", "-", "*", "/"]
print(symbols)

var = ""
while var not in symbols:
    var = input("Choose symbol: ")
while True:
    try:
        if var == "+":
            num1 = float(input("Choose first number: "))
            num2 = float(input("Choose second number: "))
            print(num1 + num2)
        if var == "-":
            num1 = float(input("Choose first number > second number: "))
            num2 = float(input("Choose second number: "))
            print(num1 - num2)
        if var == "*":
            num1 = float(input("Choose first number: "))
            num2 = float(input("Choose second number: "))
            print(num1*num2)
        if var == "/":
            num1 = float(input("Choose first number: "))
            num2 = float(input("Choose second number: "))
            print(num1/num2)
        break
    except ValueError:
        print("please input two numbers")