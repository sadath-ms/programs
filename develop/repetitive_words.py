from collections import Counter
text='This is sadath, i am from vayalpad,i have been working as a fullstack developer in banaglaore sadath'
d=text.replace(',',' ')
c=Counter(d.split(' '))
print(c.most_common(2))
