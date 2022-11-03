from cryptography.fernet import Fernet
from  app.constants_file import Constants

class Encryption():
    """Encryption for encrypt password or whatever string."""
    @staticmethod
    def get_key():
        return Constants.key_encryption

    @staticmethod
    def encrypt_value(ciphertext):
        """ Method encrypt values """
        try:
            key = Encryption.get_key().encode()
            data = ciphertext.encode()
            fernet = Fernet(key)
            value_encrypt = fernet.encrypt(data)
        except Exception as exception:
            print(exception.args[0])
                                         
        return value_encrypt
    
    @staticmethod
    def decrypt_value(ciphertext):
        """ Method encrypt values """
        try:
            key = Encryption.get_key().encode()
            data = ciphertext.encode()
            fernet = Fernet(key)
            value_encrypt = fernet.decrypt(data)
        except Exception as exception:
            print(exception.args[0])
        return value_encrypt