import sys
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
            print("Es ist nur platz für " +str(remaining)+" Toasts")
            print("Toast Vorgang wird abgebrochen")
            sys.exit(0)
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
        return str(tmp)+" Toasts ausgeworfen, Toaster leer"

    def toast(self):
        if(self.toast_ammount == 0):
            return "Geht nicht, kein Toast drin."
        self.setState()
        return str(self.time)+" Sekunden vergangen, der Toast ist "+str(self.states[self.state])

    def __str__(self):
        res = "===== Toaster Objekt ==== \n"
        res += "Farbe: " + self.color + "\n"
        res += "Anzahl der Schächte: " + str(self.slots) + "\n"
        res += "Anzahl der Toasts im Toaster: " + str(self.toast_ammount) + "\n"
        res += "Toastzeit: " + str(self.time) + "\n"
        return res


