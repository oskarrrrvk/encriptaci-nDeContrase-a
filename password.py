from OpenSSL import crypto 
import random


def takePassContent():
    option = "si"
    passwordElements = []
    while option[0].lower() != "n":
        passwordElements.append(input("introduzca una palabra cualquiera:\n\t>"))
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

def makePrivateKey():
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA,2048)
    return key

def makeCertificate(key):
    csr = crypto.X509()
    csr.get_subject().C = input("País <Las dos primeras letras>: ")
    csr.get_subject().ST = input("Estado / Provincia / Comunidad_Autónoma: ")
    csr.get_subject().L = input("Localización: ")
    csr.get_subject().O = input("Organización: ")

    csr.set_serial_number(random.randint(1024,66536))
    csr.gmtime_adj_notBefore(0)
    csr.gmtime_adj_notAfter(93 * 24 * 60 * 60)
    csr.set_issuer(csr.get_subject())
    csr.set_pubkey(key)
    csr.sign(key, 'sha256')
    publicKey = csr.get_pubkey()
    return csr, publicKey

def savePrivateKey(privateKey):
    with open("clavePrivada","wb") as file:
        file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, privateKey))

def savePublicKey(publicKey):
    with open("clavePublica","wb") as file:
        file.write(crypto.dump_publickey(crypto.FILETYPE_PEM, publicKey))

def saveCertificate(csr):
    with open("certificado.csr", "wb") as file:
        file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, csr))


def cryptPasswrd(password,publicKey):
    return

def signPasswrd(password, privateKey):
    #crypto.sign(privateKey,)
    return 

elementsPassword = takePassContent()
password = createPassword(elementsPassword)
privateKey = makePrivateKey()
csr,publickey = makeCertificate(privateKey)
savePrivateKey(privateKey)
savePublicKey(publickey)
saveCertificate(csr)
