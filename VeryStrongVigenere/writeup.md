## Title

Very Strong Vigenere

## Platform
Olicyber

## Url

https://training.olicyber.it/challenges#challenge-80

## Category

Cripto

## Difficult

Easy

## Step

1. Download the cypher text and see the text
2. The outline blatantly refers to the [Vigenere cipher](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html), which I invite you to read and understand before solving the ctf 
3. There are two alternatives, either make a script that decrypts veginere or use an online tool I recommend [dCode](https://www.dcode.fr/vigenere-cipher)


## Solution


### Script try
To decrypt the flag there are two ways the first in the case of the use of the script is to guess that the key with which the flag was encrypted is too small and therefore try a bruteforce

### Tool try

If you prefer to use a tool, it is not enough to type the flag, you have to type a plaintext part into the prompt so that the tool can find the key and decode the flag... We only know that the pattern of the flag is flag{..}, so just type flag in the prompt and you will get the flag