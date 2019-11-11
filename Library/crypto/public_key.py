from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from Library.crypto.private_key import load_private_key
import codecs


###################################################################
# Public Key functions
# def generate_public_key(private) generates a public key from a private key
# def generate_public_key_pem(public_key) generates a public pem
# def generate_public_key_pem_string(private_key_pem_string, password) extract private key from private
# key pem string then generate a public key then generate a public key pem then decode it.
# def load_public_key(public_key_pem) extract public key from public key pem
# def verify_signature(public_key_pem_string, signature, message) extracts public key from pem and
# verify the signature and the message are correct
###################################################################

# generate public key
def generate_public_key(private_key):
    return private_key.public_key()


# generate public pem
def generate_public_key_pem(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


# generate a string for the public pem
def generate_public_key_pem_string(private_key_pem_string, password):
    private_key = load_private_key(
        private_key_pem_string.encode('utf-8'),
        password.encode('utf-8')
    )
    public_key = generate_public_key(private_key)
    return generate_public_key_pem(public_key).decode()


# load public key from public pem
def load_public_key(public_key_pem):
    return serialization.load_pem_public_key(
        public_key_pem,
        backend=default_backend()
    )


# verify a signature
def verify_signature(public_key_pem_string, signature, message):
    public_key = load_public_key(public_key_pem_string.encode('utf-8'))
    signature_binary = codecs.decode(signature.encode('utf-8'), 'base64')
    return verify_binary(public_key, signature_binary, message.encode('utf-8'))


def verify_binary(public_key, signature, message_binary):
    try:
        verify = public_key.verify(
            signature,
            message_binary,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA3_256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA3_256()
        )
    except InvalidSignature:
        return False
    return True
