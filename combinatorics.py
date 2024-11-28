MOD = 998244353

def modmul(x, y, c = 0):
    return (x * y + c) % MOD

mod_mul = modmul

def inv(x):
    return pow(x, MOD - 2, MOD)

MAX = 10 ** 6

fact = [1]
for i in range(1, MAX):
    fact.append(modmul(i, fact[i-1]))

invfact = [1] * (MAX)
invfact[MAX - 1] = inv(fact[MAX - 1])
for i in range(MAX - 2, -1, -1):
    invfact[i] = modmul(i + 1, invfact[i+1])

def comb(x, y):
    return modmul(fact[x], modmul(invfact[y], invfact[x - y]))

def perm(x, y):
    return modmul(fact[x], invfact[x - y])

def invcomb(x, y):
    return modmul(invfact[x], modmul(fact[y], fact[x - y]))

def invs(x):
    return modmul(fact[x - 1], invfact[x])

#Source: own (dnialh)
