# count = 0

# for i in range(1, 11): # range(start, stop, step-(by default it is 1) )
#     if i % 2 == 0:
#         count += 1
#         print(i)
# print(f"Count: {count}")

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))

# for i in range(start, end + 1): # range(start(include), stop(exclude) , step)
#         print(i)

# FACTORIAL OF A NUMBER

num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i 
print(f"Factorial of {num} is {factorial}") 