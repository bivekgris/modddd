class SavingAccount:
    def __init__(self,name,acc_no):
        self.name=name
        self._acc_no=acc_no
        self._balance=0
        
    def get_account_no(self):
        return self._acc_no
    
    def get_balance(self):
        return self._balance
    
    def deposit(self,amount):
        self._balance+=amount
        return self._balance
    
    def withdraw_money(self,amount):
        self._balance-=amount
        return self._balance
    
class StudentAccount(SavingAccount):
    def __init__(self,name,acc_no,student_id):
        super().__init__(name,acc_no)
        self.__student_id=student_id
        
    def get_student_id(self):
        return self.__student_id
    
savingacc=SavingAccount('Prayusha',1212)
savingacc.deposit(1000)
stu_acc=StudentAccount('Bivek',3333,'a1866934')
stu_acc.deposit(400)
print(f'{savingacc.name} has a balance of {savingacc.get_balance()}')
print(f'{stu_acc.name} has a balance of {stu_acc.get_balance()} and student id {stu_acc.get_student_id()}')
print(stu_acc.balance)