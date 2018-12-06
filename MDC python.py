#python 2.7.12

def mdc(a, b):
    return a if not b else mdc(b, a % b)

print(mdc(7, 5)) 

