n=int(input('enter a number...'))
lists=list(set(map(int,input('enter lists of:-').strip().split())))
lists.sort(reverse=False)
print(lists[1])
