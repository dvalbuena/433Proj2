import sys
from DES import DES
from RSA import RSA



class InvalidArgument(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def cipher():
    if len(sys.argv) < 6:
        raise InvalidArgument(0)

    cipherName = sys.argv[1]
    # Key can span mulitple arguments
    # Example: cipher RTS 4 3 1 2 ENC small.txt output.txt
    # In the example the key would be 4 3 1 2
    key = " ".join(sys.argv[2:len(sys.argv) - 3])
    mode = sys.argv[len(sys.argv) - 3] # Thrid to last argument
    inputFileName = sys.argv[len(sys.argv) - 2] # Second to last
    outputFileName = sys.argv[len(sys.argv) - 1] # Last 
    
    inputFile = open(inputFileName, "r")
    inputFileContent = inputFile.read()
    inputFile.close()

    # inputFileContent = "meetmeafterthetogaparty"

    cipher = None

    if(cipherName == 'DES'):
        cipher = DES()
    elif(cipherName == 'RSA'):
        cipher = RSA()
    else: # Unknown Cipher Method
        raise InvalidArgument(1)
    
    if(cipher.setKey(key)):
        if(mode == 'DEC'):
            outputContent = cipher.decrypt(inputFileContent)
        elif(mode == 'ENC'):
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