'''
Write a Python program which accepts a sequence of comma-separated numbers from user
                                and generate a list and a tuple with those numbers.

'''

values=input('enter the number seperted by commas')
list=values.split(' , ')
tuple=tuple(list)
print('list:-',list)
print('tuple:-',tuple)
