from Toaster import *
class SuperToaster(Toaster):

     def __init__(self, color, slots):
        Toaster.__init__(self, color, slots)
        self.temp = 0

     def calcTemp(self):
        if(self.time * 5) >= 500:
            print("SuperToaster ist überhitzt, der Vorgang wird abgebrochen")
            sys.exit(0)
        else:
            return " "
