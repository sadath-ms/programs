'''
Given the participants' score sheet for your University Sports Day,
 you are required to find the runner-up score.
 You are given scores. Store them in a list and find the score of the runner-up.

input Format:
The first line contains n. The second line contains an array a[]  of n  integers each separated by a space.
Constraints

Sample Input
5
2 3 6 6 5
Sample Output
5
'''



n=int(input())
list_=list(set(map(int,input().strip().split(" "))))
list_.sort(reverse=True)
print(list_[1])


'''
    strip(char) is a built in function in python ,to remove characters from both left and right based on
    arguments..default is white spaces..
    split()method returns a list of all words in the string using str=" " is a seperator num= numner of
    splits to the number..'''

    
