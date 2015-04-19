from CipherInterface import Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

class RSA_433(Cipher):
    def setKey(self, key): 
        try:
            #Get the key, either pubKey.pem or privKey.pem and read it
            self.key = open(key, "r").read()
            
            return True
            
            #If not pubKey.pem or privKey.pem then return false
        except ValueError:
            return False

    def encrypt(self, plaintext):

        rsakey = RSA.importKey(self.key) #Get pubKey.pem 
        rsakey = PKCS1_OAEP.new(rsakey)  #Set the key
        encrypted = rsakey.encrypt(plaintext) #Encrypt the plaintext with the public key
        return encrypted.encode('base64') #Return as an encode version
        

    def decrypt(self, ciphertext):
 
        rsakey = RSA.importKey(self.key)  #Get the privKey.pem
        rsakey = PKCS1_OAEP.new(rsakey)   #Set the key
        decrypted = rsakey.decrypt(b64decode(ciphertext)) #Decrypt the ciphertext using the private key 
        return decrypted #Returns the plaintext 
        #plaintext = 'NOT CODED'
        #return plaintext