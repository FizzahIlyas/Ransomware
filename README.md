# Ransomware
PROJECT MANUAL

1.	The script ‘PublicPrivate.py’ is run on the command prompt which generates 
	two asymmetric keys using functions of public key and private key encryption 
	in the RSA library. 

2.	Run the Ransomware.py’ on the attacker command terminal which will encrypt all 
	the target files on the path given. The generate key function in the main file 
	which encrypts and decrypts the fernet key. This is done by using fernet from
 	the cryptography fernet library. The key generation function will create a fernet
 	encryption and decryption object. The script encrypts all the files with fernet key.
 	Now the fernet key is encrypted using the public key. A popup will open in the 
	browser asking for a ransom.

3.	The scriptwill then place an attacker’s note for the ransom on the target
	machine in the form of a documentalong with the unencrypted fernet key.
 
4.	After the ransom is paid the private key will be received. After placing 
	that document containing the key on the desktop, the encrypted fernet key will
 	be decrypted. Eventually, this key will unencrypt all the files on the target 
	system. 

