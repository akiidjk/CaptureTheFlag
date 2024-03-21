from random import randint
from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from sympy import factorint

def swap(n, p1, p2):
    s = [x for x in str(n)]
    s[p1], s[p2] = s[p2], s[p1]
    return int(''.join(s))

p = getPrime(1024)
q = 1

print("P (partenza): ",p)
print("l: ",len(str(p)))
while not isPrime(q) or p == q: #Condizione di uscita è che q e p devono essere diversi e q deve essere primo
    l = len(str(p)) #Parte sempre da 309
    a, b = randint(1,l-2), randint(1,l-2) # genera un numero random da 1 a 307
    q = swap(p, a, b)

print("P: ", p, "\nQ: ",q)
n = 9700624973335227055834821387578165820987729817710621527082447155621161414295958099546312097933523578863057993140379629780916269670655470321976734594875144696433530227361137525650790448084448289047204800420531636552990768244095520038285748691537342063595688661621589282117407882397058048167638703912241478051849281193195487402061635333315670227116368030820989272197103085229555972573665288381582068869270978768295751239967706497051433039255249462088379725705374118278747647279659599170149326364777103028984912684556440494924611905789226845891638154706316392010947789075975455446965196233425530921819310799161323107809
p,q = factorint(n).keys()

print(p,q)
q = str(q)
p = str(p)
c = 0
for i in range(len(p)):
    if(p[i] == q[i]):
        c = c + 1
    else:
        print("Carattere diverso numero: ", i)
print(c)   

flag = b"Ciao"

# n = p*q
# e = 65537
# m = bytes_to_long(flag)

# print(f"n = {n}")
# print(f"enc = {pow(m,e,n)}")
