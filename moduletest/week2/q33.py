class Universe:
    # def __init__(self,sizeval):
    #     self.sizeval=sizeval
        
    def composition(self):
        return 'Made up of atoms'
    
    def size(self,sizeval):
        return (f'size-{sizeval}')

class Sheldon(Earth):
    pass

class Earth(Solarsystem):
    pass
 
    