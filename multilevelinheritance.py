class Telephone:
    rental = 300
    def call(self):
        print("Calling")

    def receive(self):
        print("Receiving")

class Mobile(Telephone):
    rental = 400
    #Method Overriding
    def call(self):
        print("Calling wireless")
    def chat(self):
        print("Chatting")

class SmartPhone(Mobile):
    def browse(self):
        print("Internet")

nokia = Mobile()
nokia.chat()
nokia.call()
nokia.receive()
print(nokia.rental)
print(Telephone.rental)

vivo = SmartPhone()
vivo.call()
vivo.chat()
vivo.browse()


=============================================================
class Father:
    def work(self): 
        print("Lawyer")

class Mother:
    def work(self):
        print("Doctor")

class Child(Mother,Father):
    def play(self):
        print("playing in ground")

ch = Child()
ch.work()
ch.play()



