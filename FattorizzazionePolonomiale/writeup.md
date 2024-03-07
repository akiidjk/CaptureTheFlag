## Title

Fattorizzazione Polinomiale

## Platform

Olicyber

## Url

https://training.olicyber.it/challenges#challenge-559

## Category

Crypto

## Difficult

Stupid

## Step

![alt text](image.png)


We have the cypher text [**3176847892201**] and the max secret value (**65536**)

So simple copy the script and brute force the x


## Solution

```Python
def decrypt(x):
    return (x-1)*(x**2+1)*(x-3)*(x+17)


def bruteforce_key(cypher_value:int,max:int) -> int:
    for i in range(max):
        if(decrypt(i) == cypher_value):
            return i

if __name__ == '__main__':
    cypher_value = 3176847892201
    secret_number = bruteforce_key(cypher_value=cypher_value,max=65536)
    print(f"The secret is: {secret_number}")

```
