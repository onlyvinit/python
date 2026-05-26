# CONTINUE AND BREAK STATEMENTS
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. The break statement is used to exit the loop entirely.

# Example of continue statement in a loop
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Example of break statement in a loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
total = 0
while True:
    number = int(input("add the number: ")) 
    if number == 0:
        break
    if number < 0:
        continue
    total += number
print("Total:", total)