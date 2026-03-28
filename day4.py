#day4

#for loop:
# for i in range(0,10):
#     print(i)

# fruits=["a","b","c"]
# for i in fruits:
#     print(i)

# for i in range(0,10,2):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# fru=["Apple","Mango","c"]
# for i in fru:
#     print(i)

#while loop: repect the block of code as long as a condiction true
# i=0
# n=int(input("Enter the range :"))
# while(i<n):
#     print("Count is ",i)
#     i+=1

#control statements :
#break satement is used to exit loop immediately come out of thr loop
# for i in range(0,10):
#     if i==5:
#         break
#     print(i)

#continue :it skips the current iteration and moves to the next one in the loop 
# for i in range(0,10):
#     if i==3:
#         continue
#     print(i)

#pass :- its do nonothing in starement 
# for i in range(0,10):
#     if i==3:
#         pass
#     print(i)

#nested for loop
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

#patterns:
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n=5
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")
    print()


