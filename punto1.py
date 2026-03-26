import re

class N:
    def __init__(self,t,v=None,h=None):
        self.t=t; self.v=v; self.h=h or []

    def txt(self):
        return self.v

    def p(self,pre="",ult=True):
        print(pre + ("└── " if ult else "├── ") + self.txt())
        pre += "    " if ult else "│   "
        for i,x in enumerate(self.h):
            x.p(pre, i==len(self.h)-1)

def tok(s):
    return re.findall(r'\d+|[()+\-*/]',s)

class P:
    def __init__(self,t):
        self.t=t; self.i=0

    def a(self):
        return self.t[self.i] if self.i<len(self.t) else None

    def c(self):
        x=self.a(); self.i+=1; return x

    def E(self):
        x=self.T()
        while self.a() in ['+','-']:
            o=self.c()
            x=N("Op",o,[x,self.T()])
        return x

    def T(self):
        x=self.F()
        while self.a() in ['*','/']:
            o=self.c()
            x=N("Op",o,[x,self.F()])
        return x

    def F(self):
        if self.a() and self.a().isdigit():
            return N("Num",self.c())
        if self.a()=='(':
            self.c()
            x=self.E()
            if self.a()!=')':
                raise Exception("error")
            self.c()
            return x
        raise Exception("error")

def dibujar_graphviz(n):
    try:
        from graphviz import Digraph
        g=Digraph()
        def rec(nodo,padre=None,c=[0]):
            i=str(c[0]); c[0]+=1
            g.node(i,nodo.v)
            if padre:
                g.edge(padre,i)
            for h in nodo.h:
                rec(h,i,c)
        rec(n)
        g.render("arbol",view=True)
    except:
        pass

pruebas = [
    "2+3*4",
    "2+3-4",
    "2+3*(4-5)"
]

for i, s in enumerate(pruebas, 1):
    print("\n----------------------")
    print(f"Cadena {i}: {s}")
    print("Arbol:")

    a = P(tok(s)).E()
    a.p()

    dibujar_graphviz(a)
