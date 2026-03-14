while True:

    a = float(input("First number: "))
    b = float(input("Second number: "))

    action = input("Select action (+-/*): ")

    if action == "+":
        print(a + b)
    if action == "-":
        print(a - b)
    if action == "/":
        print(a / b)
    if action == "*":
        print(a * b)