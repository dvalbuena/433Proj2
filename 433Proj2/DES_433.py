from CipherInterface import Cipher
from Crypto.Cipher import DES

class DES_433(Cipher):
    def setKey(self, key):
        
        #Check to see if the given key is 8 bytes long
        if(len(key) != 8):
            #If it's not notify the user
            print("Key must be 8 bytes long")
            return False
        else:
            #If the key is 8 bytes long set the key
            self.key = key
            return True

    def encrypt(self, plaintext):
        des = DES.new(self.key, DES.MODE_ECB) #Create a new DES cipher with the given key
        ciphertext = des.encrypt(plaintext) #Encrypt the plaintext
        return ciphertext #Return the given plaintext as encryption 

    def decrypt(self, ciphertext):
        des = DES.new(self.key, DES.MODE_ECB) #Create a new DES cipher with the given key
        plaintext = des.decrypt(ciphertext) #Decrypt it using key and the DES cipher block
        return plaintext #Returns the plaintext