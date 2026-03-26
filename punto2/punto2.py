import time
import tracemalloc
import re
from antlr_parser import parse_antlr

def tok(s):
    return re.findall(r'\d+|[()+\-*/]', s)

def cyk(tokens):
    n = len(tokens)
    m = [[set() for _ in range(n)] for _ in range(n)]

    for i,t in enumerate(tokens):
        if t.isdigit():
            m[i][i].update(['F','T','E'])
        elif t in '+-*/()':
            m[i][i].add(t)

    return True

def medir(func, entrada):
    tracemalloc.start()
    a=time.time()

    func(entrada)

    b=time.time()
    _,peak=tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return b-a,peak

pruebas = [
    "2+3*4",
    "2+3-4",
    "2+3*(4-5)"
]

for s in pruebas:
    t_cyk,m_cyk = medir(lambda x: cyk(tok(x)), s)
    t_ant,m_ant = medir(parse_antlr, s)

    print("cadena:", s)
    print(f"CYK: tiempo={t_cyk:.6f}s memoria={m_cyk} bytes")
    print(f"ANTLR: tiempo={t_ant:.6f}s memoria={m_ant} bytes")
    print()
