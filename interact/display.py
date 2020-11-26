import time
import random

try:
    import os
except:
    print("os (installation reqd. - yes")
    time.sleep(3)
    quit()
else:
    pass

try:
    import getpass
except:
    print("getpass (installation reqd. - yes)")
    time.sleep(3)
    quit()
else:
    pass


def error(m='An error occured.'):
    if m.strip() == "":
        m=' '*7
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 9:
            l = l+" "*(9-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-ERROR"+"-"*(maximum-5)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")

        

def warn(m=' '*9):
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 11:
            l = l+" "*(11-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-WARNING"+"-"*(maximum-7)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")

        

def info(m=' '*6):
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 8:
            l = l+" "*(8-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-INFO"+"-"*(maximum-4)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")

        

def tip(m=' '*5):
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 7:
            l = l+" "*(7-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-TIP"+"-"*(maximum-3)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")



def custom_yesno(m=" "):
    conf = input(f"{m} (y/n) : ")
    if conf.lower().strip() in ['y' , 'yes']:
        con = 1
    elif conf.lower().strip() in ['n' , 'no']:
        con = 0
    else:
        con = 2
    print()
    return con



def yesno():
    conf = input("Confirm? (y/n) : ")
    if conf.lower().strip() in ['y' , 'yes']:
        con = 1
    elif conf.lower().strip() in ['n' , 'no']:
        con = 0
    else:
        con = 2
    print()
    return con



def exit_yesno():
    conf = input(f"Exit from application? (y/n) : ")
    if conf.lower().strip() in ['y' , 'yes']:
        con = 1
    elif conf.lower().strip() in ['n' , 'no']:
        con = 0
    else:
        con = 2
    print()
    return con



def prompt(m=" "):
    ans = input(f"{m} : ")
    print()
    return ans



def msg(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"{m}" , flush = mode , end=e)



def star(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"*{m}" , flush = mode , end=e)



def menu(title=" ",items=[],reuse=0):
    li = items
    if isinstance(li , list) == False:
        print("ArgTypeError : menu(<string> , <list> , reuse)")
        return
    n = 1
    li = list(li)
    if reuse==0:
        print(f"\n------{title}------\n")
        for l in li:
            print(f"{n}. {l}")
            n+=1
        print("\n------"+"-"*len(title)+"------\n")
        return
    elif reuse==1:
        usermenu=f"\n------{title}------\n\n"
        for l in li:
            usermenu+=f"{n}. {l}\n"
            n+=1
        usermenu+="\n------"+"-"*len(title)+"------\n\n"
        return usermenu
    else:
        print(f"\n------{title}------\n")
        for l in li:
            print(f"{n}. {l}")
            n+=1
        print("\n------"+"-"*len(title)+"------\n")
        return



def box(title='-',m=' '):
    title=str(title)
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < len(title)+2:
            l = l+" "*((len(title)+2)-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-"+title+"-"*(maximum-len(title))+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")
    

def clr():
    os.system('cls')

def help():
    print("\nLink : https://github.com/siddhanth78/interact_module/blob/master/display.txt\n")

def pause(min_=0,sec=0,msec=0):
    time.sleep((min_*60)+(sec*1)+(msec*0.001))
   
