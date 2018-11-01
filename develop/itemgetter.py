from operator import itemgetter
n=int(input('enter the n'))
l=[]
for _ in range(0,n):
    name,age,score=map(str,input('enter ').split())
    l.append(tuple([name,age,score]))
    print(l)
