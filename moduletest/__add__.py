class Day(object):
    def __init__(self,visits,contacts):
        self.visits=visits
        self.contacts=contacts
    
    def __str__(self):
        return 'Visits: %i, Contacts: %i' %(self.visits,self.contacts)
    
    
    def __add__(self,other):
        total_visits=self.visits+other.visits
        total_contacts=self.contacts+other.contacts
        return Day(total_visits,total_contacts)
    
day1=Day(10,1)
day2=Day(20,2)
day3=day1+day2
day4=day3+day1
print(day4)
        