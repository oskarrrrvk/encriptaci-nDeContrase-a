from OpenSSL import crypto 
import random


def takePassContent():
    option = "si"
    passwordElements = []
    while option[0].lower() != "n":
        passwordElements.append(input("introduzca una palabra cualquiera:\n\t"))
        option = input("quiere introducir otra palabra S/N: ")
    return passwordElements

def takeletters(passwrdElements):
    letters = ""
    for element in passwrdElements:
        for i in range (random.randint(0,len(element) - 1)):
            letters += element[random.randint(0,len(element) -1)]
    return letters

def takenumbers(letters):
    password = ""
    for letter in letters:
        password += str(random.randint(0,9))+ letter
    return password

def createPassword(passwrdElements):
    return takenumbers(takeletters(passwrdElements))

def makeKey():
    key = crypto.PKey()
    return key.generate_key(crypto.TYPE_RSA,2048)

def cryptPasswrd(password,key):
    return

elementsPassword = takePassContent()
print(elementsPassword)
password = createPassword(elementsPassword)
print(password)
