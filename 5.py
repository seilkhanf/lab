z,x=[int(i) for i in input().split()]
q=set()

w=set()


for i in range(z):
    w.add(int(input()))

for i in range(x):
    q.add(int(input()))


print(len(w&q))
print(*sorted(w&q))
print(len(w-q))
print(*sorted(w-q))    
print(len(q-w))
print(*sorted(q-w))
