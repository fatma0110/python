num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
operation = input("enter one of + - * / mod or pow: ")

if operation == '+':
    print(f"{num1} + {num2} = {num1+num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1-num2}")
elif operation == '*':
    print(f"{num1} * {num2} = {num1*num2}")
elif operation == '/':
    print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} ^ {num2} = {pow(num1,num2)}")
print(f"abs {num1} = {abs(num1)}")
print(f"abs {num2} = {abs(num2)}")