# x = int(input("Enter 1st positive integer :"))
# y = int(input("Enter 2nd positive integer :"))
# z = int(input("Enter 3rd positive integer :"))

# if ( ((x**2 + y**2) == z**2) or ((x**2 + z**2) == y**2) or ((y**2 + z**2) == x**2) ):
#     print("yes...")
# else:
#     print("NO...")

####_________ Set 4 ________####
# question 1:
# num = int(input("Enter a number :"))
# if num > 0:
#     print("Positive...")
# else:
#     print("Negative...")

# question 2:
# x = float(input("Enter a number :"))
# if (0 < x < 10):
#     x = x**2 + 2
#     print(x)
# else:
#     print(0)

# question 3:
# coins = int(input("Enter number of coins :"))   
# friend_1 = int(input("Enter coins with friend 1 :"))
# friend_2 = int(input("Enter coins with friend 2 :"))
# friend_3 = int(input("Enter coins with friend 3 :"))
# if (friend_1 + friend_2 + friend_3) == coins:
#     if (friend_1 != friend_2 or friend_2 != friend_3 or friend_3 != friend_1):
#         print("Fair...")
#     else:
#         print("Unfair...")
# else:
#     print("value is greater than total coins... Try again...")
    
# question 4:
import math
x = float(input("Enter a real number: "))
print("Greatest integer less than or equal to x:", math.floor(x))
print("Smallest integer greater than or equal to x:", math.ceil(x))


