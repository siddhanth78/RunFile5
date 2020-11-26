import time

try:
    import mysql.connector
except:
    print("mysql-connector-python (installation reqd. - yes)")
    time.sleep(3)
    quit()
else:
    pass

try:
    import stdiomask
except:
    print("stdiomask (installation reqd. - yes)")
    time.sleep(3)
    quit()
else:
    pass

import random


syner = ("Syntax for updates : updates=[(<table1>,<targetcolumn1>,<newdata1 (int or string)>,"
         "<conditioncolumn1 (can be blank by entering '')>,<pattern1> (can be blank by entering '')),\n"
         "                             (<table2>,<targetcolumn2>,<newdata2 (int or string)>,"
         "<conditioncolumn2 (can be blank by entering '')>,<pattern2> (can be blank by entering '')),\n"
         "                          ...(<table'n'>,<targetcolumn'n'>,<newdata'n' (int or string)>,"
         "<conditioncolumn'n' (can be blank by entering '')>,<pattern'n'> (can be blank by entering ''))]")


def help():
    print("\nLink : https://github.com/siddhanth78/interact_module/blob/master/sqlops.txt\n")


def login(sqlhost="localhost",sqluser="root",sqlpass="",sqldb="",dbtable="credentials"):
    usern = ""
    passw = ""
    valid = 0
    mid=''
    
    while True:
        usern = input("Username : ")
        if usern.strip() == "":
            print("\nUsername must be filled.\n")
            continue
        break
    while True:
        passw = stdiomask.getpass(prompt="Password : ")
        if passw.strip() == "":
            print("\nPassword must be filled.\n")
            continue
        break

    if sqldb.strip()=="":
        pass
    else:
        try:
            mydb = mysql.connector.connect(
                host = sqlhost.strip(),
                user = sqluser.strip(),
                passwd = sqlpass,
                database = sqldb.strip()
                )

            cursor = mydb.cursor()
        except:
            print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
            valid = 0
        else:
            cursor.execute(f"create table if not exists {dbtable.strip()} (m_id varchar(5) not null unique,Username varchar(20) not null unique , Password varchar(20) not null unique)")
            cursor.execute(f"select * from {dbtable.strip()}")
            for i in cursor:
                mid,us,pa = i
                if usern == us and passw == pa:
                    print("\nCredentials valid.\n")
                    valid = 1
                    break
            else:
                print("\nInvalid credentials.\n")
                valid = 0
                
    return(mid , usern , passw ,valid)



def select(sqlhost="localhost",sqluser="root",sqlpass="",sqldb="",dbtable="",reqcol="*",wherecol="",pattern="",multicond=[]):
    itemlist = []
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = sqldb.strip()
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        if wherecol.strip()=="" and multicond==[]:
            try:
                cursor.execute(f"select {reqcol.strip()} from {dbtable.strip()}")
            except:
                print("\nError. Check your arguments again.\n")
                return
            else:
                for item in cursor:
                    itemlist.append(item)
                return itemlist
        elif wherecol.strip()!="" and multicond==[]:
            if pattern.strip()=="":
                print("\nPattern required.\n")
                return
            else:
                try:
                    cursor.execute(f"select {reqcol.strip()} from {dbtable.strip()} where {wherecol.strip()} like '{pattern}'")
                except:
                    print("\nError. Check your arguments again.\n")
                    return
                else:
                    for item in cursor:
                        itemlist.append(item)
                    return itemlist
        elif wherecol.strip()=="" and multicond!=[]:
            if pattern.strip()!="":
                print("\nPattern not required.\n")
                return
            else:
                try:
                    if len(multicond) == 1:
                        for j in multicond:
                            where , patt = j
                        cursor.execute(f"select {reqcol.strip()} from {dbtable.strip()} where {where.strip()} like '{patt}'")
                    elif len(multicond) > 1:
                        com=""
                        n=0
                        sqlbase = f"select {reqcol.strip()} from {dbtable.strip()} where "
                        for j in multicond:
                            n+=1
                            where , patt = j
                            if n<len(multicond):
                                com = com+where+" like "+patt+" and "
                            else:
                                com = com+where+" like "+patt
                        cursor.execute(sql+com)
                except:
                    print("\nError. Check your arguments again.\n")
                    return
                else:
                    for item in cursor:
                        itemlist.append(item)
                    return itemlist



def insert(sqlhost="localhost",sqluser="root",sqlpass="",sqldb="",dbtable="",newdata=[]):
    
    if isinstance(newdata , list) == False:
        print("ArgTypeError : multi_update(<string> , <string> , <string> , <list>)")
        return
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = sqldb.strip()
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        number = 1
        for new in newdata:
            if str(new).strip() == "":
                print(f"\nError in query {number}. New data can't be blank.\n")
                number+=1
                continue
        
            else:
                ndat = ""
                for ne in new:
                    if ndat=="":
                        ndat=ndat+f"'{str(ne)}'"
                    else:
                        ndat=ndat+","+f"'{str(ne)}'"
                try:
                    cursor.execute(f"insert into {dbtable.strip()} values ({ndat.strip()})")
                    mydb.commit()
                except:
                    print(f"\nError in query {number}. Check your arguments again.\n")
                    number+=1
                    continue
                else:
                    number+=1
                    continue



def exec(sqlhost="localhost",sqluser="root",sqlpass="",comm=[]):
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to server. Probably invalid credentials.\n")
        return
    else:
        no=1
        for c in comm:
            try:
                cursor.execute(c)
            except:
                print(f"\nError in query {no}.\n")
                no+=1
            else:
                no+=1
        


def update(sqlhost="localhost",sqluser="root",sqlpass="",sqldb="",updates=[]):
    global syner
    if isinstance(updates , list) == False:
        print("ArgTypeError : multi_update(<string> , <string> , <string> , <list>)")
        return
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = sqldb.strip()
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        number = 1
        for up in updates:
            try:
                if len(up)==3:
                    dbtable,reqcol,newdata = up
                elif len(up)==5:
                    dbtable,reqcol,newdata,wherecol,pattern = up
            except:
                print(f"\nError in query {number}. Probably missing arguments or invalid data.\n")
                print(syner)
                number+=1
                continue
            else:
                pass
            
            if str(updates).strip() == "":
                print(f"\nError in query {number}. New data can't be blank.\n")
                print(syner)
                number+=1
                continue
        
            if len(up)==3:
                try:
                    cursor.execute(f"update {dbtable.strip()} set {reqcol.strip()} = '{newdata}'")
                    mydb.commit()
                except:
                    print(f"\nError in query {number}. Check your arguments again.\n")
                    print(syner)
                    number+=1
                    continue
                else:
                    number+=1
                    continue
            else:
                if pattern.strip()=="":
                    print(f"\nError in query {number}. Pattern required.\n")
                    print(syner)
                    number+=1
                    continue
                else:
                    #try:
                    cursor.execute(f"update {dbtable.strip()} set {reqcol.strip()} = '{newdata}' where {wherecol.strip()} like '{pattern}'")
                    mydb.commit()
                    '''except:
                        print(f"\nError in query {number}. Check your arguments again.\n")
                        print(syner)
                        number+=1
                        continue
                    else:
                        number+=1
                        continue'''
                


def sign_up(sqlhost="localhost",sqluser="root",sqlpass="",sqldb="",dbtable="credentials"):
    usern = ""
    passw = ""
    valid = 0
    mid=''

    while True:
        usern = input("Username : ")
        if usern.strip() == "":
            print("\nUsername must be filled.\n")
            continue
        break
    while True:
        passw = stdiomask.getpass(prompt="Password : ")
        if passw.strip() == "":
            print("\nPassword must be filled.\n")
            continue
        break
    while True:
        repassw = stdiomask.getpass(prompt="Confirm password : ")
        if repassw.strip() == "":
            print("\nPassword must be filled.\n")
            continue
        
        if repassw != passw:
            print("\nPasswords do not match.\n")
            continue
        elif repassw == passw:
            break

    if sqldb.strip()=="":
        pass
    else:
        try:
            mydb = mysql.connector.connect(
                host = sqlhost.strip(),
                user = sqluser.strip(),
                passwd = sqlpass,
                database = sqldb.strip()
                )

            cursor = mydb.cursor()
        except:
            print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
            valid = 0
        else:
            try:
                mid=""
                no1=random.randint(0,9)
                no2=random.randint(10,99)
                ch1=random.randint(65,90)
                ch2=random.randint(65,90)
                mid=str(chr(ch1))+str(no1)+str(chr(ch2))+str(no2)
                print(f"\nYour m_id : {mid}\n")
                cursor.execute(f"create table if not exists {dbtable.strip()} (m_id varchar(5) not null unique,Username varchar(20) not null , Password varchar(20) not null unique)")
                cursor.execute(f"insert into {dbtable.strip()} values('{mid}','{usern}','{passw}')")
                mydb.commit()
            except:
                print("\nError. Couldn't register. Possibly because username/password/m_id already exists or invalid username/password (No special characters other than '_' allowed).\n")
                valid = 0
            else:
                print("\nYou have been registered. Welcome.\n")
                valid = 1
                
    return(mid , usern , passw ,valid)
