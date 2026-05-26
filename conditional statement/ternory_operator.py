age = int(input("enter your age:"))

result = "an adult" if age >= 18 and age < 60 else "child" if age < 18 else "senior citizen" if age >= 60 else "invalid age"
print(result)

number = int(input("enter a number:"))

result = "positive" if number > 0 else "negative" if number < 0 else "zero" if number == 0 else "invalid number"
print(result)