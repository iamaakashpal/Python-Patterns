# 1 ####################################################

'''

* 
* * 
* * * 
* * * * 
* * * * * 

num=int(input("Enter Number Of Rows : "))
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end=' ')
    print()

'''

# 2 ####################################################

'''

* * * * *
* * * *
* * *
* *
*

num=int(input("Enter Number Of Rows : "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=' ')
    print()

'''


# 3 ####################################################

'''

          *
        * *
      * * *
    * * * *
  * * * * *

num=int(input("Enter Number of Rows : "))
for i in range(0,num):
    for j in range(i,num):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")
    print()    

'''

# 4 ####################################################

'''

  * * * * *
    * * * *
      * * *
        * *
          *

num=int(input("Enter Number Of Rows : "))
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,num):
        print("*",end=" ")
    print()

'''

# 5 ####################################################

'''

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

num=int(input("Enter Number of Row : "))
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

'''

# 6 ####################################################

'''

        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *

num=int(input("Enter Number of Row : "))
for i in range(num):
    for j in range(num-1,i,-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")        
    print()

'''

# 7 ####################################################

'''

          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *

num=int(input("Enter Number of Rows:"))
for i in range(0,num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

'''

# 8 ####################################################

'''

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

num=int(input("Enter Number of Rows : "))
for i in range(num):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,num):
        print("*",end=" ")
    for j in range(i,num-1):
        print("*",end=" ")
    print()

'''

# 9 ####################################################

'''

        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *

num=int(input("Enter Number of Rows:"))
k=num*2-2
for i in range(num):
    for j in range(k):
        print(" ",end="")
    k=k-1
    for j in range(i+1):
        print("*",end=" ")
    print()
k=num-2
for i in range(num,-1,-1):
    for j in range(k):
        print(" ",end="")
    k=k+1
    for j in range(i+1):
        print("*",end=" ")
    print()

'''

# 10 ####################################################

'''

* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *


num=int(input("Enter Number of Rows : "))
for i in range(0,num):
    for j in range(num-i):
        print("*",end=" ")
    for j in range(2*i):
        print(" ",end=" ")

    # for j in range(i):
    #     print(" ",end=" ")
    for j in range(num-i):
        print("*",end=" ")


    print()
for i in range(0,num):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(num-i-1):
        print(" ",end=" ")
    for j in range(num-i-1):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")
    print()

'''