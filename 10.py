o, p = [int(i) for i in input().split()]
t = set()

for i in range(p):
    ai, bi = [int(k) for k in input().split()]

    for k in range(ai, o+1, bi):

        if k%7 == 6 or k%7 == 0:
            continue
        
        t.add(k)


print(len(t))
