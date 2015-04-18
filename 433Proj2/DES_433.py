from CipherInterface import Cipher
from Crypto.Cipher import DES

class DES_433(Cipher):
    def setKey(self, key):
        if(len(key) != 8):
            print("Key must be 8 bytes long")
            return False
        else:
            self.key = key
            return True

    def encrypt(self, plaintext):
        des = DES.new(self.key, DES.MODE_ECB)
        ciphertext = des.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        des = DES.new(self.key, DES.MODE_ECB)
        plaintext = des.decrypt(ciphertext)
        return plaintext