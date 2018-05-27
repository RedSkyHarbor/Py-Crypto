''' Fernet is AES128 in CBC mode with a SHA256 HMAC
It is therefore an implementation of symmetric authenticated cryptography 

'''

from cryptography.fernet import Fernet

key = Fernet.generate_key() # Keep it secret! Keep it safe!
fk = Fernet(key)

message = input("Enter your message: ")
b_message = message.encode('utf-8') # Convert to bytes

token = fk.encrypt(b_message)
d_token = fk.decrypt(token)

print("cyphertext:", token,  sep=' ')

print("plaintext:", fk.decrypt(token), sep=' ')
