num1 = int(input("Enter the 1st Number:"))
num2=int(input("Enter the 2ndt Number:"))
operator=input("Give operator:")
if operator=="+":
    print(f"adiition of two numbers is {num1+num2}")
elif operator=="-":
     print(f"subtraction  of two numbers is{num1-num2}")
elif operator=="*":
    print(f"multiplication of two numbers is {num1*num2}")
elif operator=="/":
    print(f"division of two numbers is {num1*num2}") 
else:
    print("Invalid number")
