## Title

Base party

## Platform

Olicyber

## Url

https://training.olicyber.it/challenges#challenge-223

## Category

Misc

## Difficult

Easy/Medium


## Step

The ctf doesn't give us much information, just a file, the description and the title of the ctf, the title is 'Base Party' and the description tells us that 3 different encodings were used.

1. By analysing the file we immediately recognise a hex file.
2. The tool I recommend you use is [Cyberchef](https://gchq.github.io/CyberChef)
3. Once converted using hex deconding we notice that the text has been encoded with a base
4. Then trivially we start using all base decoders until we get valid output
5. And we repeat this step as soon as we find another valid base, the 64
6. We notice that we return a hex encoding and if we repeat the next steps then a base 32 and 64 decoding we notice that the text gets smaller and smaller until we find the flag


## Solution

In final the tool to use is this: [Final tool](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')From_Base32('A-Z2-7%3D',true)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9-_',true,false)From_Hex('None')From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9-_',true,false)From_Hex('None')From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9%2B/%3D',true,false))