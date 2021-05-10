""" 
    This Script would contain Hash functions, Cryptographic algorithms 
    and lots more
"""

import hashlib, binascii
from decouple import config
import random
import string

def plain_sha_hasher(data):
    """ 
        This function would receive data(string) as it parameter and hash it
    """

    PLAIN_SALT = config("__PLAIN_SALT__").encode()

    the_hash = hashlib.pbkdf2_hmac("sha256", password=data.encode(), salt=PLAIN_SALT, iterations=100000)
    the_hash_hex = binascii.hexlify(the_hash)

    return the_hash_hex

    


def plain_sha_decoder(encoded_string, raw_data):
    """ 
        This function would decode the hash done by the first plain haser function
    """
    validation_hash = plain_sha_hasher(raw_data)

    if (validation_hash == encoded_string.encode()):
        return True
    else:
        print(validation_hash, encoded_string)

    


def coin_data_hasher(coin_data):
    """ 
        This function would recieve the coin data as it parameter
        and create a SHA256 hash specifically encoded for the coin
        data hash
    """

    COIN_HASH_SALT = config("__COIN_SALT__").encode()

    the_coin_hash = hashlib.pbkdf2_hmac("sha256", password=coin_data.encode(), salt=COIN_HASH_SALT, iterations=100000)
    the_coin_hash_hex = binascii.hexlify(the_coin_hash)

    return the_coin_hash_hex



def validate_coin_data_hash(encoded_string, raw_string):
    """ 
        This function would validate the hash against what is suppose to be
    """

    validation_coin_hash = coin_data_hasher(raw_string)

    if (validation_coin_hash == encoded_string.encode()):
        return True
    else:
        print(validation_coin_hash, encoded_string)


def generate_random_id():
    base_string = "".join(random.choices(string.ascii_uppercase + string.digits, k=32))

    COIN_HASH_SALT = config("__COIN_SALT__").encode()

    random_hashed = hashlib.pbkdf2_hmac("sha256", password=base_string.encode(), salt=COIN_HASH_SALT, iterations=100000)
    random_hashed_hex = binascii.hexlify(random_hashed)
    random_hashed_hex = random_hashed_hex.decode()

    return random_hashed_hex

def generate_block_hash(string_to_hash):
    BLOCK_HASH_SALT = config("__BLOCK__SALT__").encode()

    block_hash = hashlib.pbkdf2_hmac("sha256", password=string_to_hash.encode(), salt=BLOCK_HASH_SALT, iterations=100000)
    block_hash_hex = binascii.hexlify(block_hash)

    return block_hash_hex

def validate_block_hash(raw_string, hashed_string):
    validation_block_hash = generate_block_hash(raw_string)

    if (validation_block_hash == encoded_string.encode()):
        return True
    else:
        print(validation_block_hash, encoded_string)
