from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

key = open("pubkey.pem", "r").read()
rsakey = RSA.importKey(key)
rsakey = PKCS1_OAEP.new(rsakey)
encrypted = rsakey.encrypt("whatthefuck!!")
package = encrypted.encode('base64')
print encrypted.encode('base64')

key2 = open("privkey.pem", "r").read() 
rsakey2 = RSA.importKey(key2) 
rsakey2 = PKCS1_OAEP.new(rsakey2) 
decrypted = rsakey2.decrypt(b64decode(package)) 
print decrypted