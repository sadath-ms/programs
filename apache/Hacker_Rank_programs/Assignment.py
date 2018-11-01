from collections import defaultdict,OrderedDict
d = defaultdict(list)
for _ in range(int(input())):
    for _ in range(int(input())):
        name,tweet=input().split()
        d[name].append(tweet)
        dict={key:len(value) for key,value in d.items()}
        #print(dict)
        highest_values=max(dict.values())
        #print(highest_values)
        sorting_=OrderedDict(sorted(dict.items()))
    for key,value in sorting_.items():
        if value==highest_values:
            print(key,value)
