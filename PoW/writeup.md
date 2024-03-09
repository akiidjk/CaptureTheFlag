## Title

PoW

## Platform
Olicyber

## Url

https://training.olicyber.it/challenges#challenge-275

## Category

Misc

## Difficult

Medium

## Step

1. This CTF is particular this because it is a [proof of work](https://en.wikipedia.org/wiki/Proof_of_work) so it requires a lot of computation and good scripting
2. Initially, we need to understand what the ctf requires, and we can see that the requirement is: ```Give me x so that sha256(bytes.fromhex(x)) starts with c094b6```
3. So the aim is to find an X, which in our case are bytes written in hexadecimal, to which a SHA256 must be applied, and where the first 6 characters or 3 bytes begin with the string that the script gives us
4. This will unfortunately be asked several times and this is a problem because the more times we are asked, the more computation and data we should have.


## Solution

The initial idea I had, when I was unaware that it was more than one request, was to calculate the hash each time, find it and send it once found, and since the script has a timeout already after the second request, the time would expire or in a range of 16^8 it would not find a combination that respected the hash.

After several studies, I came up with the idea of using a kind of [Rainbow Table](https://en.wikipedia.org/wiki/Rainbow_table), i.e. a kind of precomputed table that allows us to pre-calculate all possible values 

But to do this we need computing power and time and find the right compressed time and data, in my case 500_000_000 combinations and about 25 minutes of time were needed (*I came to this conclusion after doing some tests and increasing the maximum value *)

In the end the final script is this but I think it can be improved considerably



```Python

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

```
