n = int(input())

adj = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split()); u -= 1; v -= 1
    adj[u].append((v))
    adj[v].append((u))

def dist(start):
    d = [-1] * n

    d[start] = 0

    st = [start]
    while st:
        u = st.pop()
        
        for v in adj[u]:
            if d[v] == -1:
                st.append(v)
                d[v] = d[u] + 1

    return d

#Source: Own (dnialh)
