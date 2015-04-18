from CipherInterface import Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

class RSA_433(Cipher):
    def setKey(self, key):
        try:
            self.key = open(key, "r").read()
            
            return True
        except ValueError:
            return False

    def encrypt(self, plaintext):

        rsakey = RSA.importKey(self.key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(plaintext)
        return encrypted.encode('base64')
        

    def decrypt(self, ciphertext):
 
        rsakey = RSA.importKey(self.key) 
        rsakey = PKCS1_OAEP.new(rsakey) 
        decrypted = rsakey.decrypt(b64decode(ciphertext)) 
        return decrypted
        #plaintext = 'NOT CODED'
        #return plaintext