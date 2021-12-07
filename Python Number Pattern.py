# 1 ####################################################

'''

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

'''

# 2 ####################################################

'''

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()

'''

# 3 ####################################################

'''

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(i+1):
        print(i+1,end=" ")
    print()

'''

# 4 ####################################################

'''

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(num,i,-1):
        print(num-i,end=" ")
    print()

'''

# 5 ####################################################

'''

5
4 4
3 3 3
2 2 2 2
1 1 1 1 1

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(i+1):
        print(num-i,end=" ")
    print()

'''

# 6 ####################################################

'''

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(i+1):
        print(num-j,end=" ")
    print()

'''

# 7 ####################################################

'''

5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

num=int(input("Enter a Number of Rows :"))
for i in range(num):
    for j in range (i,-1,-1):
        print(num-j,end=" ")
    print()

'''