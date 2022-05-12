import os
z = 1
while(True):
    print("\n 1. Add Record")
    print("\n 2. Display All Record")
    print("\n 3. Search Student Record By Name")
    print("\n 4. Search Student Record By Roll No")
    print("\n 5. Delete Student Record By Name")
    print("\n 6. Update Student Record")
    print("\n 7. Exit")

n = int(input(" Enter Your Choice :"))
if(n == 7):
    break
elif(n == 1):
    print("\n Enter student Detail \n")
    n = input("Enter Name:")
    r = input("Enter Roll No :")
    cl = input("Enter Class :")
    fees = input(" Enter Fees :")
    per = input(" Enter Percentage :")
    f = open("developers.txt", "a")
    f.write(n+"-"+r+"-"+cl+"-"+fees+"-"+per+"\n")
    f.close()
elif(n == 2):
    print("\n\n List of Present Records \n\n")
    print("NAME - ROLL NO - CLASS - FEES - PERCENTAGE")
    f = open("developers.txt", "r")
    while(True):
        d = f.readline()
        l = len(d)
        if(l == 0):
            break
        print(d.strip())
    f.close()
elif(n == 3):
    search = input("Enter student Name :")
    f = open("developers.txt", "r")
    flag = 0
    while(True):
        t = f.readline()
        l = len(t)
        if(l == 0):
            break
        g = t.split('-')
        if(g[0] == search):
            print("\n Record Found ")
            print(" Name is ", g[0])
            print(" Roll No is ", g[1])
            print(" Class is ", g[2])
            print(" Fees is ", g[3])
            print(" Percentage is ", g[4])
            flag = 1
            break
        if(flag == 0):
            print(" Record Not Found")
        f.close()
elif (n == 4):
    search = input("Enter student Roll No :")
    f = open("developers.txt", "r")
    flage = 0
    while(True):
        t = f.readline()
        l = len(t)
        if(l == 0):
            break
        g = t.split('-')
        if(g[1] == search):
            print("\n Record Found ")
            print(" Name is ", g[0])
            print(" Roll No is ", g[1])
            print(" Class is ", g[2])
            print(" Fees is ", g[3])
            print(" Percentage is ", g[4])
            flag = 1
            break
        if(flag == 0):
            print(" Record Not Found")
        f.close()
elif(n == 5):
    search = input("Enter Student Name :")
    f = open("developers.txt", 'r')
    tt = open("temp.txt", "w")
    h = 0
    flag = 0
    while(True):
        t = f.readline()
        l = len(t)
        if(l == 0):
            break
        g = t.split('-')
        if(g[0] != search):
            tt.write(t)
        if(g[0] == search):
            h = 1
    f.close()
    tt.close()
    if(h == 1):
        print("Record Deleted Successfully")
        os.remove("developers.txt")
        os.rename("temp.txt", "developers.txt")
    elif(h == 0):
        print(" Record Not Found !! deletion unsuccessful")
elif(n == 6):
    h = 0
    search = input("Enter Student Name :")
    f = open("developers.txt", "r")
    tt = open("temp.txt", "w")
    flag = 0
    while(True):
        t = f.readline()
        l = len(t)
        if(l == 0):
            break
        g = t.split('-')
        if(g[0] == search):
            print("Current Detail is \n ", t)
            print("------------")
            new_roll = input(
                "want to change rollno? Enter new detail or Press enter to continue")
            new_class = input(
                "want to change class? Enter new detail or Press enter to continue")
            new_fees = input(
                "want to change fees? Enter new detail or Press enter to continue")
            new_per = input(
                "want to change per? Enter new detail or Press enter to continue")
            if(len(new_roll) == 0):
                new_roll = g[1]
            if(len(new_class) == 0):
                new_class = g[2]
            if(len(new_fees) == 0):
                new_fees = g[3]
            if(len(new_per) == 0):
                new_per = g[4]
            tt.write("\n"+g[0]+"-"+new_roll+"-" +
                     new_class+"-"+new_fees+"-"+new_per)
            h = 1
        else:
            tt.write(t)
    f.close()
    tt.close()
    if(h == 1):
        print(" Record Updated Successully")
        os.remove("developers.txt")
        os.rename("temp.txt", "developers.txt")
    elif(h == 0):
        print("No Such Record Exist: for Updation Process")
