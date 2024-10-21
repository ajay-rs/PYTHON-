class Telephone:
    def __init__(self, name, programs):
        self.name = name
        self.programs = programs
        
    
    def call(self):
        print(self.name,"Calling")

    def receive(self):
        print("Receiving")

class Mobile(Telephone):
    
    def chat(self):
        print("Chatting")
nokia= Mobile("Vettaiyan",630)
nokia.chat()
nokia.call()
nokia.receive()

