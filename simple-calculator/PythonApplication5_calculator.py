#Simple Calculator -Sum of Two Numbers
from ast import Mult


print("welcome to alaa calculator")
Num1 =input("Enter the First Num:   ")
Num2 =input("Enter the secand Num:  ")
Num1=float(Num1)
Num2=float(Num2)
operator=str (input("Enter your operato * / + - :  "))

minn= Num1-Num2
div=Num1*Num2
Mult=Num1/Num2
if operator =='+':
  print("result = ", Num1+Num2 )
elif operator=='-':
    print("result = " , minn)
elif operator =='*': 
    print("result = " , div)
elif operator =='/':
   print("result = " , Mult)
else:  None