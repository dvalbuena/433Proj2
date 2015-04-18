from CipherInterface import Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

class RSA_433(Cipher):
    def setKey(self, key):
        try:
            self.key = key
        
            key = open(self.key, "r").read()
            
            return True
        except ValueError:
            return False

    def encrypt(key, plaintext):
        '''ey = open(public_key_loc, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(message)
        return encrypted.encode('base64')'''
        
        #key = open(self.key, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(plaintext)
        return ''.join(encrypted.encode('base64'))
        

    def decrypt(key, ciphertext):
        '''from Crypto.PublicKey import RSA 
        from Crypto.Cipher import PKCS1_OAEP 
        from base64 import b64decode 
        key = open(private_key_loc, "r").read() 
        rsakey = RSA.importKey(key) 
        rsakey = PKCS1_OAEP.new(rsakey) 
        decrypted = rsakey.decrypt(b64decode(package)) 
        return decrypted'''
        
        
        #key2 = open("privkey.pem", "r").read() 
        rsakey = RSA.importKey(key) 
        rsakey = PKCS1_OAEP.new(rsakey) 
        decrypted = rsakey2.decrypt(b64decode(ciphertext)) 
        return ''.join(decrypted)
        #plaintext = 'NOT CODED'
        #return plaintext