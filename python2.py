# num = int(input("Entery the number: "))
# if num % 2 == 0:
#     print ("The Number is even ")
# else:
#     print ("The Number is odd ")


   
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
 print ("The first number is the largest ")
elif num2 >num1 and num2 > num3:
 print ("The scond number is the largest ")
elif num1 == num2 and num2 == num3:
 print ("The whole numbers are same ")
else:
 print ("The third number is the largest ")


num4 = int(input("Enter the number you wanted to check: "))
if num4 % 7 == 0: 
    print("The number is divided by 7")
else:
    print("The number is not divided by 7")