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
adhar_number = input("Enter Aadhar number: ")
pattern_adhar = r'^\d{12}$'

if re.fullmatch(pattern_adhar, adhar_number):
    print("Valid Aadhar number")
else:
    print("Invalid Aadhar number")

# Password validation
password = input("Enter password: ")
pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.fullmatch(pattern_password, password):
    print("Valid password")
else:
    print("Invalid password")


# Program: make a list (using a for loop) of squares of even numbers
def even_squares_upto(n):
    
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(i * i)
    return result


if __name__ == "__main__":
    # Example: squares of even numbers up to 10
    n = 10
    print("Squares of even numbers up to", n, ":", even_squares_upto(n))

