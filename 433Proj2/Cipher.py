import sys
from DES_433 import DES_433
from RSA_433 import RSA_433


#Checks if input is valid
class InvalidArgument(Exception):
    def __init__(self, value):
        self.value = value #Set value
    def __str__(self):
        return repr(self.value)

def cipher():
    
    #Check if command is of length 6
    if len(sys.argv) < 6: 
        raise InvalidArgument(0)

    #Get commands needed to implement Cipher [DES/RSA] and [ENC/DEC]
    cipherName = sys.argv[1]
    key = sys.argv[2]
    mode = sys.argv[3]
    inputFileName = sys.argv[4] #Get file's needed to run implementation
    outputFileName = sys.argv[5]
    
    #Open file with text to encrypt
    inputFile = open(inputFileName, "r")
    inputFileContent = inputFile.read()
    inputFile.close()

    #Get file length
    inputSize = len(inputFileContent)
    cipher = None
    outputContent = ""

    #Implementation of DES cipher
    if(cipherName == 'DES'):
        cipher = DES_433() #Calling DES Cipher class
        if(len(inputFileContent)%8 != 0):
            inputFileContent = inputFileContent.ljust(inputSize+(8-inputSize%8),'0')
    elif(cipherName == 'RSA'): #Implementation of the RSA Cipher class
        cipher = RSA_433() #Calling RSA Cipher class
    else: # Unknown Cipher Method
        raise InvalidArgument(1)
    
    #Getting the cipher key
    if(cipher.setKey(key)): 
        if(mode == 'DEC'): #Implement decryption for given cipher
            outputContent = cipher.decrypt(inputFileContent)
        elif(mode == 'ENC'): #implement encryption for given cipher
            if(cipherName == 'DES'):
                #Set ciphertext
                for i in range(0, inputSize, 8):
                    outputContent = outputContent + cipher.encrypt(inputFileContent[i:i+8])
            else:
                outputContent = cipher.encrypt(inputFileContent) 
        else:
            raise InvalidArgument(2)

        print(outputContent)
        
        #Write ciphertext to specified file
        outputFile = open(outputFileName, 'w')
        outputFile.write(outputContent)
        outputFile.close()
        

    else:
        print('Invalid Key')

if __name__ == '__main__':
    try:
        cipher()
    except InvalidArgument as e:
        print('usage: cipher <CIPHER NAME> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>\n')
        if(e.value == 1):
            print('<CIPHER NAME>:')
            print('DES: DES technique')
            print('RSA: public-key encryption')
        elif(e.value == 2):
            print('<ENC/DEC>:')
            print('ENC: Encrypt')
            print('DEC: Decrypt')
    except IOError as e:
        print("A File error occured");
    except Exception as e:
        print(e.value)