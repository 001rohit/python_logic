class Bank:
    def __init__(self):
        self.name = name
        self.account_type =""
        self.bank_name =""
        self.mobile_no =""
        self.ammoun =0
        self.ammoun1 =0
    def CreateData_Acc(self):
        self.name = input("Enter Your name: ")
        self.account_type = input("Enter Your Account: ")
        self.bank_name = input("Enter bank name: ")
        self.mobile_no = int(input("Enter your mobile number: "))

    def Display_data(self):
        print(f"Customer name: {self.name}")
        print(f"Your Account type: {self.account_type}")
        print(f"Bank name: {self.bank_name}")
        print(f"mobile number: {self.mobile_no}")
   

      
    def Check_ammount(self):
          print(f"You Balance is {self.ammoun}")

     
    def Add_ammount(self):
             self.ammoun1 = int(input("Enter ammount: "))
             self.ammoun+=self.ammoun1

    def Deb_ammount(self):
             self.ammoun1 = int(input("Enter ammount: "))
             self.ammoun-=self.ammoun1
   
    def check_balance(self):
          print(f"{self.name} Your balance is {self.ammoun}")
    
    def Upadate_accou(self):
          update = input("Enter your field name: ")

          if update.lower() =="name":
                self.name = input("Enter new name: ")
          elif update.lower() == "accout":
                self.account_type = input("Enter your choice")
          elif update == "mobile":
                self.mobile_no = int(input("Enter your choice"))

list_of_customer = {}
n = 0 
while (n !=7):
      print("\n\n 1. Creat New Account ")
      print("2. Display customer Data")
      print("3. Check your balance")
      print("4. Add amount ")
      print("5. Debit amount ")
      print("6. Updata user data")
      print("7. Exit")
      n=int(input("Enter you choice: "))

      if(n==7):
            break
      
      name = input("Enter your name: ")

      if name not in list_of_customer:
            list_of_customer[name] = Bank()

      if n==1:
            list_of_customer[name].CreateData_Acc()
     
      elif n==2:
            list_of_customer[name].Display_data()

      elif n==3:
            list_of_customer[name].Check_ammount()

      elif n==4:
            list_of_customer[name].Add_ammount()      
            
      elif n==5:
            list_of_customer[name].Deb_ammount()

      elif n==6:
            list_of_customer[name].Upadate_accou()        