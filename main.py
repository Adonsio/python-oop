from Toaster import *
from SuperToaster import *
def main():
    toasterObject = SuperToaster('Grün', 2)
    print(toasterObject)

    time = int(input("Bitte Toastzeit eingeben: "))
    toasterObject.changeTime(time)

    ammount = int(input("Bitte Anzahl der Toasts eingeben: "))
    print(toasterObject.insertToast(ammount))

    print("Toastvorgang wird gestartet..")

    # check if object is a SuperToaster
    if(type(toasterObject) is SuperToaster):
        print(toasterObject.calcTemp())
    print(toasterObject.toast())

    print("\nErgebnisse: \n")
    print(toasterObject)


if __name__ == "__main__":
    main()