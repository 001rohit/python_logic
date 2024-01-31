lst1=[]
def Append():
    input1 = int(input("Enter any number: "))
    for i in range(1,input1+1):
        val1 = int(input("Enter any number: "))
        lst1.append(val1)

def PrintList():
       print(lst1)
    
def Pop():
     lst1.pop()
    
def remove():
     remo = int(input("Enter any value in index"))
     lst1.pop(remo)

def insert1():
     index = int(input("Enter any value in list index: "))
     value = int(input("Enter value in list of item: "))
     lst1.insert(index,value)

def Clear():
     lst1.clear()

def reverse():
     lst1.sort(key=None,reverse=True)

def check_lst():
          if(len(lst1)==0):
               print("list is Empty")
          else:
               print("Elements is present in list")
def check_lengthList():
       print(len(lst1))

# choice=0
while choice!=10:
        print("1 Add Element in list")
        print("2 print  list")
        print("3 Remove last element in list")
        print("4 Remove element in list for any one index")
        print("5 Insert Element in index to any position in list")
        print("6 Clear Element in list")
        print("7 Reverse Element in list")
        print("8 Check Element in list")
        print("9 check length of list")
        print("10 Exit this program")

        choice = int(input("Enter your choice: "))
        if(choice==1): 
             Append()
        elif(choice==2):                     
             PrintList()
        elif(choice==3):                     
                Pop()
        elif(choice==4):                     
               remove()
        elif(choice==5): 
              insert1()                    
        elif(choice==6):                     
                Clear()
        elif(choice==7):                     
                reverse()
        elif(choice==8):                     
                check_lst()
        elif(choice==9):                     
                check_lengthList()
        elif(choice>=10):                     
                break

