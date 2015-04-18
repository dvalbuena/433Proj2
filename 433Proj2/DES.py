from CipherInterface import Cipher

class DES(Cipher):
    def setKey(self, key):
        try:
            self.key = int(key)
            return True
        except ValueError:
            return False

    def encrypt(self, plaintext):
        ciphertext = 'NOT CODED'
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = 'NOT CODED'
        return plaintext