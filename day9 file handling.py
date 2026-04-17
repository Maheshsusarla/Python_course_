#error handling 
# try: # if try block is flase then print except block
#     x=int(input("Enter the number : "))
#     print(10/x)
# except:
#     print("worng answer")


# try :
#     file=open("filehandling.csv","r")
#     print(file.read())
#     file.close()
# except:
#     print("File is not there ")

# try :
#     file=open("filehandlings.csv","r")
#     print(file.read())
#     file.close()
# except:
#     print("File is not there ")

# try:
#     file=open("filehandling.csv","r")
#     print(file.read())
#     file.close()
# except:
#     print("File is not there ") #try block is flase then it will print
# else:
#     print("File is there ")
# finally:
#     print("Done")

try:
    file=open("filehandling.csv","r")
    print(file.read())
    file.close()
except:
    print("File is not there ") #try block is flase then it will print
else:
    print("File is there ") #when the try block is true then else is also true
finally:
    print("Done") #always print it 
