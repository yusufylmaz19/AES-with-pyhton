from base64 import b64decode, b64encode
from Crypto.Cipher import AES

input1=input("ENTER  KEY: ") # 32 byt key_size
key=str.encode(input1)
input2=input("ENTER IV: " )
iv=str.encode(input2)  #16 byte iv_size

def encrypt(text):
    aes = AES.new(key, AES.MODE_CFB, iv)
    encrypted = aes.encrypt(text)
    return b64encode(encrypted)


input3 = input("ENTER PLAINTEXT: ")
message=str.encode(input3)

encrypted_message = encrypt(message)
print("    encrypted > {}".format(encrypted_message))

