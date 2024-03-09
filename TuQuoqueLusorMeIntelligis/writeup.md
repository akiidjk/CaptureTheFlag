## Title
Tu quoque lusor, me intelligis?

## Platform
Olicyber

## Url

https://training.olicyber.it/challenges#challenge-558

## Category

Cripto

## Difficult

Easy

## Step

1. Analyze the script

```Python

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(plaintext, key):
	assert key < len(alphabet) and key > 0
	ciphertext = ""
	for c in plaintext:
		ciphertext += alphabet[(alphabet.index(c) + key) % 26] 

	return ciphertext

```
The script uses a caeser 

2. Now we have the cypher text: QSGOFSIGOJOIBQWTFOFWCGWAWZS and the script
3. Now we can try a bruteforce because the possible keys are only 26, this is because the assert in the script is ```assert key < len(alphabet) and key > 0```.


## Solution

```Python

def decrypt(plaintext, key):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	assert key < len(alphabet) and key > 0
	ciphertext = ""
	for c in plaintext:
		ciphertext += alphabet[(alphabet.index(c) - key) % 26] 

	return ciphertext
        
if __name__ == '__main__':
	flag = "QSGOFSIGOJOIBQWTFOFWCGWAWZS" #Encrypt flag
	for i in range(1,26):
		flag  = decrypt(flag,i)
		if("CESARE" in flag):
			print(flag)
		
```