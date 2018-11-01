students_data=dict()
import datetime

n=str(input('enter which u operations you have to perform'))


if n.upper()=='C':

    def create(name,joining_date,releaving_date):
        students_data[name]=[joining_date,releaving_date]
        return students_data

    print('sorry something went wrong...')


name=str(input('enter the student name..'))
admission_date=input(datetime.date)
realiving_date=input(datetime.date)

create(name,admission_date,realiving_date)
n=str(input('enter which u operations you have to perform'))









