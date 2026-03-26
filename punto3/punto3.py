g1 = """Gramatica 1: Asociatividad izquierda
E -> E op T | T
T -> num
op -> + | - | * | /
"""

g2 = """Gramatica 2: Asociatividad derecha
E -> T op E | T
T -> num
op -> + | - | * | /
"""

g3 = """Gramatica 3: Precedencia normal
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> num | (E)
"""

g4 = """Gramatica 4: Precedencia inversa
E -> E * T | E / T | T
T -> T + F | T - F | F
F -> num | (E)
"""

def izq(t):
    r=int(t[0]); i=1
    while i<len(t):
        op=t[i]; n=int(t[i+1])
        if op=='+': r+=n
        elif op=='-': r-=n
        elif op=='*': r*=n
        elif op=='/': r/=n
        i+=2
    return r

def der(t):
    def f(i):
        if i==len(t)-1:
            return int(t[i])
        a=int(t[i])
        op=t[i+1]
        b=f(i+2)
        if op=='+': return a+b
        if op=='-': return a-b
        if op=='*': return a*b
        if op=='/': return a/b
    return f(0)

def prec(t,ops):
    t=t[:]
    while len(t)>1:
        for i in range(1,len(t),2):
            if t[i] in ops:
                a=float(t[i-1]); b=float(t[i+1])
                if t[i]=='+': r=a+b
                elif t[i]=='-': r=a-b
                elif t[i]=='*': r=a*b
                else: r=a/b
                t=t[:i-1]+[str(r)]+t[i+2:]
                break
        else:
            ops=['+','-','*','/']
    return float(t[0])

def probar(e):
    t=e.split()
    print("expresion:",e)
    print("g1:",izq(t))
    print("g2:",der(t))
    print("g3:",prec(t,['*','/']))
    print("g4:",prec(t,['+','-']))
    print()

print(g1)
print(g2)
print(g3)
print(g4)

probar("4 - 3 - 2")
probar("2 + 3 * 4")
