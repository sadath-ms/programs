from os import system, name
import sys


def add_new():
    print("What do you want to add in the list")
    list_add = input()
    my_file = open("sad.txt", mode='a+')
    my_file.write(list_add + '\n')
    my_file.close()

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    print("The list has been updated")

    print("Do you want to continue? type y/n")
    n = input()
    if n is 'y':
        main()
    else:
        exit_todo


def show_list():
    my_file = open("sad.txt", mode='r')
    contents = my_file.readlines()
    # print(contents)
    if len(contents) == 0:
        print("No records found")
    global i
    i = 1
    for itr in contents:
        print(str(i) + ". " + itr, end='')
        i += 1
    my_file.close()

    print("\n\nDo you want to continue? type y/n")
    n = input()
    if n is 'y':
        main()
    else:
        exit_todo


def remove_a_list():
    print("Enter the task you wanna delete")
    n = input()
    with open("sad.txt", mode='r') as my_file:
        contents = my_file.readlines()
        my_file.close()
    # print(contents)
    count = 0
    counter = -1
    for itr in contents:
        counter += 1
        if itr.find(n) != -1:
            print("Are you sure you want to delete this line?\n" + itr + "Type y/n")
            choice = input()
            if choice is 'y':
                count = 1
                contents.pop(counter)
                my_file = open("my_file.txt", mode='w')
                for i in contents:
                    my_file.write(i)
                print("The record has been deleted successfully")
                break
    if count == 0:
        print("No records found with name " + n)

    print("Do you want to continue? type y/n")
    n = input()
    if n is 'y':
        main()
    else:
        exit_todo


def reset_list():
    print("Are you sure you want to reset? Type y/n")
    n = input()
    if n is 'y':
        my_file = open("sad.txt", mode='w')
        my_file.close()
        print("All the data has been deleted")
    else:
        print("reset Cancelled")

    print("\nDo you want to continue? type y/n")
    n = input()
    if n is 'y':
        main()
    else:
        exit_todo


def completeTask():
    print("Enter the task you completed")
    n = input()
    with open("my_file.txt", mode='r') as my_file:
        contents = my_file.readlines()
        my_file.close()
        print(contents)
    count = 0
    counter = -1
    for itr in contents:
        counter += 1
        if itr.find(n) != -1:
            count = 1
            contents.pop(counter)
            my_file = open("my_file.txt", mode='w')
            for i in contents:
                my_file.write(i)
            print("The record has been assigned completed")
            break
    if count == 0:
        print("No records found with name " + n)

    print("Do you want to continue? type y/n")
    n = input()
    if n is 'y':
        main()
    else:
        exit_todo


def exit_todo():
    sys.exit()


def main():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    print("\n\nEnter your choice")
    print("1. Add new item")
    print("2. Show records")
    print("3. Remove a desired record")
    print("4. Reset the record")
    print("5. Assigned the task as completed")
    print("6. Exit")
    choice = int(input())

    # print(choice)
    # print("this line will execute")
    # my_dict={
    # 		'1':add_new(),
    # 		'2':show_list(),
    # 		'3':remove_a_list,
    # 		'4':reset_list,
    # 		'5':sort_ascending,
    # 		'6':exit_todo,
    # 	}
    # my_dict.get(choice)
    # print(my_dict,"hiiiiii")
    # # if 0<choice<7:
    # # 	my_dict.get(choice)

    # # else:
    # 	# print("invalid input")

    if choice == 1:
        add_new()
    elif choice == 2:
        show_list()
    elif choice == 3:
        remove_a_list()
    elif choice == 4:
        reset_list()
    elif choice == 5:
        completeTask()
    elif choice == 6:
        exit_todo()


if __name__ == '__main__':
    main()
