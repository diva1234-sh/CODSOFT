num1=int(input("enter the  first number"))
num2=int(input("enter the second number "))
operation=input("can be +, -,*,/")
if operation== '+':
  result= num1 + num2
elif operation=="-":
  result= num1-num2
elif operation=="*":
  result= num1*num2
elif operation=="/":
        if num2!=0:
          result=num1/num2
        else :
           result="error, division by zero"
else:
   result="invalid operation" 

print("result:", result)                  
