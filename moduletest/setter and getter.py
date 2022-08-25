#setter is used to set the values for private data
#getter is used to get the values of private data from outside the class

class Customer:
    customer_counter=0
    
    def __init__(self,name):
        self.name=name
        self.account_no=Customer.customer_counter+1
        Customer.customer_counter+=1
        self.__balance=0
    
    def withdraw_money(self,amount):
        self.__balance-=amount
        return self.__balance
    
    def deposit_money(self,amount):
        self.__balance+=amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount>0:
            self.__balance=amount
            
c1=Customer('Bivek')
c2=Customer('Prayu')

c1.deposit_money(1000)
c2.deposit_money(2000)

print(f'The customer {c1.name} has a balance of {c1.get_balance()}')

c1.withdraw_money(2000)
c1.set_balance(1)
print(f'The customer {c1.name} has a balance of {c1.get_balance()} after withdraw')
        