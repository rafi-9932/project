class Bank:
 def __init__(self, balance):
    self.balance = balance
    self.min_withdrew = 100
    self.max_withdrew = 100000


 def get_balance(self):
    return self.balance


 def deposit(self,amount):
    if amount > 0:
       self.balance += amount

 def withdraw(self,amount):
     if amount < self.min_withdrew:
        print(f'fokra, you can not withdrew below {self.min_withdrew}')
     elif amount > self.max_withdrew:
        print(f'bank fokir hoye jabe , you can not withdrew than {self.max_withdrew}')
     else:
        self.balance -= amount
        print(f'here is your money{amount}')
     

brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(500000)


dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.get_balance())

   
