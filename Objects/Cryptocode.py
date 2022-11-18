from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


# This is not my code.
# I'm only changed few parametrs for faster encryption.

def encrypt(message, password):
    plain_text = message
    salt = get_random_bytes(AES.block_size)
    private_key = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2 ** 2,
        r=1,
        p=1,
        dklen=16,
        )

    cipher_config = AES.new(private_key, AES.MODE_GCM)

    (cipher_text, tag) = \
        cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    encryptedDict = {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8'),
        }
    encryptedString = encryptedDict['cipher_text'] + '*' \
                      + encryptedDict['salt'] + '*' + encryptedDict[
                          'nonce'] + '*' \
                      + encryptedDict['tag']
    return encryptedString


def decrypt(enc_dict, password):
    enc_dict = enc_dict.split('*')
    try:
        enc_dict = {
            'cipher_text': enc_dict[0],
            'salt': enc_dict[1],
            'nonce': enc_dict[2],
            'tag': enc_dict[3],
            }

        salt = b64decode(enc_dict['salt'])
        cipher_text = b64decode(enc_dict['cipher_text'])
        nonce = b64decode(enc_dict['nonce'])
        tag = b64decode(enc_dict['tag'])

        private_key = hashlib.scrypt(
            password.encode(),
            salt=salt,
            n=2 ** 2,
            r=1,
            p=1,
            dklen=16,
            )

        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
    except:
        return False

    return decrypted.decode('UTF-8')
