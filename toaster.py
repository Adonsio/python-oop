class Toaster:

    def __init__(self, color, slots):
        self.color = color
        self.slots = slots
        self.time = 0
        self.state = 0
        self.toast_ammount = 0
        self.states = [
                'ungestoastet',
                'leicht getoastet',
                'stark getoastet',
                'verbrannt'
        ]

    def setState(self):
        if(self.time == 0):
            self.state = 0
        elif(self.time <= 15):
            self.state = 1
        elif(self.time > 15 and self.time <= 30):
            self.state = 2
        elif(self.time > 30):
            self.state = 3

    def insertToast(self, ammount):
        remaining = self.slots - self.toast_ammount
        if(ammount > remaining):
            return "Es ist nur platz für " +str(remaining)+" Toasts"
        else:        
            self.toast_ammount = ammount
            return str(ammount)+" Toasts wurden in den Toaster gesteckt"

    def changeTime(self, ammount):
        if((self.time + ammount) <= 0):
            self.time = 0
        else:
            self.time += ammount

    def ejectToast(self):
        tmp = self.toast_ammount
        self.toast_ammount = 0
        return str(tmp)+" Toasts azsgeworfen, Toaster leer"

    def canToast(self):
        return (self.toast_ammount > 0)

    def startToasting(self):
        if(self.toast_ammount == 0):
            return 
toastObject = Toaster('schwarz', 2)
print(toastObject.insertToast(2))
toastObject.changeTime(10)
toastObject.setState()
print(toastObject.states[toastObject.state])
toastObject.changeTime(2221)
toastObject.setState()
print(toastObject.canToast())