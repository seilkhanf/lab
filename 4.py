B=input().split()
X=set()


for i in range(len(B)): 


    if B[i] in B[:i]:
        print("YES")
    else:   
        print("NO")
        X.add(i)
