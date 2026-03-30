menu={
    'dosa': 20,
    'idly': 40,
    'vada': 50
}
orders=[]
total=0
n=int(input("Enter how many items you want : "))
for i in range(n):
    item=input("Enter item (dosa,idly,vada) ")
    if item in menu:
        orders.append(item)
        total+=menu[item]
        print(f"{item} added")
    else:
        print("Item is not avaliable")
print("your ordrs",orders)
print("total",total)