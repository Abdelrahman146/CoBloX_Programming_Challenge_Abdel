from Library.crypto import private_key, public_key, hashing

if __name__ == '__main__':
    password = private_key.generate_password()
    private_key = private_key.generate_private_key_pem_string(password=password)
    public_key = public_key.generate_public_key_pem_string(private_key, password)
    print(private_key)
    print(hashing.hash(public_key))