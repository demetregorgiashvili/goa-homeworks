your_age=int(input("put your age to see if you get discount : "))
if your_age<=18:
    if your_age<14:
        print("20% disc")
    else:
        print ("10% disc")
else:
    print("no dicount for you")