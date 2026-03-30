#tuple :tuple is collection of order items enclosing ()
# tuple is immutable 
my_tuple=(1,2,4)

# print(my_tuple)
# print(my_tuple[0:1])

# my_tuple[0]="Mahi" #TypeError: 'tuple' object does not support item assignment
# print(my_tuple)

# my_tuple=list(my_tuple)
# my_tuple[0]="Mahesh"
# my_tuple=tuple(my_tuple)
# print(my_tuple)

#len
# print(len(my_tuple))

# #count 
# print(my_tuple.count(2))

#index 
# print(my_tuple.index(1))

#packing and unpacking 
# per=('mahi',21,'Engineer')
# (name,age,job)=per
# print(name)
# print(age)
# print(job)


#set : is a unorder collection of unqie elements enclosed in {}
# duplicates are automatically remove 
fru={'app','mango','orange'}
# print(type(fru))

num={1,2,3,1,3,4,1,2,4}
# empty=set()
# print(num)
# print(num[0]) #TypeError: 'set' object is not subscriptable

#add
fru.add('bannana')
# print(fru)

#update add multiple items
fru.update(['mai',3,6,8])
# print(fru)

# #remove
# fru.remove('app')
# # print(fru)
# #it agian to run its show error because app is not there so thats why its show error 
# # we use discard merhods if value it not there didt show error


# fru.discard('app')
# # print(fru)

# a={1,2,3,4}
# b={3,4,5,6,7}
# print(a|b) #show all the ele   #union
# print(a&b) #only cooman values #intersection
# print(a-b) #only elements in a not there in b 
# print(a^b) 

# #len
# print(len(fru))
# #clear
# print(fru.clear())
# #copy
# print(fru.copy())



#dictionary : A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
student={"Name":"Mahesh","age":21,}

# print(student["Name"])
# print(student["Names"]) #KeyError: 'Names' not in value error 

#get
# print(student.get("age"))
# print(student.get("ages")) #if it is not there in value it show none  use get method

#add new key value 
student["Class"]=4
#update the old value
student["age"]=22
# print(student)

#pop specific key it will remove
student.pop("Class")
# print(student)

for key,value in student.items():
    print(key,":",value)


#nested dict
emp={
    "name":"mahi",
    "age":21,
    "skills":["python","sql","html"]
}
print(emp["skills"][0])