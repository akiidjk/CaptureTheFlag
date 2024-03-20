from base64 import b64encode, b64decode
from pwn import *

from AESFLIPPER import Aesflipper

enc_base64 = "4bEPJBge2NKncgt/74V4kfh4PReBc56MSegFTmt6rJA2oclTm9zvARke4jOUkdfG"

enc_hex = ''.join(format(byte, '02x') for byte in b64decode(enc_base64)).encode()

plaintext = b'{"admin": false, "msg": "Dammi la flaaag!"}'
target = b'{"admin": true , "msg": "Dammi la flaaag!"}'

print(len(plaintext))
print(len(target))

flipper = Aesflipper(
    plain=plaintext,
    ciphertext=enc_hex,
    # add_iv=True,
    debug=True
)
token = flipper.full_flip(target=target)

# Converti il risultato in base64 (come nel tuo codice originale)
result_base64 = b64encode(bytes.fromhex(token.decode())).decode()
print(result_base64)



# def crypto(msg,IV):
#     plaintext = json.dumps({'admin': True, 'msg': msg}).encode()
#     cipher = AES.new(key, AES.MODE_CBC, IV)
#     ciphertext = cipher.encrypt(pad(plaintext, 16))
#     return ciphertext 

# r = connect('flip.challs.olicyber.it',10603)
# r.recvline_endswith(b'!!!')
# r.sendline(b'1')
# r.sendline(b'a')
# IV = b64decode(r.recvline_contains(b'IV').decode().split('IV: ')[-1][:-1])
# print(IV)
# msg = "Dammi la flaaag!"
# result = crypto("Dammi la flaaag!",IV)
# print(result)



