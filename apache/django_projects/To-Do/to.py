import datetime

def create():
    patient_name=input('enter name of the student...')
    appoinment_date=
    appoinment_time=


    with open('sad.txt',mode='a+') as sadath:
        sadath.write(patient_name + '\n')

def read():
    with open('sad.txt',mode='r') as sadath1:
        print(sadath1.read())




def dele():
    with open("sad.txt", "r") as f:
        lines = f.readlines()
        print(lines)
        with open("sad.txt", "w") as new_f:
            for line in lines:
                new_f.write(line)




def main():
    print('add! add new entry...')
    n=str(input())

    if n=='add':
        add()
    elif n=='display':
        display()
    elif n=='d':
        dele()



if __name__ == '__main__':
        main()
