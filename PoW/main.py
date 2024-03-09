from hashlib import sha256
from pwn import *
import json
import re


shas = {}
def precomputing():
    for j in range(2,10,2):
        print(f"Digit {j}")
        for i in range(16**j):
            comb = format(i, f'0{j}x')
            sha_digest = sha256(bytes.fromhex(comb)).hexdigest()
            shas[sha_digest[:6]] = comb
    with open("numbers.json","w") as f:
        json.dump(shas,f,indent=4)

# print(shas)


def solve_pow_challange():
    try:
        r = remote("pow.challs.olicyber.it", 12209)
        while True:
            question = r.recvline().decode()
            print(question)
            if 'flag' in question:
                print(question)
                break
            match = re.search(r'\b([0-9a-fA-F]+)\b', question)
            if match:
                number = match.group(1)
                print(f"Received number: {number}")
                r.sendline(shas[number])
    except:
        solve_pow_challange()



if __name__ == '__main__':
    # print("calcolo")
    # precomputing()
    with open('numbers.json',"r") as f:
        shas = json.load(f)
    print("PWN")
    solve_pow_challange()
