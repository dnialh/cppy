sk_left = [-1]
sk_right = [-1]
sk_value = [-1]

def meld(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if sk_value[a] < sk_value[b]:
        a, b = b, a
        
    val = sk_value[a]
    
    lt = meld(sk_right[a], b)
    rt = sk_left[a]

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
    assert a
    return meld(sk_left[a], sk_right[a])

def get_list(a):
    out = []
    st = [a]
    while st:
        u = st.pop()
        if u == 0:
            continue

        out.append(sk_value[u])
        st.append(sk_left[u])
        st.append(sk_right[u])

    return sorted(out)
    
#Source: Own (dnialh)
