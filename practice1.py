# sum of even number
def sum_even():
    num=int(input("Enter any number: "))
    sum1_even=0
    for i in range(0,num+1):
           if(i%2==0):
               sum1_even+=i

    print(sum1_even)

# sum_even()

# sum of Odd number
def sum_odd():
    num=int(input("Enter any number: "))
    sum1_odd=0
    for i in range(0,num+1):
           if(i%2!=0):
               sum1_odd+=i
    if(sum1_odd%2==0):
         print("It is give even number sum ",sum1_odd)
    else:
         print("It is give odd number sum ",sum1_odd)

# sum_odd()

# Find Prime number
def Find_prime():
    num1 = int(input("Enter number: "))
    count = 0
    for i in range(1,num1+1):
          if(num1%i==0):
                count+=1
    if(count==2):
         print("Give number is prime")
    else:
         print("Give number is not prime number")

# Find_prime()
         
# Find Factorial
        
def Find_Factorial():
    num1 = int(input("Enter any number: "))
    fact=1
    for i in range(1,num1+1):
          fact*=i
    print(fact)

# Find_Factorial()
         
# Find_LCM
        
def Calc_LCM():
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     num3 = int(input("Enter second number: "))
     hcf=0
     if(num1>num2 and num1>num3):
          largest=num1
     elif(num2>num1 and num2>num3):
           largest = num2
     elif(num3>num1 and num3>num2):
           largest = num3
     elif(num1==num2==num3):
          largest=num1     
    #  if(num1>num2):
    #       small = num2
    #  else:
    #       small=num1
     for i in range(1,largest+1):
          if(num1%i==0) and (num2%i==0) and(num3%i==0):
              hcf=i
     print(hcf)
            
     LCM=num1*num2*num3/hcf
     print(LCM)
    
# Calc_LCM()