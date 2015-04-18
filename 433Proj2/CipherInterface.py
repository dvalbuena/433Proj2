from abc import ABCMeta, abstractmethod

class Cipher(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setKey(self, key): 
        self.key = key

    @abstractmethod
    def encrypt(self, plaintext): pass

    @abstractmethod
    def decrypt(self, ciphertext): pass