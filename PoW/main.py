from hashlib import sha256
from pwn import *
import re
from datetime import datetime as time

shas = {}

def precomputing(limit=500_000_000):
    for i in range(limit):
        comb = format(i, 'x').zfill(8)
        sha_digest = sha256(bytes.fromhex(comb)).hexdigest()
        shas[sha_digest[:6]] = comb
    print("File saved.")


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
                r.sendline(shas[number].encode())
    except:
        print("Not found")



if __name__ == '__main__':
    print("Computing")
    start = time.now()
    precomputing()
    end = time.now()
    print("Elapsed time: ", end - start)
    print("PWN")
    solve_pow_challange()