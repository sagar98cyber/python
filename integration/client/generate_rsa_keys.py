# Program : Generate rsa keys
# Description : Allow to generate rsa keys
# Date : 29/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import rsa
from store_rsa_keys_in_files import store_rsa_keys_in_files


def generate_rsa_keys() -> tuple:
    public_key: rsa.key.PublicKey
    private_key: rsa.key.PrivateKey

    (public_key, private_key) = rsa.newkeys(1024)

    return public_key, private_key

(public_key, private_key) = generate_rsa_keys()

store_rsa_keys_in_files(private_key, public_key)
