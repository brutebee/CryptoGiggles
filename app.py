from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

class PasswordEncryptorDecryptor:
    SECRET_KEY = b'9c33e99e13a04579aa6e38ac28ca93ae' # Yes I know, there is a SECRET KEY HERE! Create your own, Alright!?

    @staticmethod
    def encrypt_password(password):
        if password is None:
            return None

        cipher = Cipher(
            algorithms.AES(PasswordEncryptorDecryptor.SECRET_KEY),
            modes.ECB(),
            backend=default_backend()
        )

        encryptor = cipher.encryptor()

        # Pad the data to be a multiple of the block size
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(password.encode('utf-8')) + padder.finalize()

        encrypted_password = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(encrypted_password).decode('utf-8')

    @staticmethod
    def decrypt_password(encrypted_password):
        if encrypted_password is None:
            return None

        cipher = Cipher(
            algorithms.AES(PasswordEncryptorDecryptor.SECRET_KEY),
            modes.ECB(),
            backend=default_backend()
        )

        decryptor = cipher.decryptor()

        decrypted_password = decryptor.update(base64.b64decode(encrypted_password.encode('utf-8'))) + decryptor.finalize()

       
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_password) + unpadder.finalize()

        return unpadded_data.decode('utf-8')

print("""
 _____                            _  ______ _       _     _   _ 
|  ___|                          | | | ___ (_)     | |   | | | |
| |__ _ __   ___ _ __ _   _ _ __ | |_| |_/ /_  __ _| |__ | |_| |
|  __| '_ \\ / __| '__| | | | '_ \\| __|    /| |/ _` | '_ \\| __| |
| |__| | | | (__| |  | |_| | |_) | |_| |\\ \\| | (_| | | | | |_|_|
\\____/_| |_|\\___|_|   \\__, | .__/ \\__\\_| \\_|_|\\__, |_| |_|\\__(_)
                       __/ | |                 __/ |            
                      |___/|_|                |___/             
""")

action = input("Type 'encrypt' or 'decrypt' and see the magic happens: ").lower()

if action == 'encrypt':
    password_to_encrypt = input("Type your password, it'll be encrypted: ")
    encrypted_password = PasswordEncryptorDecryptor.encrypt_password(password_to_encrypt)
    print("Encrypted Password:", encrypted_password)

elif action == 'decrypt':
    encrypted_password_to_decrypt = input("Type the encrypted password, it'll be decrypted: ")
    decrypted_password = PasswordEncryptorDecryptor.decrypt_password(encrypted_password_to_decrypt)
    print("Decrypted Password:", decrypted_password)

else:
    print("Invalid Option! you even know how to type'encrypt' ou 'decrypt'? or just know how to write Twitter posts?")
