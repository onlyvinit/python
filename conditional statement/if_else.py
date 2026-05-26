# age = int(input("What is your age? :"))
# if age < 18 :
#     print("you are a kid")
# if age >= 18 and age < 60 :
#     print("you are an adult")
# if age >= 60 :
#     print("you are a senior citizen")
# else :
#     print("invalid age")  

# nasted if-else statement

age  = int(input("What is your age? :"))
certficate = str(input("Do you have a certificate? (yes/no) :"))
if certficate.lower() == "yes" :
    certficate = True
if certficate.lower() == "no" :
    certficate = False

if age >= 18 and age < 60 :
    if certficate ==  True :
        print("you are eligible for the job")
    elif certficate == False :
        print("get a certificate to be eligible for the job")
if age < 18  :
    if certficate ==  True :
        print("we will consider you for the job when you turn 18")
    elif certficate == False :
        print("you are not eligible for the job")
else :
    print("invalid age")