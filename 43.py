class Bank:
        def __init__ (self,acc_no,name,acc_type,balance) :
              self.acc_no=acc_no
              self.name=name
              self.acc_type=acc_type
              self.balance=balance
        def deposit(self,amount):
              self.balance=self.balance+amount
              print("Amount deposit successfully")     
        def withdraw(self,amount) :
              if amount <=self.balance:
                    self.balance=self.balance-amount
                    print("Amount withdrawn successfully")
              else:
                    print("insufficient balance")
        def display(self):
              print("account number :" ,self.acc_no)
              print("name:",self.name)         
              print("Account Type:",self.acc_type) 
              print("balance:",self.balance) 
                                              

b1=Bank(1,"Varsha","savings",5000)
b1.display()
b1.deposit(2000)


print("balance after deposit:" ,b1.balance)
b1.withdraw(1000)
print("balance after withdrawal :",b1.balance)

