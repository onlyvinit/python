# number = int(input("add number: "))
# end_number = int(input("number you would like to end with: "))
# sum = 0

# if end_number < number:
#     print("End number must be greater than or equal to the starting number.")    
# else :
#     pass
# while number <= end_number:
#     sum += number 
#     print(f"{sum} ", end="")
#     number += 1   
    

# table = int(input("add number you'd like to have table of:"))
# b = 1
# while b <= 10:
#     print(f"{table} x {b} = {table * b}")
#     b += 1


number1 = int(input("add number: "))
end_number1 = int(input("number you would like to end with: "))
total = 0
counter = 0

i = number1

if end_number1 < number1:
    print("End number must be greater than or equal to the starting number.")    
else :  
    pass
while i <= end_number1:
    if i % 2 == 0 and i % 7 == 0:
        total += i 
        counter += 1
        print(f"{i} ", end="")
    i += 1
print(f"Total: {total}")
print(f"Counter: {counter}")