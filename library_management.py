
def rand_user_id():
    import random
    result = "2"
    for i in range(9):
        digit = str(random.randint(0,9))
        result += digit
    
    return result

def rand_admin_id():
    import random
    result="1"
    for i in range(9):
        digit = str(random.randint(0,9))
        result += digit
    
    return result

def rand_book_id():
    import random
    result = ""
    lst = ['a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z','1','2','3','4','5',
    '6','7','8','9','0']
    list_r=[]
    for i in range(10):
        while True:
            rand = random.choice(lst)
            if (rand not in list_r) :
                list_r.append(rand)
                break    
    for i in list_r :
        result += i
    
    return result

def user_file():
    try:
        with open("C:/Users/AceR/Desktop/python/Project/user.txt" , 'r') as x:
            lst=x.readlines()
            l=len(lst)
            for i in range(0,l):
                lst[i]=lst[i].strip()
    except FileNotFoundError :
        with open("C:/Users/Acer/Desktop/python/Project/user.txt" , 'w') as r:
            r.write("----------------user list : ----------------\n")  
        r.close()
        lst=r.readlines()
    
    return lst

def admin_file():
    try:
        with open("C:/Users/AceR/Desktop/python/Project/admin.txt" , 'r') as x:
            lst=x.readlines()
            l=len(lst)
            for i in range(0,l):
                lst[i]=lst[i].strip()
    except FileNotFoundError :
        with open("C:/Users/Acer/Desktop/python/Project/admin.txt" , 'w') as r:
            r.write("----------------admin list : ----------------\n")  
        r.close()
        lst=r.readlines()
    
    return lst

def book_file():
    try:
        with open("C:/Users/AceR/Desktop/python/Project/book.txt" , 'r') as x:
            lst=x.readlines()
            l=len(lst)
            for i in range(0,l):
                lst[i]=lst[i].strip()
    except FileNotFoundError :
        with open("C:/Users/Acer/Desktop/python/Project/book.txt" , 'w') as r:
            r.write("----------------book list : ----------------\n")  
        r.close()
        lst=r.readlines()
    
    return lst

def borrow_file():
    try:
        with open("C:/Users/AceR/Desktop/python/Project/borrow.txt" , 'r') as x:
            lst=x.readlines()
            l=len(lst)
            for i in range(0,l):
                lst[i]=lst[i].strip()
    except FileNotFoundError :
        with open("C:/Users/Acer/Desktop/python/Project/borrow.txt" , 'w') as r:
            r.write("----------------borrow list : ----------------\n")  
        r.close()
        lst=r.readlines()
    
    return lst

def reserve_file():
    try:
        with open("C:/Users/AceR/Desktop/python/Project/reserve.txt" , 'r') as x:
            lst=x.readlines()
            l=len(lst)
            for i in range(0,l):
                lst[i]=lst[i].strip()
        
    except FileNotFoundError :
        with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'w') as r:
            r.write("----------------reserve list : ----------------\n")  
        r.close()
        lst=r.readlines()
    
    return lst


def book_write(lst):
    with open("C:/Users/AceR/Desktop/python/Project/book.txt" , 'w') as x:
        for i in lst:
            x.write(i)
            x.write("\n")
    x.close()

def currentdate():
    import datetime

    current_time = datetime.datetime.now()
    date=str()
    date+=str(current_time.year)
    date+="/"
    date+=str(current_time.month)
    date+="/"
    date+=str(current_time.day)

    return date


def dayspassed(start ,end):
    year=int(end[0:4])-int(start[0:4])
    month=int(end[5])-int(start[5])
    day=int(end[7:9])-int(start[7:9])

    if (day<0):
        day+=30
        month-=1
    
    if (month<0):
        month+=12
        year-=1
    
    return (year*365 + month*30 + day)


def user_edit(userid):
    temp=userid
    lst = user_file()
    l= len(lst)
    for i in range (0,l):
        if (lst[i]==userid):
            j=i
            break
    
    lst[j+1]=input("\t\t\t Enter your new password (press <<b>> to back): ")
    if (lst[j+1]=="b"):
        user_page(userid)
    lst[j+2]=input("\t\t\t Enter your new name : ")
    lst[j+3]=input("\t\t\t Enter your new number : ")

    with open("C:/Users/AceR/Desktop/python/Project/user.txt" , 'w') as w:
        for i in range(0,l):
            w.write(lst[i])
            w.write("\n")
    w.close()
    user_page(temp)


def login(x):
    #x:1:user
    #x:2:admin
    t=x
    print("\t\t\t -----------------------------------------\n")
    print("\t\t\t     welcome to login page\n")
    print("\t\t\t ##please enter your id and password to continue : ")
    myid = input("\t\t\t enter id \t (press <<b>> to back) : ")
    if (myid=="b"):
        main_menu(x)
    password = input("\t\t enter password : ")
    import os
    os.system('cls')

    c = 0
    if (x==1):
        lst=user_file()
        for i in range(0,len(lst)):
            if (lst[i]==myid):
                c=1
                index=i
                break

        if (c==0):
            print("\n\t\t username not found... \n")
            login(t)
        if (password==lst[index+1]):
            print("\t\t\t Login succesfull\n")
            user_page(myid)
            
        else:
            print("\t\t\t wrong username or password\n")
            login(t)
    
    else:
        lst=admin_file()
        for i in range(0,len(lst)):
            if (lst[i]==myid):
                c=1
                index=i
                break

        if (c==0):
            print("\n\t\t username not found... \n")
            login(t)
        if (password==lst[index+1]):
            print("\t\t\t Login succesfull\n")
            admin_page(myid)
            
        else:
            print("\t\t\t wrong username or password\n")
            login(t)


def register(x):
    print("\t\t\t -----------------------------------------\n")
    print("\t\t\t     welcome to registration page\n")
    t=x

    #x:1:user
    #x:2:admin

    if (t==1):
        username = rand_user_id()
        print(f"\t\t\t your username is : {username}")
        name = input("\t\t Enter your name ( press <<b>> to back ) : ")
        if (name=="b"):
            main_menu(t)
        password = input("\t\t Enter your password : ")
        number = input("\t\t Enter your phone number : ")
        import os
        os.system('cls')

        with open("C:/Users/AceR/Desktop/python/Project/user.txt" , 'a') as user:
            user.write(username)
            user.write("\n")
            user.write(password)
            user.write("\n")
            user.write(name)
            user.write("\n")
            user.write(number)
            user.write("\n")
            user.write("----------------------------------------")
            user.write("\n")

    else:
        adminid = rand_admin_id()
        print(f"\t\t\t your username is : {adminid}")
        password = input("\t\t Enter your password ( press <<b>> to back ) : ")
        if (password=="b"):
            main_menu(t)
        import os
        os.system('cls')

        with open("C:/Users/AceR/Desktop/python/Project/admin.txt" , 'a') as admin:
            admin.write(adminid)
            admin.write("\n")
            admin.write(password)
            admin.write("\n")
            admin.write("----------------------------------------")
            admin.write("\n")

    print("\t\t registration succesfull")
    main_menu(t)


def forgot(x):
    #x:1:user
    #x:2:admin
    t=x

    print("\t\t --------------------------------------------\n")
    print("\t\t\t please enter your id to get your passwod : ")
    a_id = input("\t\t Enter your username  (press <<b>> to back) : ")
    if (a_id=="b"):
        main_menu(t)
    s=0
    import os
    os.system('cls')

    if (t==1):
        with open("C:/Users/AceR/Desktop/python/Project/user.txt" , 'r') as f:
            lst =f.readlines()
            l=len(lst)

            for i in range(0,l):
                a=lst[i].strip()
                if (a==a_id):
                    b=lst[i+1].strip()
                    s = 1
                    break

            if (s==0):
                print("\t\t\t username can not be found !")
                forgot(t)
            else:
                print(f"\t\t\t your password is : {b}")
                main_menu(t)        

    else:
        with open("C:/Users/AceR/Desktop/python/Project/admin.txt" , 'r') as f:
            lst =f.readlines()
            l=len(lst)

            for i in range(0,l):
                a=lst[i].strip()
                if (a==a_id):
                    s = 1
                    b=lst[i+1].strip()
                    break
            
            if (s==0):
                print("\t\t\t username can not be found !")
                forgot(t)
            else:
                print(f"\t\t\t your password is : {b}")
                main_menu(t)  


def addbook(adminid):
    temp=adminid
    bookid = rand_book_id()
    print("\t\t -Book id : {0}".format(bookid))
    name = input("\t\t -Enter bookname ( press <<b>> to back ) : ")
    if (name=="b"):
        admin_page(temp)
    author = input("\t\t -Enter Book author : ")
    daily_fair = input("\t\t -Enter daily fair : ")
    status = "available"
    borrow_id = "#"
    import os
    os.system('cls')

    with open ("C:/Users/Acer/Desktop/python/Project/book.txt" , 'a') as book:
        book.write(bookid)
        book.write("\n")
        book.write(name)
        book.write("\n")
        book.write(author)
        book.write("\n")
        book.write(daily_fair)
        book.write("\n")
        book.write(status)
        book.write("\n")
        book.write(borrow_id)
        book.write("\n")
        book.write("----------------------------------------\n")
    book.close()

    print("\n\t\t\t Book added succesfully \n")
    admin_page(temp)


def edit_book(adminid):
    '''
    bookid
    name
    author
    daily fair
    status
    borrow id
    '''
    temp=adminid
    lst=book_file()

    name = input("\t\t Enter the book name to edit ( press <<b>> to back ) : ")
    if (name=="b"):
        admin_page(temp)
    found=0
    for i in range(0,len(lst)):
        if (lst[i]==name):
            index=i
            found=1
            break
    import os
    os.system('cls')

    if (found==0):
        print("\n\t\t\t Book not found ! \n")
        edit_book(temp)

    lst[index] = input("\t\t -Enter book new name : ")
    lst[index+1] = input("\t\t -Enter book new author : ")
    lst[index+2] = input("\t\t -Enter book new daily fair : ")

    with open ("C:/Users/Acer/Desktop/python/Project/book.txt" , 'w') as book:
        for i in lst:
            book.write(i)
            book.write("\n")
    book.close()
    import os
    os.system('cls')

    print("\n\t\t\t Book Edit succesfull...\n")
    admin_page(temp)

def remove_book(adminid):
    temp=adminid
    name = input("\n\t\t\t Enter Book Name to Delete ( press <<b>> to back ) : ")
    if (name=="b"):
        admin_page(temp)
    lst=book_file()
    import os
    os.system('cls')
    found=0

    for i in range(0,len(lst)):
        if (lst[i]==name):
            index=i-1
            found=1
            break
            
    if (found==0):
        print("\n\t\t\t Book Not Found !...\n")
        remove_book(temp)

    i=0
    with open("C:/Users/Acer/Desktop/python/Project/book.txt" , 'w') as book:
        while i<len(lst):
            if (i==index):
                i+=7
                continue
            book.write(lst[i])
            book.write("\n")
            i+=1
    book.close()

    print("\n\t\t\t Book Delete Succesfull... \n")
    admin_page(temp)

def user_print(userid):
    temp=userid
    lst=book_file()
    borrowlist=borrow_file()
    found=0
    s=0

    for i in range(0,len(lst)):
        if (lst[i]==userid):
            found=1
            index1=i
            index1-=4
            break
    
    if (found==0):
        print("\n\t\t no Book is Borrowed By this ID ... \n")
        user_page(temp)
    
    for i in range(0,len(borrowlist)):
        if (borrowlist[i]==userid):
            found=1
            index3=i+1
            break

    today=currentdate()
    start=borrowlist[index3]
    day=18-dayspassed(start, today)

    for i in range(index1+5,len(lst)):
        if (lst[i]==userid):
            index2=i
            index2-=4
            s=1
            break


    print("\n\t\t-----------------------------------------\n")
    print("\n\t\t -Book Name : " , lst[index1])
    print("\n\t\t -Book Author : " , lst[index1+1])
    print("\n\t\t -Book Daily fair : " , lst[index1+2])
    print("\n\t\t -Days left : " , day)
    print("\n\t\t-----------------------------------------\n")

    if (s==1):
        print("\n\t\t -Book Name : " , lst[index2])
        print("\n\t\t -Book Author : " , lst[index2+1])
        print("\n\t\t -Book Daily fair : " , lst[index2+2])
        for i in range(index3+1,len(borrowlist)):
            if (borrowlist[i]==userid):
                index3=i+1
                break

        today=currentdate()
        start=borrowlist[index3]
        day=18-dayspassed(start, today)
        print("\n\t\t -Days left : " , day)

    user_page(temp)


def reserve_list(userid , bookname):
    try :
        with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'r') as r:
            tr=r.read()
        r.close()
    except FileNotFoundError :
        with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'w') as r:
            r.write("----------------reserve list : ----------------\n")  
        r.close()

    lst=reserve_file()
    temp=userid
    found=0

    for i in range(0,len(lst)):
        if (bookname==lst[i]):
            index=i
            found=1
            break
    
    if (found==0):
        with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'a') as r:
            r.write(bookname)
            r.write("\n")
            r.write(userid)
            r.write("\n")
            r.write("#")
            r.write("\n")
            r.write("----------------------------")
        r.close()
        print("\n\t\t You Got in reserve list succesfully :) \n")
    
    else:
        if (lst[index+1]==userid or lst[index+2]==userid):
            print("\n\t\t\t !! You Cannot Get in Reserve list more than one Time ...\n")
            user_page(temp)
        
        if(lst[index+2]=="#"):
            lst[index+2]=userid
            print("\n\t\t You Got in reserve list succesfully :) \n")
            with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'w') as r:
                for i in lst:
                    r.write(i)
                    r.write("\n")
            r.close()

        else:
            print("\n\t\t Sorry !! Reserve list is full ... :( \n")

    user_page(temp)


def borrow_book(userid):
    temp=userid
    print("\t\t ------------------------------------------\n")
    name=input("\t Enter Book Name to Borrow ( press <<b>> to back ) : ")
    if (name=="b"):
        user_page(temp)
    import os
    os.system('cls')
    found=0
    counter=0
    c=0

    lst=book_file()

    for i in range(0,len(lst)):
        if (name==lst[i]):
            index=i
            found=1
            break

    for i in lst:
        if (i==userid):
            c+=1

    if (found==0):
        print("\n\t\t Book Not Found !...\n")
        borrow_book(temp)

    else:
        if (lst[index+4]==userid):
            print("\n\t\t You Can not Borrow a Book more Than One Time ...\n")
            user_page(temp) 

        elif (lst[index+3] != "available"):
            reserve_list(temp, name)

        elif (c>2):
            print("\n\t\t You Can not Borrow more Than Two Book ...\n")
            user_page(temp)

        else:
            date=currentdate()

            lst[index+3]="busy"
            lst[index+4]=userid
            book_write(lst)
            print("\n\t\t Book Borrowed Succesfully...\n")
            
            with open("C:/Users/Acer/Desktop/python/Project/borrow.txt" , 'a') as b:
                b.write(name)
                b.write("\n")
                b.write(userid)
                b.write("\n")
                b.write(date)
                b.write("\n")
                b.write("--------------------------------------\n")
            b.close()

            user_page(temp)


def respite_book(userid):
    temp=userid
    booklist=book_file()
    borrowlist=borrow_file()
    reservelist=reserve_file()

    name=input("\n\t\t\t Enter Book Name to continue \t ( press <<b>> to back ) : ")
    if (name=="b"):
        user_page(temp)
    import os
    os.system('cls')
    found=0
    for i in range(0,len(borrowlist)):
        if (borrowlist[i]==name and borrowlist[i+1]==userid):
            index=i
            found=1
            break

    if (found==0):
        print("\t\t no book is borrowed by you ... \n")
        respite_book(temp)
    
    start=borrowlist[index+2]
    end=currentdate()
    day=dayspassed(start, end)

    for i in range(0,len(booklist)):
        if (booklist[i]==name):
            index2=i
            break

    dailyfair=booklist[index2+2]
    if (day>18):
        total_fair=day*dailyfair
    else :
        total_fair=0
    
    print("\n\t\t Your total fair is : " , total_fair)
    while 1:
        x=input("\n\t\t Click Ok to continue : ")
        if (x=="ok" or x=="OK" or x=="Ok" or x=="oK"):
            break
    import os
    os.system('cls')

    found=0
    for i in range(0,len(reservelist)):
        if (reservelist[i]==name):
            found=1
            index3=i
            break

    if (found==1):
        if (reservelist[index3+2] != "#"):
            booklist[index2+4]=reservelist[index3+1]
            borrowlist[index+1]=reservelist[index3+1]
            reservelist[index3+1]=reservelist[index3+2]
            reservelist[index3+2]="#"
            borrowlist[index+2]=currentdate()

            with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'w') as res :
                for i in reservelist:
                    res.write(i)
                    res.write("\n")
            res.close()
        else:
            booklist[index2+4]=reservelist[index3+1]
            borrowlist[index+1]=reservelist[index3+1]
            reservelist[index3+1]="#"
            borrowlist[index+2]=currentdate()

            with open("C:/Users/Acer/Desktop/python/Project/reserve.txt" , 'w') as res :
                i=0
                while(i<len(reservelist)):
                    if (i==index3):
                        i+=4
                        continue
            res.close()
    
        with open("C:/Users/Acer/Desktop/python/Project/book.txt" , 'w') as book :
            for i in booklist:
                book.write(i)
                book.write("\n")
        book.close()

        with open("C:/Users/Acer/Desktop/python/Project/borrow.txt" , 'w') as bo :
            for i in borrowlist:
                bo.write(i)
                bo.write("\n")
        bo.close()
    else:
        booklist[index2+3]="available"
        booklist[index2+4]="#"
        with open("C:/Users/Acer/Desktop/python/Project/book.txt" , 'w') as book :
            for i in booklist:
                book.write(i)
                book.write("\n")
        book.close()
        with open("C:/Users/Acer/Desktop/python/Project/borrow.txt" , 'w') as bo :
            i=0
            while (i<len(borrowlist)):
                if (i==index):
                    i+=4
                    continue
                else:
                    bo.write(borrowlist[i])
                    bo.write("\n")
                    i+=1
        
    print("\n\t\t Book Respited succefully \n")
    user_page(temp)

def renewal(userid):
    temp=userid
    reservelist=reserve_file()
    borrowlist=borrow_file()
    found=0
    f=0

    name=input("\n\t\t Enter book name  ( press <<b>> to back ) : ")
    if(name=="b"):
        user_page(temp)
    import os
    os.system('cls')
    for i in range(0,len(borrowlist)):
        if (borrowlist[i]==name):
            found=1
            borrow_index=i
            break
    
    if (found==0):
        print("\n\t\t No book is borrowed by your id...\n")
        renewal(temp)

    status = True
    for i in range(0,len(reservelist)):
        if (reservelist[i]==name):
            status=False
            break
    
    if (status==False):
        print("\n\t\t Book is in reserve list ...\n")
        user_page(temp)
    
    borrowlist[(borrow_index)+2] = currentdate()

    with open("C:/Users/Acer/Desktop/python/Project/borrow.txt" , 'w') as bo :
        for i in borrowlist:
            bo.write(i)
            bo.write("\n")
    bo.close()
    
    print("\n\t\t your time renewaled succesfully ...\n")
    user_page(temp)


def admin_page(adminid):
    temp=adminid
    print("\t\t ------------------------------------------\n")
    print("\t\t\t welcome to your page dear admin\n")
    print("\t\t -press 1 to add book\n")
    print("\t\t -press 2 to edit book\n")
    print("\t\t -press 3 to remove book\n")
    print("\t\t -press 4 to exit\n")
    a=int(input("\t\t -Enter your choice : "))
    import os
    os.system('cls')

    if (a==1):
        addbook(temp)
    elif (a==2):
        edit_book(temp)
    elif (a==3):
        remove_book(temp)
    elif(a==4):
        main_menu(2)
    else:
        print("\t\t Enter correct value ...\n")
        admin_page(temp)


def user_page(userid):
    temp=userid
    print("\t\t ------------------------------------------\n")
    print("\t\t\t welcome to your page dear user\n")
    print("\t\t -press 1 to edit your information\n")
    print("\t\t -press 2 to borrow book\n")
    print("\t\t -press 3 to respite book\n")
    print("\t\t -press 4 to reneawl book time\n")
    print("\t\t -press 5 to print your books information\n")
    print("\t\t -press 6 to exit\n")

    awnser=int(input("\t\t enter yout choice : "))
    import os
    os.system('cls')

    if (awnser==1):
        user_edit(temp)
    elif (awnser==2):
        borrow_book(temp)
    elif(awnser==3):
        respite_book(temp)
    elif (awnser==4):
        renewal(temp)
    elif (awnser==5):
        user_print(temp)
    elif (awnser==6):
        main_menu(1)
    else:
        print("\t\t Enter correct value ...\n")
        user_page(temp)

def main_menu(x):
    t=x
    print("\t\t\t --------------------------------------------\n")
    print("\t\t\t       Welcome to main menu \n")
    print("\t\t -press 1 to login\n")
    print("\t\t -press 2 to register\n")
    print("\t\t -press 3 if you forgot your password\n")
    print("\t\t -press 4 to exit\n")

    a = int(input("\t\t Enter your choice : "))
    import os
    os.system('cls')

    if (a==1):
        login(t)
    elif (a==2):
        register(t)
    elif (a==3):
        forgot(t)
    elif (a==4):
        start_page()
    else:
        print("\t\t Enter corect value !")
        main_menu(t)

def start_page():
    print("\t\t\t ------------------------------------------------------------- \n")
    print("\t\t\t\t Are you user(1) or admin(2) ? \n")
    print("\t\t\t\t press (3) to exit \n")
    awnser=int(input("\t\t Enter awnser :"))
    import os
    os.system('cls')
    
    if (awnser==1 or awnser==2):
        main_menu(awnser)
    elif (awnser==3):
        print("\t\t -----------------Thank you...\n\n")
        exit()
    else:
        print("\t\t Enter correct value ")

start_page()