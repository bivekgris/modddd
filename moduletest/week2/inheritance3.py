class BankAccount:
    def __init__(self,pin):
        self.__pin=pin
        self.__balance=0
    
    def deposit(self,pin,amount):
        if pin==self.__pin:
            self.__balance+=amount
            return self.__balance
        else:
            print ('Incorrect PIN')
    
    def withdraw(self,pin,amount):
        if pin==self.__pin:
            self.__balance-=amount
            return self.__balance
        else:
            return ('Incorrect PIN')
    
    def get_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return (f'Incorrect PIN')
    
    def change_pin(self, oldpin,newpin):
        if oldpin==self.__pin:
            self.__pin=newpin
            return self.__pin
        else:
            return (f'Incorrect PIN')
        
c1=BankAccount(123)
c1.deposit(123,100)
print(c1.get_balance(123))
c1.deposit(231,200)
print(c1.get_balance(123))
            