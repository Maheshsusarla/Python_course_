# 1 create a tuple of your 5 fav colors and print 3rd one 
tup=('red','black','yellow','green','white')
# print(tup[2])

# 2 try to change tuple value
fav=('hi','hello','good')
favs=list(fav)
favs[0]='mahi'
fav=tuple(favs)
# print(fav)

# 3 create 2 sets of sets and show the union and intersection 
c={1,2,3,2,3,4,6,5,7,8}
d={4,3,1,2,4,6,3,5,7}
# print(c|d)
# print(c&d)

#find unqui words from a list of repeted words using set
lis=["apple","mango","apple","mango"]
sets=set(lis)
# print(sets)

# 5 comple two tuple and find how mant times specific value count
t1=(10,20,30,10,20)
t2=(40,30,20,10)
t3=t1+t2
# print(t3.count(10))


# write a program that store 3 studends list of them marks list and calculate avg marks
students = {
    "mahi": [20, 30, 40],
    "pardhu": [50, 60, 70],
    "pavan": [25, 35, 45]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(name, "average marks:", avg)