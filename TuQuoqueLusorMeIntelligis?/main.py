


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
		