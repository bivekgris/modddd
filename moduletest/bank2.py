class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
        #self.__balance=0 this will create private variables
        
    def withdraw_money(self,amount):
        self.balance-=amount
        return self.balance
    
    def deposit_money(self,amount):
        self.balance+=amount
        return self.balance
    
    def bankFees(self):
        self.balance=self.balance-0.05*self.balance
        return self.balance
    
    def display(self):
        return (f'{self.name}')
    
c1=BankAccount('Bivek', 111222)
c2=BankAccount('Prayu',222333)
print(c1.balance)
print(c1.withdraw_money(200))
print(c2.deposit_money(100))
