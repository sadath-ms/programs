phoneBook={}
n=int(input('how many contacts will u save..'))
for _ in range(n):
    name,number=input('enter name and number').split()
    phoneBook[name]=number
search=input('')
while search:
    phone_number=phoneBook.get(search)
    if phone_number:
        print(search+'-'+phone_number)
        break
    else:
        print('not found..')
