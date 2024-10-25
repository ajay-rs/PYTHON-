class College:
    def init(self):
        print("college constructor")



    class Dept:
        def init(self):
            print("Dept Constructor")


        def meeting(self):
            print("Dept Meetings")



management = College()
hod =Dept()
hod.meeting()
