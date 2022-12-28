zipcode=str(input("Please enter the code:"))
if len(zipcode)==6 and zipcode.isdigit()==True:
    print("TRUE")
else:
    print("please enter the code again!")
print(type(zipcode))