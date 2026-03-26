import time

def entrada(n):
    t=['int','id']
    for _ in range(n-1):
        t += [',','id']
    t.append(';')
    return t

def cyk(t):
    n=len(t)
    lex={'int':{'T'},'float':{'T'},'id':{'I'},',':{'C'},';':{'L'}}
    reglas={('T','X'):{'D'},('I','L'):{'X'},('C','X'):{'L'}}

    m=[[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i].update(lex.get(t[i],set()))

    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            for k in range(i,j):
                for a in m[i][k]:
                    for b in m[k+1][j]:
                        m[i][j].update(reglas.get((a,b),set()))

    return 'D' in m[0][n-1]

def lineal(t):
    i=0
    if t[i] not in ['int','float']:
        return False
    i+=1

    if t[i]!='id':
        return False
    i+=1

    while t[i]==',':
        i+=1
        if t[i]!='id':
            return False
        i+=1

    return t[i]==';'

def test(n):
    t=entrada(n)

    a=time.time()
    cyk(t)
    b=time.time()

    lineal(t)
    c=time.time()

    print(f"{n} ids")
    print("cadena:", " ".join(t))
    print("CYK:", b-a)
    print("Lineal:", c-b)
    print()

for i in [5,10,20,40]:
    test(i)
