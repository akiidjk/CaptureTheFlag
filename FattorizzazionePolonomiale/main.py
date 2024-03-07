

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
