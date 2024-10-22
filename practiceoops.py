
class IPL: 

    def __init__(self,name):
        self.name = name

    @classmethod
    def net_practice(cls):
        print("Net Practice")

    def play(self):
        print(self.name, 'is playing')

player1 = IPL("dhoni")
player2 = IPL("rohit")
player1.net_practice()
player2.net_practice()
player1.play()
player2.play()
IPL.net_practice()



'''



class IPL: 

    def __init__(self,*details):
        self.details = details



    @classmethod
    def net_practice(cls):
        print("Net Practice")
 

    def play(self):
        print(self.details, 'is playing')

    ##@staticmethod
    ##def play():
        #print('is playing')

player1 = IPL("dhoni","wk")
player2 = IPL("rohit")
player1.net_practice()
player2.net_practice()
player1.play()
player2.play()

IPL.net_practice()






'''






















