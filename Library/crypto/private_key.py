from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import codecs
import os


###################################################################
# Private_key functions
# def generate_password() generates a password for the private key
# def generate_private_key() generates a private key
# def generate_private_key_pem(private_key) generates a private pem
# def generate_private_key_pem_string(password) generates a private key then
# generates a private key pem and returns private_key_pem_string
# def load_private_key(private_key_pem) encode the private key pem string
# and extracts the private key from private_key_pem
# def sign(private_key_pem_string, msg) extracts private_key and return a signature for the message
###################################################################


# generate a new password
def generate_password():
    randomness = os.urandom(64)
    return codecs.encode(randomness, 'base64').decode()


# generate a private key
def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )


# generate private key pem
def generate_private_key_pem(private_key, password):
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password=password)
    )


# generate a private key pem string
def generate_private_key_pem_string(password):
    private_key = generate_private_key()
    private_key_pem = generate_private_key_pem(private_key, password.encode('utf-8'))
    return private_key_pem.decode()


# loads private key from a private_key_pem_string
def load_private_key(private_key_pem, password):
    return serialization.load_pem_private_key(
        private_key_pem,
        password=password,
        backend=default_backend()
    )


# sign a message
def sign(private_key_pem_string, password, message):
    private_key = load_private_key(
        private_key_pem_string.encode('utf-8'),
        password.encode('utf-8')
    )
    signature = sign_binary(private_key, message.encode('utf-8'))
    return codecs.encode(signature, 'base64').decode()


def sign_binary(private_key, message_binary):
    type(message_binary)
    signature = private_key.sign(
        message_binary,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA3_256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA3_256()
    )
    return signature
