service=int(input("input service"))
if service>=5 :
    salary = int(input("input salary"))
    print("bonus payable amount=",salary+(.05*salary))//.05 is the bonus 
else:
    print("you are not eligible")
