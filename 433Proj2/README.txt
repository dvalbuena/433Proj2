– Names and email addresses of all partners.
Pete Chern <chernp@csu.fullerton.edu>,
Natally Santillan <nat1130@csu.fullerton.edu>,
Leslie Salguero <leslie.salguero93@gmail.com>,
Eduardo Rojas <eduardorojas@csu.fullerton.edu>
Denice Ron Valbuena <denice_valbuena@csu.fullerton.edu>

– The programming language you use (e.g. C++ or Java)
Programming Language used Python

– How to execute your program.
The user must enter the following requirements
<CIPHER NAME> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>
-CIPHER NAME  - name of the encryption technique
-KEY - the encryption key to use 
-ENC/DEC - whether to encrypt or decrypt, respectively
-INPUT FILE - the file from which to read th input
-OUTPUT FILE - the file to which to write the output

– Whether you implemented the extra credit.
Extra credit not implemented

– Anything special about your submission that we should take note of.
The python library use for encryption techniques are:

Crypto.PublicKey import RSA,
Crypto.Cipher import PKCS1_OAEP (use for padding),
base64 import b64decode (use for base64 encoded string),
Crypto.Cipher import DES

DES implementation was completed using the DES demo in class as a reference.
RSA implementation was completed using the following link as a reference:
https://launchkey.com/docs/api/encryption