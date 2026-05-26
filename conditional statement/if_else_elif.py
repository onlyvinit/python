maths = input("maths: ")
science = input("science: ")
social_science = input("social science: ")
english = input("english: ")
physics = input("physics: ")

total = int(maths) + int(science) + int(social_science) + int(english) + int(physics)
total_avg = total / 5

print(total_avg)

if total_avg >= 90:
    print("you got an A")
elif total_avg >= 80:
    print("you got a B")
elif total_avg >= 70:
    print("you got a C")
elif total_avg >= 60:
    print("you got a D")
elif total_avg >= 50:
    print("you got an F")
elif total_avg >= 30:
    print("you got an H")
else:
    print("you are failed")  
