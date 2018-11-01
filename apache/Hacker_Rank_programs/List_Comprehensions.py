'''
            List Comprehesions:
                List Comprehesions is used to creating a new list from another iterables.

                syntax:
                    [expression for variable in collection]

                        expression is generate the element in the list,condition execute every item
                                                                                    in the collection


    #Task:-
            You are given three integers x,y and z  representing the dimensions of a cuboid along with an integer N .
             You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of
              i+j+k is not equal to N . Here, 0<=i<=X; 0<=j<=Y; 0<=k<=Z;

              i/p:-1
                   1
                   1
                   2

              o/p:-[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

'''
x, y, z, n = (int(input()) for _ in range(4))
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n])
