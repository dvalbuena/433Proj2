import sys
from DES import DES
from RSA_433 import RSA_433



class InvalidArgument(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def cipher():
    if len(sys.argv) < 6:
        raise InvalidArgument(0)

    cipherName = sys.argv[1]
    key = sys.argv[2]
    mode = sys.argv[3]
    inputFileName = sys.argv[4]
    outputFileName = sys.argv[5]
    
    inputFile = open(inputFileName, "r")
    inputFileContent = inputFile.read()
    inputFile.close()

    inputSize = len(inputFileContent)
    cipher = None

    if(cipherName == 'DES'):
        cipher = DES()
        if(len(inputFileContent)%8 != 0):
            inputFileContent.ljust(inputSize+(8-inputSize%8),'0')
    elif(cipherName == 'RSA'):
        cipher = RSA_433()
    else: # Unknown Cipher Method
        raise InvalidArgument(1)
    
    if(cipher.setKey(key)):
        if(mode == 'DEC'):
            outputContent = cipher.decrypt(inputFileContent)
        elif(mode == 'ENC'):
            if(cipherName == 'DES'):
                for i in range(0, inputSize, 8):
                    outputContent = outputContent + cipher.encrypt(inputFileContent[i:i+8])
            else:
                outputContent = cipher.encrypt(inputFileContent)
        else:
            raise InvalidArgument(2)

        print(outputContent)

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
    except FileNotFoundError as e:
        print(e.filename + ' was not found')
    except Exception as e:
        print(e.value)