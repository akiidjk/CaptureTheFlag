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