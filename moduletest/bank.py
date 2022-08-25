class Customer:
    def __init__(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
        #self.__balance=0 this will create private variables
        self.dr_card_no=None
        
    def withdraw_money(self,amount):
        self.balance-=amount
        return self.balance
    
    def deposit_money(self,amount):
        self.balance+=amount
        return self.balance
    
c1=Customer('Bivek', 111222)
c2=Customer('Prayu',222333)
print(c1.balance)
print(c1.withdraw_money(200))
print(c2.deposit_money(100))
