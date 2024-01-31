def check_ability():
      age = int(input("Enter your age =):  "))
      if(age>=18):
              print("You can vote")
      else:
            print("Please wait for age above 18")
       
def check_Status():
        gender1 = int(input("Enter number (1 to 2) ):  "))
        if(gender1==1):
              print("Your gender is Female")
        elif(gender1==2):
              print("Your gender is Male")
        # if(gender1.upper()=="M"):
        #       print("Your gender is Male")
        # elif(gender1.upper()=="F"):
        #       print("Your gender is Female")
              
def check_day_schedule():
      day = int(input("Enter number (1 to 7): "))
      if(day==1):
            print("Sunday: Watch Movie")
      elif(day==2):
            print("Monday : working with my team members")
      elif(day==3):
            print("Tuesday : working with my Family members")
      elif(day==4):
            print("Wednesday: Rest my mind and body relax")                  
      elif(day==5):
            print("Thursday :Time Spande with my Family ")
      elif(day==6):
            print("Friday : Prepared  My Daily Routine Chart ")
      elif(day==7):
            print("Saterday : Travel and Tour ")       

def check_favorit_fruit():
        fruit = int(input("Enter number (1 to 5): "))
        if(fruit==1):
            print("Your favorit fruit is Banan")
        elif(fruit==2):
            print("Your favorit fruit is Apple")
        elif(fruit==3):
            print("Your favorit fruit is Graps")
        elif(fruit==4):
            print("Your favorit fruit is Orange")
        elif(fruit==5):
            print("Your favorit fruit is Mango")    

def check_Your_hobby():
         hobby = int(input("Enter number (1 to 5): "))
         if(hobby==1):
               print("Your hobby is 'singing'")
         elif(hobby==2):
               print("Your hobby is Playing 'indoor games' ")
         elif(hobby==3):
               print("Your hobby is 'Driving car and bike' ")
         elif(hobby==4):
               print("Your hobby is 'Playing cricket and footbal' ")
         elif(hobby==5):
               print("Your hobby is 'Gym' ")

def check_favorit_color():
        color = int(input("Enter number (1 to 5): "))
        if(color==1):
             print("your favorit color is 'Red' ")        
        elif(color==2):
             print("your favorit color is 'Green' ")                           
        elif(color==3):
             print("your favorit color is 'Yellow' ")
        elif(color==4):
             print("your favorit color is 'Blue' ")
        elif(color==5):
             print("your favorit color is 'Black' ")
            
def check_favorit_place():
        place = int(input("Enter number (1 to 5): "))
        if(place==1):
            print("hill station")
        elif(place==2):
            print("Beach like sea")
        elif(place==3):
            print("Zoo")
        elif(place==4):
            print("Musiuam")    
        elif(place==5):
            print("Wild life century")
    
def Check_favorit_food():
        food = int(input("Enter number (1 to 5): "))
        if(food==1):
            print("Pizza")
        elif(food==2):
            print("chinese")
        elif(food==3):
            print("Burgar")
        elif(food==4):
            print("Edli Dosha") 
        elif(food==5):
              print("Pasta")

user_choice=0
while user_choice!=9:
            print("\n\n\tHuman mind Games\n")
            print("1 check your Ability"   )
            print("2 check your Status "   )
            print("3 check your day Status"   )
            print("4 check your favorit fruit"   )
            print("5 check your favorit hobby"   )
            print("6 check your favorit Color"   )
            print("7 check your favorit Place "   )
            print("8 check your favorit Food "   )
            print("9 Exit your Program\n\n") 
            user_choice = int(input("Enter your choise: "))                 
            if(user_choice==1):
                check_ability()

            elif(user_choice==2):
                check_Status()
            
            elif(user_choice==3):
                check_day_schedule()
  
            elif(user_choice==4):
                check_favorit_fruit()
                   
            elif(user_choice==5):
                check_Your_hobby() 

            elif(user_choice==6):
                check_favorit_color()

            elif(user_choice==7):
                check_favorit_place()

            elif(user_choice==8):
                Check_favorit_food()       

            elif(user_choice>=9):
                break   