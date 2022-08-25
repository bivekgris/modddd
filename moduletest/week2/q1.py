class Speaker:
    def __init__(self,jack,tweeters,woofers):
        self.jack=jack
        self.tweeters=tweeters
        self.woofers=woofers
    
    def play_music(self):
        return ('Playing Music')
    
    
class BluetoothSpeaker(Speaker):
    def __init__(self,jack,tweeters,woofers,connected_to):
        super().__init__(jack,tweeters,woofers)
        self.battery=100
        self.__connected_to=connected_to
    
    def play_music(self):
        return (f'Playing Music from {self.__connected_to}')
    
    def set_connected_to(self,device):
        self.__connected_to=device
    
    def get_connected_to(self):
        return self.__connected_to
    
q1_o1=Speaker(2.5,2,2)
q1_o2=BluetoothSpeaker(3.5,2,2,'PC')
print(q1_o2.play_music())
            
        
    
    
        