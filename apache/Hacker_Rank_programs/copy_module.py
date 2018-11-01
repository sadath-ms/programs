






import copy
li=[1,2,[3,4],5]

# li2=copy.deepcopy(li)
#
# print('orginal elements...')
#
# for i in range(0,len(li)):
#     print(li[i],end=' ')
#
# print("\r")
#
# li2[2][0]=7
#
# print()
#
# print('the new list of the element after deep copying...')
#
# for i in range(0,len(li2)):
#     print(li2[i],end=' ')
#
#
# print('orginal element after deep copying...')
#
# for i in range(0,len(li)):
#     print(li[i],end=' ')



#
# """____Shallow copy_____"""
#
#
# li=[1,2,[3,4],5]
#
# li2=copy.copy(li)
#
# print('orginal list...')
#
# for i in range(0,len(li)):
#     print(li[i],end=' ')
#
# li2[2][0]=7
# print('\r')
#
# print('after shallow copy...')
#
# for i in range(0,len(li2)):
#     print(li2[i],end=' ')
#     print('\r')
#
#
# print('to check the changes...')
#
# for i in range(0,len(li)):
#     print(l
