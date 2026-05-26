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
if total_avg >= 80:
    print("you got a B")
if total_avg >= 70:
    print("you got a C")
if total_avg >= 60:
    print("you got a D")
if total_avg < 60:
    print("you got an F")
if total_avg < 30:
    print("you are failed")    
