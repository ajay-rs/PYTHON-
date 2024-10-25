class Demo:
    count = 0
    def __init__(self):
        Demo.count+=1
        #print(Demo.count)

    @classmethod
    def display(cls):
        print(cls.count)





d1 = Demo()
d2 = Demo()
d3 = Demo()
d4 = Demo()

Demo.display()


class Employee:

    def __init__(self,ename, esalary):
        self.ename = ename
        self.esalary = esalary


    def display(self):
        #print(self.ename, 'gets', self.esalary)
        print(f'{self.ename} gets {self.esalary}')


emp = Employee('Raja',20000)
emp.display()


class Employee:
    def __init__(self,ename, esalary):
        self.ename = ename
        self.esalary = esalary



    def display(self):
        #print(self.ename, 'gets', self.esalary)
        print(f'{self.ename} gets {self.esalary}')





class Office:
    def increment(emp):
        emp.esalary = emp.esalary + 5000
        emp.display()

       
emp = Employee('Raja',20000)
Office.increment(emp)
