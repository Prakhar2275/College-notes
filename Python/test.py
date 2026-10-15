# iterative statements 
# if we want to execute a group of statements multiple times then we should go fo iteratice statements python support 2 type of itterative statement 
#  for loop 
#  while loop

# /to print hello 10 times 

# for r in range(10):
#     print("hello")
 
# to display no. form 1 to 10 

# for i in range(10):
#     print(i+1)
    
# to diplay odd no. in rangel 0-20


# for i in range(20):
#     if(i%2!=0):
#         print(i)


# pattern printing 

# for i in range(5):
#     for j in range(i):
#         print("*")


# a=10
# def f1():
#     a=777 #local varable
#     print(a)
#     print(globals()['a'])

# f1()

# lambda function

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# iseven = lambda n: n % 2 == 0
# isodd = lambda n: n % 2 != 0
# even_numbers = list(filter(iseven, numbers))
# odd_numbers = list(filter(isodd, numbers))
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)

# regex programs-------------------------
import re

#Email validation
# email = input("Enter email address: ")
# pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# if re.fullmatch(pattern_email, email):
#     print("Valid email")
# else:
#     print("Invalid email")

#  Mobile number validation
# import re

# mobile_number = input("Enter mobile number: ")
# pattern_mobile = r'^[6-9]\d{9}$'

# if re.fullmatch(pattern_mobile, mobile_number):
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")



# PAN number validation
# pan_number = input("Enter PAN number: ")
# pattern_pan = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

# if re.fullmatch(pattern_pan, pan_number):
#     print("Valid PAN number")
# else:
#     print("Invalid PAN number")

# Aadhar number validation
# adhar_number = input("Enter Aadhar number: ")
# pattern_adhar = r'^\d{12}$'

# if re.fullmatch(pattern_adhar, adhar_number):
#     print("Valid Aadhar number")
# else:
#     print("Invalid Aadhar number")

# Password validation
# password = input("Enter password: ")
# pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# if re.fullmatch(pattern_password, password):
#     print("Valid password")
# else:
#     print("Invalid password")





# Program: make a list (using a for loop) of squares of even numbers
# def even_squares_upto(n):
    
#     result = []
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             result.append(i * i)
#     return result


# if __name__ == "__main__":
    # Example: squares of even numbers up to 10
    # n = 10
    # print("Squares of even numbers up to", n, ":", even_squares_upto(n))


# def generate_num(n):
#     for i in range(1,n+1):
#         yield i

# for value in generate_num(5):
#     print(value)

# subjects=["hello","guys","itss","MEhhhh","CPP"]
# for i,v in enumerate(subjects):
#     print(i,v)

# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple)


# ===================== NESTED DICTIONARY =====================

# Example 1: Simple nested dictionary
# student = {
#     "name": "John",
#     "age": 20,
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "zipcode": "10001"
#     },
#     "courses": {
#         "math": 85,
#         "science": 90,
#         "english": 78
#     }
# }

# # Accessing nested dictionary values
# print("Student Name:", student["name"])
# print("City:", student["address"]["city"])
# print("Math Score:", student["courses"]["math"])

# # Example 2: Adding values to nested dictionary
# student["address"]["country"] = "USA"
# print("Updated Address:", student["address"])

# # Example 3: Iterating through nested dictionary
# print("\nCourses and Scores:")
# for subject, score in student["courses"].items():
#     print(f"{subject}: {score}")

# # ===================== DICTIONARY OF CUBES OF ODD NUMBERS (1-10) =====================

# # Program: Create a dictionary of cube of odd numbers in range 1-10
# cube_odd_dict = {}

# for num in range(1, 11):
#     if num % 2 != 0:  # Check if number is odd
#         cube_odd_dict[num] = num ** 3

# print("\nDictionary of cubes of odd numbers (1-10):")
# print(cube_odd_dict)

# # Alternative method using dictionary comprehension
# cube_odd_dict_v2 = {num: num**3 for num in range(1, 11) if num % 2 != 0}
# print("\nUsing Dictionary Comprehension:")
# print(cube_odd_dict_v2)

# # Display individual cubes
# print("\nIndividual Odd Numbers and Their Cubes:")

# for num, cube in cube_odd_dict.items():
#     print(f"Cube of {num} = {cube}")   

# from durgamata import add as sum
# print(sum(10,20))


# def fact(n):
#     if(n==1):
#         return 1
#     return n*fact(n-1)
# print(fact(4));

# f=open("abc.txt","r")
# print(f.read())
# f.close()

# f=open("abc.txt","a")
# f.write("this is the next line")
# f.close()

# f=open("abc.txt","w")
# list=["mannu\n","sahil\n","shivam\n","pranav\n","rohan\n","shagun\n"]

# f.writelines(list)
# print("data written successfully")
# f.close()

# TRY CATCH BLOCK STATEMENT!!!!!!!

#  custom exception handeling for insuffiicient baalnce 

# class insufficientBalance(Exception):

#     def __init__(self,msg):
#         print(msg)


    
class account:
    def __init__(self,acc_num,acc_bal):
        self.acc_num=acc_num
        self.acc_bal=acc_bal

    def deposit(self,amount):
        self.acc_bal+=amount
        

    def withdraw(self,amount):
        try: 
            if self.acc_bal>=amount:
                self.acc_bal-=amount
            else:
                raise ValueError("insufficient balance!!!")
        except ValueError as e:
            print(e)

    # Static methodss
# --------------------based on inilitalization this method can be tered as static or instance method----------------
    @staticmethod
    def m1(acc_num):
        print(acc_num)


a1=account(1,1000)
a1.withdraw(10000)

account.m1(123)
a1.m1()
