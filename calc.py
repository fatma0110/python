num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
operation = input("enter one of + - * / mod pow abs and : ")

if operation == '+':
    print(f"{num1} + {num2} = {num1+num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1-num2}")
elif operation == '*':
    print(f"{num1} * {num2} = {num1*num2}")
elif operation == '/':
    print(f"{num1} / {num2} = {num1/num2}")
elif operation == 'mod':
    print(f"{num1} % {num2} = {num1%num2}")
elif operation=='pow':
    print(f"{num1} ** {num2} = {num1}**{num2}")
elif operation == 'abs':
    print(f"abs {num1} = {abs(num1)}")
else:
    print("Thank You")