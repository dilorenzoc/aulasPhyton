n=int(input('Digite um numero'))

def decPbin(n):
    b = []
    while n != 0:
        b.append(str(n % 2))
        n = int(n / 2)
    return b[::-1]
    
print(decPbin(n))

