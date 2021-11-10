from base64 import b64decode, b64encode
from Crypto.Cipher import AES

input1=input("ENTER  KEY: ") # 32 byt key_size
key=str.encode(input1)
input2=input("ENTER IV: " )
iv=str.encode(input2)  #16 byte iv_size

def decrypt(data):
    aes = AES.new(key, AES.MODE_CFB, iv)
    encrypted = b64decode(data)
    decrypted = aes.decrypt(encrypted)
    return decrypted


input3 = input("ENTER CIPHERTEXT: ")
encrypted_message=str.encode(input3)

decrypted_message = decrypt(encrypted_message)
print("decrypted > {}".format(decrypted_message))


