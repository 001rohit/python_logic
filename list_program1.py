lst1=[]
def Append():
    print("\n1) Add Element in list\n")
    input1 = int(input("How many time Enter value in list: "))
    for i in range(1,input1+1):
        val1 = int(input("Enter any number: "))
        lst1.append(val1)

def PrintList():
       print()
       print("2)  print  list")
       print("List: ",lst1)
       print()
     
def Pop():
     print("3) Remove last element in list")
     if(len(lst1)>0):
            lst1.pop()
     else:
          print()
          print("\nYour list isEmpty,Please Add element in list\n")   
          print()
    
def remove():
     print("4) Remove element in list for any one index")
     if(len(lst1)>0):
               remo = int(input("Enter any value in index: "))
               lst1.pop(remo)
     else:
          print("\nYour list is Empty,Please Add element in list\n")
           

def insert1():
     print("5) Insert Element in index to any position in list")
     if(len(lst1)>0):
            index = int(input("Enter any value in list index: "))
            value = int(input("Enter value in list of item: "))
            lst1.insert(index,value)
     else:
          print("\nYour list is Empty,Please Add element in list\n")

def Clear():
     print("6) Clear Element in list")
     if(len(lst1)>0):
          lst1.clear()
     else:
          print("\nYour list is Empty\n")

def reverse():
     print("7) Reverse Element in list")
     lst1.sort(key=None,reverse=True)

def check_lst():
          print("8) Check Element in list Empty or Not")
          if(len(lst1)==0):
               print("\nlist is Empty")
          else:
               print("\nElements is present in list")

def check_lengthList():
        print("9) check length of list")
        if(len(lst1)>0):
                   print("The Length of list: ",len(lst1))
        else:
                 print("List is Empty")

def Find_index(): 
       print("10) Find index with help to Element ")
       if(len(lst1)>0):
                 val = int(input("Enter Element value : "))
                 if(val<=len(lst1)):
                              print("Index: ",lst1.index(val))
                 else:
                        print("invalid index")
       else:
          print("\nYour list is Empty,Please Add element in list\n")
           
      
def Find_Number():
          print("11) Find Element with help to index value")
          if(len(lst1)>0):
               index = int(input("Enter index: "))
               if(index<= len(lst1)-1):
                   print("Element: ", lst1[index])
               else:
                     print("Invalid Element")
          else:
              print("\nYour list is Empty,Please Add element in list\n")
          
def Check_Number_Repeat():
          print("12) check Number Repeat or No-repeat")
          if(len(lst1)>0):
                  intVal = int(input("Enter any number: "))
                  if(intVal<=len(lst1)):
                              print(f"The Element {intVal} Present in list ",lst1.count(intVal)," time ")
                  else:
                               print(f"{intVal}  Element is not available in list ")
          else:
             print("\nYour list is Empty,Please Add element in list\n")
            
choice=0
while choice!=13:
        print("\n\n1 Add Element in list")
        print("2 print  list")
        print("3 Remove last element in list")
        print("4 Remove element in list for any one index")
        print("5 Insert Element in index to any position in list")
        print("6 Clear Element in list")
        print("7 Reverse Element in list")
        print("8 Check Element in list Empty or Not")
        print("9 check length of list")
        print("10 Find index with help to Element ")
        print("11 Find Element with help to index value")
        print("12 check Number Repeat or No-repeat")
        print("13 Exit this program\n")

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
        elif(choice==10):                     
                Find_index()
        elif(choice==11):                     
                Find_Number()
        elif(choice==12):                     
                Check_Number_Repeat()
        elif(choice==13):                     
                break
        else:
               print()
               print("Not found This Type Option Please Enter Your Correct choice ")
               print() 

