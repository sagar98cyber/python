import rsa
from generate_rsa_keys import generate_rsa_keys
from store_rsa_keys_in_files import store_rsa_keys_in_files
from get_rsa_keys import get_rsa_keys
from encrypt import  encrypt
from decrypt import decrypt
from read_bytes_of_file import read_bytes_of_file
from write_on_file import write_on_file

def keyGeneration():
    private_key: rsa.key.PrivateKey
    public_key: rsa.key.PublicKey
    (public_key, private_key) = generate_rsa_keys()
    store_rsa_keys_in_files(private_key, public_key)

def encryption(file_to_read):
    normal_message: bytes = read_bytes_of_file(file_to_read)
    encrypted_message: bytes
    decrypted_message: bytes
    (private_key, public_key) = get_rsa_keys()
    encrypted_message = encrypt(normal_message, public_key)
    write_on_file('file_to_write_on.txt', encrypted_message)
    return True

def decryption():
    (private_key, public_key) = get_rsa_keys()
    encrypted_message = read_bytes_of_file('file_to_write_on.txt')
    decrypted_message = decrypt(encrypted_message, private_key)
    write_on_file('decrypted_file.txt', decrypted_message)

