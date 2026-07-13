import math
print("            =================================")
print("                ______Mini calculator_____")
print("            =================================")

print("1. Addition")
print("2. Substraction")
print("3. Multipication")
print("4. Division")
print("5. Factor")
print("6. Squre")
print("7. HCF")
print("8. LCM")
print("9. Power")
print("10.square root")

choice =int (input("Enter your choice:"))

if choice==1:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("sum=",num1+num2)

elif choice==2:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("sub=",num1-num2)

elif choice==3:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("mult=",num1*num2)

elif choice==4:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("divi=",num1/num2)
    
elif choice==5:
    num = int(input("enter the value of num: "))
    print("Factorial:",math.factorial(num))  

elif choice==6:
    num = int(input("enter the value of num: "))
    print("Squre=",num *num)      

elif choice==7:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("HCF=",math.gcd(num1,num2))
        
elif choice==8:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("LCM=",math.lcm(num1,num2))        

elif choice==9:
    num1 = int(input("enter the value of num1:"))
    num2 = int(input("enter the value of num2:"))
    print("power=",math.pow(num1,num2))

elif choice==10:
    num = int(input("enter the value of num: "))
    print("sub=",math.sqrt(num))

else:
    print("please enter the valid choice..")