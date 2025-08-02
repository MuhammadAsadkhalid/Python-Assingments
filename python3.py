grades =["C", "D", "A", "A", "B", "B", "A"]
print (grades.count("A"))

#  WAP to count the number of students with the “A” grade in the following tuple.
students =  ("C", "D", "A", "A", "B", "B", "A")
print (students.count("A")) 

#  Store the above values in a list & sort them from “A” to “D”
alphabets =["C", "D", "A", "A", "B", "B", "A"]
alphabets.sort()
print(alphabets)


ask = input("enter your 1st favourite movie: ")
ask1 = input("Enter youe 2nd favourite movie: ")
ask2 = input("Enter your 3rd favourite movie: ")
movies = [ask,ask1,ask2]
print(movies)


check1 = [1, 2, 3, 2, 1]
check2 = [1, "abc", "abc", 1]

list1 = check1.copy()
list2 = check2.copy()

list3 = check1.reverse()
list4 =check2.reverse()

if  list1 == list3:
    print("Check 1 is palindrome")
else:
    print("Check 1 is not palindrome")
if list2 == list4:
    print("Check 2 is palindrome")  
else:
    print("Check 2 is not palindrome")