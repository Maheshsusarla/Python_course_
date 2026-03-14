# #day3:

#comparision operators: checks for something
x=10
y=20
# print(x==y)
# print(x<y)
# print(x>y)
# # y=10
# print(x<=y)
# print(x>=y)
# print(x!=y)


# print(x>5 and y>=20) #both true
# print(x>5 or y>20)#one condiction is true
# print(not(x<y)) #opsite


#condictional statements
# age=int(input("Enter the age "))
# if age>18:
#     print("Major")
# else:
#     print("minor")

# age=int(input("Enter the age "))
# if age<18:
#     print("Minor")
# elif age<60:
#     print("Citizen")
# elif age<90:
#     print("very old")
# else:
#     print("Senior citizen")

# mark=int(input("Enter marks"))
# if mark>=50:
#     if mark>=90:
#         print("Excellent")
#     else:
#         print("passed but must improve")
# else:
#     print("Failed")

#list -all thigs are apply
a=[1,2,3,4,5]
# print(a)
# print(a[2])
# print(a[-1])
# a[0]="mango"
# print(a)

# a.append("apple") #add an end of the list
# a.remove(2) #remove element
# print(len(a))
# print(a)
# print(a[0:3])
# print(a[::-1])



#Task1
# create list and print and sum,average
# nums=[1,2,3,4,5]
# total=sum(nums)
# avg=total/len(nums)
# print(total,avg)

#Task2 
# take 3 input from users and append it list and find the average and avg
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# nums=[]
# nums.append(a)
# nums.append(b)
# nums.append(c)
# print(nums)
# total=sum(nums)
# avg=total/len(nums)
# print(total,avg)

#taks3
#take age from user and print if less 13 and 13 between 19 and 20 b/w 59 and else
age=int(input("Enter the age "))
if age<13:
    print("Chiled")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior")