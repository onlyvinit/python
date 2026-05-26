# def hello():
#     print("hello world")
#     print("hello python")

# hello()


# ODD EVEN NUMBER
# def num_nature():
#     while True:
#         n = int(input("enter a number:"))

#         if n % 2 == 0:
#             print("even number")
#         if n == 0:
#             print("stop!")
#             break
#         else:
#             print("odd number")

# num_nature()

# FACTOR OF A NUMBER
# def factor():
#     while True:
#         n = int(input("enter a number:"))
#         if n == 0:
#             print("stop!")
#             break
#         elif n < 0:
#             print("enter a positive number")
#         else:
#             print("factors of", n, "are:")
#             for i in range(1, n + 1):
#                 if n % i == 0:
#                     print(i)

# factor()

# FACTORIAL OF A NUMBER

# def factorial ():
#     while True:
#         n = int(input("enter the number:"))
#         if n == 0:
#             print("stop")
#             break
#         elif n < 0:
#             print("please add positive number")
#         else:
#             total = 1
#             for i in range(1, n + 1):
#                 total *= i
#                 print(f"total :{total}")

# factorial()

# PYRAMID BUID WITH NUMBER

# def pyramid():
#     while True:
#         num = int(input("enter the num:"))
#         if num < 0 :
#             print("please enter positive number")
#         elif num == 0 :
#             print("stop!")
#             break
#         else:
#             for i in range(1, num + 1):
#                 for j in range(1, i + 1):
#                     print(f"{j}, end=" "")
#                 print(" ")

# pyramid()

# ATM (BALANCE)
# def atm(balance):
#     while True:
#         choice = input("1-Deposit  2-Withdraw  3-Check  4-Exit : ")

#         if choice != "1" and choice != "2" and choice != "3" and choice != "4":
#             print("Invalid choice! Please try again.")

#         elif choice == "1":
#             amount = int(input("Enter deposit amount: "))
#             balance = balance + amount

#         elif choice == "2":
#             amount = int(input("Enter withdraw amount: "))
#             if amount <= balance:
#                 balance = balance - amount
#             else:
#                 print("Insufficient balance!")

#         elif choice == "3":
#             print("Balance:", balance)


#         elif choice == "4":
#             print("bbyeee")
#             break

# balance = int(input("Enter starting balance: "))
# atm(balance)

# GRADE ANALYZER

def grade_analyzer(name):
    for i in name:
        
        maths = int(input("add maths marks :"))
        sci = int(input("add sci marks :"))
        bio = int(input("add bio marks :"))
        chemistry = int(input("add chemistry marks :"))
        total = maths + chemistry + bio + sci
        avarage = total / 4

        if avarage >= 50:
             grade = "A"
        elif avarage >= 40:
             grade = "B"
        elif avarage >= 30:
             grade = "C"
        elif avarage >= 25:
             grade = "D"
        elif avarage >= 20:
             grade = "E"
        else:
            print('You got "NOTHING, YOU FUCKING FAILURE"')
            
        print(
            f"Hey {name} your marks are maths {maths}, sci {sci}, bio {bio}, chemistry {chemistry} and your total is {total} with Grade {grade}. "
        )
        
        another = input("check another student marks? (yes/no) : ")
        if another == "yes":
            grade_analyzer(name = str(input("enter your name: ")))
        else:
            print("thank you for using grade analyzer")
            break

student = str(input("enter your name: "))
grade_analyzer(student)