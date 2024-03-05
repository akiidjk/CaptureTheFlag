### Title
Tu quoque lusor, me intelligis?

### Platform
Olicyber

### Url

https://training.olicyber.it/challenges#challenge-558

### Category

Cripto

### Difficult

Easy

### Step

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
The script use a caeser 

2. Now we have the cyper text: QSGOFSIGOJOIBQWTFOFWCGWAWZS and the script
3. Now we can try a bruteforce because the possible key are only 26 this because the assert in the script ```assert key < len(alphabet) and key > 0```


### Solution

```Python

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decrypt(plaintext, key):
	assert key < len(alphabet) and key > 0
	ciphertext = ""
	for c in plaintext:
		ciphertext += alphabet[(alphabet.index(c) - key) % 26] 

	return ciphertext


flag = "QSGOFSIGOJOIBQWTFOFWCGWAWZS"
for i in range(1,26):
    print(decrypt(flag,i))
    
```