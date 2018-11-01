'''
  Nested_List:

  Given the names and grades for each student in a Physics class of N students,
   store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

  Note: If there are multiple students with the same grade,
    order their names alphabetically and print each name on a new line.

    input Format
        The first line contains an integer,N, the number of students.
        The 2N subsequent lines describe each student over 2 lines;
        the first line contains a student's name, and the second line contains their grade.

 Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students,
 order their names alphabetically and print each one on a new line.

'''

python_students=[]
for _ in range(int(input())):
    name=input('enter student name..')
    grade=float(input('enter student grade...'))
    python_students.append([name,grade])
    print(python_students)

all_grades=list(set([student[1] for student in python_students]))
print(all_grades)
all_grades=sorted(all_grades)
print(all_grades)

second_lowest=all_grades[1]
print(second_lowest)

result=[name for name,grade in python_students if grade==second_lowest]
sorted_by_names=sorted(result)
output='/n'.join(sorted_by_names)
print(output)


#[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
