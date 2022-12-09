from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open('SEND_ME_BACK.txt', 'rb') as f:
    encryptedFernetKey = f.read()

private_key = RSA.import_key(open('private_key.pem').read())

# Private decrypter
privateDecrypter = PKCS1_OAEP.new(private_key)

# Decrypted session key
DecryptedFernetKey = privateDecrypter.decrypt(encryptedFernetKey)
with open('DESKTOP.txt', 'wb') as f:
    f.write(DecryptedFernetKey)
print('> Decryption Completed')

