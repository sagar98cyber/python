# Program : Decrypt files
# Description : Allow to decrypt file encrypted with the RSA key
# Date : 29/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import rsa
from read_bytes_of_file import read_bytes_of_file
from get_rsa_keys import get_rsa_keys
from write_on_file import write_on_file


def decrypt(ciphertext: bytes, private_key: rsa.key.PrivateKey) -> bytes:
    try:
        print("decrypted")
        return rsa.decrypt(ciphertext, private_key)

    except:
        print("decryption failed")
        return False