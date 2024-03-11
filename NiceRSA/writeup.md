## Title

Nice RSA

## Platform
Olicyber

## Url

https://training.olicyber.it/challenges#challenge-78

## Category

Crypto

## Difficult

Medium (Just because you have to know the theory)

## Step

 - First read the code with which the flag was encrypted and we can see that as the trace says, it is a simple RSA 
 - One particular thing is the way in which p and q are generated in fact we can see that q is generated with the nextprime(p) function this makes the difference between the numbers very small and this will be our exploit

## Solution

Thanks to the small difference between the two numbers, we can factor N in spite of its large size in a very easy way with this function ```factorint(n)```. With this function we have the factorised of n and with p and q we can get the d to decrypt the message.

```Python
from sympy import factorint


if __name__ == '__main__':
    with open('./ct.txt','r') as file:
        content = file.read().split('\n')
        
    n = int(content[0].split('=')[-1])
    e = int(content[1].split('=')[-1])
    ct = int(content[2].split('=')[-1])

    p,q = factorint(n).keys()

    fi=(p-1)*(q-1)
    d=pow(e,-1,fi)

    decrypted = bytes.fromhex(hex(pow(ct, d, n))[2:]).decode()
    print(decrypted)
```