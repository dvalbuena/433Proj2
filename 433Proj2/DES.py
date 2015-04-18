from CipherInterface import Cipher
from Crypto.Cipher import DES

class DES_433(Cipher):
    def setKey(self, key):
        try:
            self.key = int(key)
            '''
            
            '''
            return True
        except ValueError:
            return False

    def encrypt(self, plaintext):
        des = DES.new(self.key, DES.MODE_ECB)
        ciphertext = des.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        des = DES.new(self.key, DES.MODE_ECB)
        plaintext = des.decrypt(ciphertext)
        return plaintext