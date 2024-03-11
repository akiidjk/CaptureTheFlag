import string
from hashlib import sha256

alphabet = string.ascii_letters + string.digits + "{"+"}"
print(alphabet)
flag = ''

with open('./ILikeHashes/ctx.txt') as f:
    for i in range(33):
        h = f.readline().strip()
        print(h)
        
        for letter in alphabet:
            if sha256(letter.encode()).hexdigest() == h:
                flag += letter
                break
        else:
            flag += "_"

print(flag)
