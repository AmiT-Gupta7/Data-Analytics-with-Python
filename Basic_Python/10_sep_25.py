# time = int(input("Enter time :"))

# if (time < 10):
#     print("Longer")
#     price = int(input("Enter price :"))
#     if (price > 500):
#         print("Train")
#     else:
#         print("coach")
# else:
#     print("Shorter")
#     price = int(input("Enter price :"))
#     if (price > 200):
#         print("Daytime Filght")
#     else:
#         print("Red Eye Flight")

# str = input("Enter a string :")
# output=""
# if "a" in str:
#     output+="a"
# if "e" in str:
#     output+="e"
# if "i" in str:
#     output+="i"
# if "o" in str:
#     output+="o"
# if "u" in str:
#     output+="u"
# print(output)

# num = int(input("enter number :"))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev*10  + digit 
#     num = num//10
# print(rev)

# num = int(input("enter number :"))
# num1 = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev*10  + digit 
#     num = num//10
# if num1 == rev:
#     print("Palindrom...")
# else:
#     print("Not a Palindrom...")

# str = input("Enter a String:")
# str1 = str[::-1]
# if str == str1:
#     print("Palindrom...")
# else:
#     print("Not a Palindrom...")

num = int(input("Enter a number :"))
for i in range(10):
    i += 1
    print(num,'X',i,'=',i*num)