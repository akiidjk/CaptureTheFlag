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
