

def decrypt(x):
    return (x-1)*(x**2+1)*(x-3)*(x+17)


cypher_value = 3176847892201
for i in range(65536):
    if(decrypt(i) == cypher_value):
        print(f"The secret is: {i}")
