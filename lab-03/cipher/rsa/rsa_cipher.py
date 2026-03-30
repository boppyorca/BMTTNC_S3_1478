import rsa
import os

class RSACipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')
        
    def generate_keys(self):
        public_key, private_key = rsa.newkeys(1024)
        with open(os.path.join(self.keys_dir, 'publicKey.pem'), 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open(os.path.join(self.keys_dir, 'privateKey.pem'), 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open(os.path.join(self.keys_dir, 'publicKey.pem'), 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open(os.path.join(self.keys_dir, 'privateKey.pem'), 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)
    
    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode('utf-8')

    def sign(self, message, private_key):
        return rsa.sign(message.encode('utf-8'), private_key, 'SHA-256')

    def verify(self, message, signature, public_key):
        try:
            rsa.verify(message.encode('utf-8'), signature, public_key)
            return True
        except rsa.VerificationError:
            return False
