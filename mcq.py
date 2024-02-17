score=0
choice= 0
while choice!=5:
    print("Welcome to my computer quiz!")
    print("1) Basic mcq quize")  
    print("2) intermediat mcq quize")  
    print("3) advance mcq quize")  
    print("4) check your score")  
    print("5) Exit")
    choice = int(input("Please Enter your choice: "))
    if(choice==5):
      break
    if(choice==1):
        answare = input("What is the fullform of www: ").lower()
        if(answare=="world wide web"):
                  print("correct answare ")
                  score+=1
        else:
                 print("wrong answare")


    elif(choice==2):
        answare = input("What is the fullform of CPU: ").lower()
        if(answare=="central proccessing unit"):
                print("correct answare ")
                score+=1
        else:
                print("wrong answare")

    elif(choice==3):
      answare = input("What is the fullform of RAM: ").lower()
      if(answare=="random access memory"):
               print("correct answare ")
               score+=1
      else:
               print("wrong answare")
      
    elif(choice==4):
            if(score >0 and score<4):
                 print(f"Your score is {score}")
            
            elif(score>=4):
                  score=0
   
    
