sk_left = [-1]
sk_right = [-1]
sk_value = [-1]

def meld(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    

    val = max(sk_value[a], sk_value[b])
    

    if val == sk_value[a]:
        lt = meld(sk_right[a], b)
        rt = sk_left[a]
    else:
        lt = meld(a, sk_right[b])
        rt = sk_left[b]

    ind = len(sk_value)
    
    sk_value.append(val)
    sk_left.append(lt)
    sk_right.append(rt)
    
    return ind

def insert(a, v):
    ind = len(sk_value)

    sk_left.append(0)
    sk_right.append(0)
    sk_value.append(v)

    return meld(ind, a)

def tail(a):
    return meld(sk_left[a], sk_right[a])
    
#Source: Own (dnialh)
