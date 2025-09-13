# # question 1:
# x = int(input("Enter first integer: "))
# y = int(input("Enter second integer: "))

# print(x ** y)

# question 2:
m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))
if m < n:
    print(m)
if  m >= n:
    while m >= n:
        m = m - n
    print(m)

m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))

if m < n:
    print(m)
if m >= n:
    print(m%n)

# # question 4:
# dob =input("Enter your date of birth: ")
# year = int(dob[6:])
# print(year)


# # question 5:
# val = []
# num = input("Enter a number: ")
# val.append(num)
# f1 = int(val[0][0])
# f2 = int(val[0][1])
# # Split the input string by commas and convert each part to int
# nums = [int(x) for x in val[0].split(',')]
# f1, f2, f3, f4, f5 = nums
# product = f1 * f2 * f3 * f4 * f5
# print(product)
# f4 = int(val[0][3])
# f5 = int(val[0][4])
# sum = f1+f2+f3+f4+f5
# print(sum)
