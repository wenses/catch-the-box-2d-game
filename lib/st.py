import rsa

k1,k2=rsa.newkeys(1024)

k1_filedata=rsa.PublicKey._save_pkcs1_pem(k1)
k2_filedata=rsa.PrivateKey._save_pkcs1_pem(k2)
file1=open('publickey.pem','wb').write(k1_filedata)
file2=open('privatekey.pem','wb').write(k2_filedata)

print('keys generated and saved successfully')

#plain=input('enter word to encrypt:')
plain='cybermaster'
ciphered=rsa.encrypt(plain.encode(),k1)
print(f'RSA ENCRYPTION OF {plain} --> {ciphered.hex()}')

deciphered=rsa.decrypt(ciphered.hex().encode(),k2)
print(deciphered)
