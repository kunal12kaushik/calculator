op = input(''' please try any math operator
+ for addition
- for substraction
/ for division
* for multiplication''')

print("enter your first number ")
n1 = int(input())
print("enter your second number")
n2 = int(input())

if (op=='+'):
    print( "sum of these two numbers is", int(n1)+int(n2))
elif(op=='-'):
    print("sum of these two numbers is", int(n1)-int(n2))

elif(op=='/'):
    print("sum of these two numbers is", int(n1)/int(n2))

elif(op=='*'):
    print("sum of these two numbers is", int(n1)*int(n2))

else:
    print("you`ve not types a valid operator")