# a = 9
# b = 8
# c =sum ((a,b)) #built in function
# def function1(a,b):
#     print("hello you are in function 1", a+b)
# def function2(a,b):
#     average = (a+b)/2
#     print(average)
#     return average
# v = function2(5, 7)
# print(v)
print("enter number 1")
num1 = input()
print("enter number 2")
num2 =input()
try:
    print("sum of these two numbers is",
      int(num1)+int(num2))
except Exception as e:
    print(e)

print("this line is very important")