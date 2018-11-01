n=int(input('enter the number'))
rev=0
dig=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)


n=input('enter the number')
print(n[::-1])
print(type(n))
