'''
finding the percentage...
'''
students_marks={}
for _ in range(int(input('total no of students...'))):
    name,*a=input().split()
    score=list(map(float,a))
    students_marks[name]=score

query_name=input('enter whos % you want')
marks=students_marks[query_name]
print(marks)
print('%.2f'%(sum(marks)/len(marks)))
