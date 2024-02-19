import time 

x = 1
print("Start")
x=1
while x<=10:
     print()
     time.sleep(.5)
     print(x)
     x+=1
     if(x==11):
          print("End")
          x=1
          print()
          print("Start")
