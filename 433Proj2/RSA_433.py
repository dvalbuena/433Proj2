from CipherInterface import Cipher
from Crypto.Cipher import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

class RSA_433(Cipher):
    def setKey(self, key):
        try:
            self.key = key
            if(key == 'privkey.pem'):
	            keyFile = open(key,"r")
	            privKey = keyFile.read()
	            keyFile.close()
            	return True
            elif(key == 'pubkey.pem'):
            	keyFile = open(key,"r")
	            pubKey = keyFile.read()
	            keyFile.close()
            	return True
        except ValueError:
            return False

    def encrypt(self, plaintext):
        '''ey = open(public_key_loc, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(message)
        return encrypted.encode('base64')'''
        
        key = open(self.key, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(message)
        return encrypted.encode('base64')
        

    def decrypt(self, ciphertext):
        '''from Crypto.PublicKey import RSA 
        from Crypto.Cipher import PKCS1_OAEP 
        from base64 import b64decode 
        key = open(private_key_loc, "r").read() 
        rsakey = RSA.importKey(key) 
        rsakey = PKCS1_OAEP.new(rsakey) 
        decrypted = rsakey.decrypt(b64decode(package)) 
        return decrypted'''
        
        plaintext = 'NOT CODED'
        return plaintext