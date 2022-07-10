first = input("enter first num: ")
operator = input("enter operator (+,-,*,/,%) :")
second = input("enter seond num: ")

first = int(first)
second = int(second)

if operator == "+":
	print(first + second)
elif operator == "-":
	print(first - second)
elif operator == "*":
	print(first * second)
elif operator == "/":
	print(first / second)
elif operator == "%":
	print(first % second)
else: 
	print("Invalid operator")

	