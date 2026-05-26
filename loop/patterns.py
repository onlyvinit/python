# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()
    
#1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3 
# 4 4 4 4 4
# 5 5 5 5 5

# for i in range(5, 0, -1):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()

# for i in range (1, 6):
#     for j in range (1, i+1):
#         print("*", end=" ")
#     print()
    
# for i in range (4, 0, -1):
#     for j in range (1, i+1):
#         print("*", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#         j += 1
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
    
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
    
# for i in range (5, 0, -1):
#     for j in range (1, i+1):
#         print(j, end=" ")
#     print()
    
# for i in range (1, 6):
#     for j in range (1, i+1):
#         print(j, end=" ")
#     print()

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(n, i-1, -1):
        print(j, end=" ")
    print()