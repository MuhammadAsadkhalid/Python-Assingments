# WAP to input side of a square & print its area
side = input("Enter the length of the side of the square ")

area = int(side) ** 2

print ("This is the area of the square:", area)

# WAP to input 2 floating point numbers & print their average

num1 = float(input("Enter the first floating point number: "))
num2 = float (input("Enter the second floating point number: "))
average = (num1 + num2) / 2
print("The average of the two numbers is:", average)

#  WAP to input 2 int numbers, a and b. 
# Print True if a is greater than or equal to b. If not print False.

a = int(input("Enter the first integer number (a)   : "))
b = int(input("Enter the second integer number (b)   : "))
if a >= b:
 print("True")
else:
 print("False")