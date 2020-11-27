import os
import webbrowser
import subprocess
import sys
import interact.display as disp
import custom_commands as ccs
import _argn_._arg0_ as _arg0_
import _argn_._arg1_ as _arg1_
import _argn_._arg2_ as _arg2_
import _argn_._arg3_ as _arg3_
import _help_._help_ as _help_
import _help_._histops_ as _histops_
import _help_._pathops_ as _pathops_
import _help_._dispops_ as _dispops_
import for_loop
import time

origin = os.getcwd()
path = origin
print("RunFile 5.2.2. Enter 'help' for more info.\n")
print("HomePath:{}".format(path))
browserPath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
func=""
var = {}
forcode = []
loopli = []
for_ = runloop_ = 0
user=''
historydir = path+'\\.runfile_history'

commandlist = ['homepath','delpath','showpath','newhomepath','delfile','createfile','addcontent','store',
            'runfile','runfunc','funclist','findfunc','content','addpath','findpath','browse',
            'storelines','RunFile','clearcontent','clr','clear','help',
               'quit','history','clearhistory','searchhistory',
               'msg','menu','box','error','warn','info','tip','star',
               'int','string','float','list','tuple','type','prompt','for']

arg0 = ['homepath','showpath','delpath','enablenhp','disablenhp','enablebrowser','disablebrowser','quit',
        'clear','clr','help','history','clearhistory',
        'error']

arg1 = ['newhomepath','delfile','createfile','addcontent','runfile','funclist','content',
        'browse','RunFile','clearcontent','findpath','addpath',
        'searchhistory','error','warn','info','tip','box','msg','star',
        'int','string','float','list','tuple','type']

arg2 = ['runfunc','findfunc','box','int','string','float','list','store','storelines','tuple','addcontent']

arg3 = ['msg','star','menu','int','string','float','list','tuple']

historyops = ['history','clearhistory','searchhistory']
pathops = ['newhomepath','homepath','delpath','showpath','addpath','findpath']
dispops = ['msg','star','tip','error','warn','info','box']

invalidnames = list("!@#$%^&*()-+=:;><?/\|',.~`1234567890")

if os.path.exists(historydir)==False:
    filee = open(historydir,'x')
    filee.close()

def evaluate(com,arguments):
    global var
    if com=='summation':
        expr=""
        if arguments[0] in var:
            arguments[0] = var[arguments[0]]
        if isinstance(arguments[0],list):
            for x in range(0,len(arguments[0])):
                arguments[0][x] = str(arguments[0][x])
                if x==len(arguments[0])-1:
                    expr = expr+arguments[0][x]
                else:
                    expr = expr+arguments[0][x]+"+"
        elif "," in arguments[0]:
            typeliarg = []
            typeli = arguments[0].split(",")
            arguments[0] = []
            for i in typeli:
                i = i.strip()
                if i.isnumeric()==True:
                    i = eval(i)
                else:
                    pass
                typeliarg.append(i)
            arguments[0].extend(typeliarg)
            for x in range(0,len(arguments[0])):
                arguments[0][x] = str(arguments[0][x])
                if x==len(arguments[0])-1:
                    expr = expr+arguments[0][x]
                else:
                    expr = expr+arguments[0][x]+"+"
        else:
            for x in range(0,len(arguments)):
                arguments[x] = str(arguments[x])
                if arguments[x] in var:
                    arguments[x] = str(var[arguments[x]])
                
                if x==len(arguments)-1:
                    expr = expr+arguments[x]
                else:
                    expr = expr+arguments[x]+"+"
    elif len(arguments)==0:
        return com
    else:
        expr = str(com)
        if expr=='open':
            expr = '('
        elif expr=='close':
            expr = ')'
        elif expr=='pi':
            expr = '3.14'
        elif expr=='sub':
            expr = '-'
        else:
            pass
        for x in arguments:
            x = str(x)
            if x in var:
                expr = expr+str(var[x])
            elif x=='add':
                expr = expr+'+'
            elif x=='sub':
                expr = expr+'-'
            elif x=='mul':
                expr = expr+'*'
            elif x=='div':
                expr = expr+'/'
            elif x=='pow':
                expr = expr+'**'
            elif x=='floor':
                expr = expr+'//'
            elif x=='open':
                expr = expr+'('
            elif x=='close':
                expr = expr+')'
            elif x=='pi':
                expr = expr+'3.14'
            else:
                expr = expr+x
    try:
        expr = eval(expr)
    except:
        print("rf5>>Invalid expression.")
        return com
    else:
        return expr

while True:

    if for_==0:
        user = input("rf5>>")
    elif for_==1:
        user = input(" "*4+">")
        
    if user.strip()=="":
        continue

    command,com_arg = ccs.command_args(user,"::")

    if command[0] not in ['history','clearhistory','searchhistory']:
        filee = open(historydir,'a')
        filee.write(user.strip()+'\n')
        filee.close()

    if command[0]=="runloop":
        if for_==1:
            print("rf5>>For loop is still open.")
        elif for_==0:
            if runloop_==0:
                print("rf5>>No loops found.")
                continue
            for_loop.for_loop(var["_loopvar_"],loopli,forcode,len(com_arg),command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist)
            print()
            delete = var.pop(var["_loopvar_"],None)
            del var["_loopvar_"]
            runloop_=0
            forcode = []
        continue
            

    if command[0]=="endloop":
        if for_==0:
            print("rf5>>No loops found.")
            continue
        for_=0
        print("\nrf5>>Loop closed.")
        continue

    if command[0]=="for":
        if for_==1:
            print("rf5>>For loop is still open.")
            continue
        if runloop_==1:
            print("rf5>>Previous for loop due.")
            continue
        try:
            var["_loopvar_"] = com_arg[0]
            var[var["_loopvar_"]] = ""
            if com_arg[1] in var:
                com_arg[1] = var[com_arg[1]]
            if "," in com_arg[1]:
                try:
                    com_argli = com_arg[1].split(",")
                    start = int(com_argli[0].strip())
                    end = int(com_argli[1].strip())
                    step = int(com_arg[2])
                    loopli = list(i for i in range(start,end,step))
                    if loopli == []:
                        print("rf5>>Loop varied due to conflicting loop arguments.")
                        start = end = step = 0
                        loopli = [0]
                except:
                    try:
                        start = end = step = 0
                        typeliarg=[]
                        typeli = com_arg[1].split(",")
                        for i in typeli:
                            i = i.strip()
                            if i.isnumeric()==True:
                                i = eval(i)
                            else:
                                pass
                            typeliarg.append(i)
                        loopli = typeliarg
                    except:
                        print("rf5>>Invalid input.")
                        continue
                    else:
                        pass
                else:
                    pass
            elif isinstance(com_arg[1],str) or isinstance(com_arg[1],list) or isinstance(com_arg[1],tuple):
                loopli = com_arg[1]
                start = end = step = 0
            else:
                print("rf5>>Invalid input.")
                continue
            for_=1
            runloop_=1
            print("\n>>for [var:{0}, start:{1}, stop:{2}, step:{3}, iterate:{4}]\n".format(var["_loopvar_"],start,end,step,loopli))
        except:
            print("rf5>>Invalid input.")
            for_=0
            runloop_=0
            start = end = step = 0
            loopli = []
            forcode = []
        else:
            pass
        continue

    if for_==1:
        forcode.append(user)
        continue

    if command[0]=="delvar":
        del var[com_arg[0]]
        print("rf5>>Variable '{}' deleted.".format(com_arg[0]))
        continue

    if command[0] == "pause":
        if com_arg[0] in var:
            com_arg[0] = var[com_arg[0]]
        try:
            time.sleep(int(com_arg[0]))
        except:
            print("rf5>>Invalid input.")
        else:
            pass
        continue

    if len(command)==2:
        if command[1]=='summation':
            var[command[0]] = evaluate('summation',com_arg)
        elif command[1] in var:
            var[command[0]] = evaluate(var[command[1]],com_arg)
        else:
            var[command[0]] = evaluate(command[1],com_arg)
        continue

    if command[0] in var:
        if len(com_arg)==0:
            print(var[command[0]])
        elif len(com_arg)==1:
            if isinstance(var[command[0]],str) or isinstance(var[command[0]],list) or isinstance(var[command[0]],tuple):
                if "," in com_arg[0]:
                    try:
                        com_argli = com_arg[0].split(",")
                        if com_argli[0] in var:
                            outer = var[com_argli[0]]
                        else:
                            outer = int(com_argli[0].strip())
                        if com_argli[1] in var:
                            inner = var[com_argli[1]]
                        else:
                            inner = int(com_argli[1].strip())
                        print(var[command[0]][outer][inner])
                    except:
                        print("rf5>>Index out of range.")
                        continue
                    else:
                        pass
                else:
                    try:
                        if com_arg[0] in var:
                            ind = var[com_arg[0]]
                        else:
                            ind = int(com_arg[0].strip())
                        print(var[command[0]][ind])
                    except:
                        print("rf5>>Index out of range.")
                        continue
                    else:
                        pass
        elif len(com_arg)==2:
            if com_arg[0]=='type':
                if com_arg[1]=='int':
                    try:
                        var[command[0]]=int(var[command[0]])
                    except:
                        print("rf5>>Invalid typecasting.")
                    else:
                        pass
                elif com_arg[1]=='string':
                    try:
                        var[command[0]]=str(var[command[0]])
                    except:
                        print("rf5>>Invalid typecasting.")
                    else:
                        pass
                elif com_arg[1]=='float':
                    try:
                        var[command[0]]=float(var[command[0]])
                    except:
                        print("rf5>>Invalid typecasting.")
                    else:
                        pass
                elif com_arg[1]=='list':
                    try:
                        var[command[0]]=list(var[command[0]])
                    except:
                        print("rf5>>Invalid typecasting.")
                    else:
                        pass
                elif com_arg[1]=='tuple':
                    try:
                        var[command[0]]=tuple(var[command[0]])
                    except:
                        print("rf5>>Invalid typecasting.")
                    else:
                        pass
            elif com_arg[0]=='nest':
                if com_arg[1] in var:
                    com_arg[1] = var[com_arg[1]]
                    
                if isinstance(var[command[0]],list):
                    typeliarg=[]
                    if isinstance(com_arg[1],list) or isinstance(com_arg[1],tuple) or isinstance(com_arg[1],int) or isinstance(com_arg[1],float):
                        var[command[0]].append([com_arg[1]])
                        continue
                    typeli = com_arg[1].split(",")
                    fl=0
                    for i in typeli:
                        if fl==1:
                            typeliarg[-1] = typeliarg[-1]+i
                            fl=0
                            continue
                        i = i.strip()
                        if i[-1]=="\\":
                            i = list(i)
                            ele = ""
                            for n in range(len(i)):
                                if i[n]=="\\":
                                    i[n] = ","
                                ele = ele+i[n]
                            i = ele
                            fl = 1
                        if i.isnumeric()==True:
                            i = eval(i)
                        else:
                            pass
                        typeliarg.append(i)
                    var[command[0]].append(typeliarg)
                else:
                    print("rf5>>Can nest only to a list.")
            elif com_arg[0]=='stack':
                if com_arg[1] in var:
                    com_arg[1] = var[com_arg[1]]
                
                if isinstance(var[command[0]],list):
                    typeliarg=[]
                    if isinstance(com_arg[1],list) or isinstance(com_arg[1],tuple):
                        var[command[0]].extend(com_arg[1])
                        continue
                    if isinstance(com_arg[1],int) or isinstance(com_arg[1],float):
                        var[command[0]].extend([com_arg[1]])
                        continue
                    typeli = com_arg[1].split(",")
                    fl=0
                    for i in typeli:
                        if fl==1:
                            typeliarg[-1] = typeliarg[-1]+i
                            fl=0
                            continue
                        i = i.strip()
                        if i[-1]=="\\":
                            i = list(i)
                            ele = ""
                            for n in range(len(i)):
                                if i[n]=="\\":
                                    i[n] = ","
                                ele = ele+i[n]
                            i = ele
                            fl = 1
                        if i.isnumeric()==True:
                            i = eval(i)
                        else:
                            pass
                        typeliarg.append(i)
                    var[command[0]].extend(typeliarg)
                else:
                    print("rf5>>Can stack only to a list.")
            elif com_arg[0]=='join':
                if com_arg[1] in var:
                    com_arg[1] = var[com_arg[1]]
                    
                if isinstance(var[command[0]],str) and isinstance(com_arg[1],str):
                    var[command[0]] = var[command[0]]+com_arg[1]
                else:
                    print("rf5>>Can join only to a string.")
            elif isinstance(var[command[0]],str) or isinstance(var[command[0]],list) or isinstance(var[command[0]],tuple):
                if "," in com_arg[0]:
                    try:
                        com_argli = com_arg[0].split(",")
                        if com_argli[0] in var:
                            outer = var[com_argli[0]]
                        else:
                            outer = int(com_argli[0].strip())
                        if com_argli[1] in var:
                            inner = var[com_argli[1]]
                        else:
                            inner = int(com_argli[1].strip())
                        if com_arg[1]=="type":
                            print(type(var[command[0]][outer][inner]))
                    except:
                        print("rf5>>List index out of range.")
                        continue
                    else:
                        pass
                else:
                    try:
                        if com_arg[0] in var:
                            ind = var[com_arg[0]]
                        else:
                            ind = int(com_arg[0].strip())
                        if com_arg[1]=="type":
                            print(type(var[command[0]][ind]))
                    except:
                        print("rf5>>List index out of range.")
                        continue
                    else:
                        pass
            else:
                print("rf5>>Invalid input.")
        elif len(com_arg)==3:
            if com_arg[2] in var:
                com_arg[2] = var[com_arg[2]]
            if isinstance(var[command[0]],str) or isinstance(var[command[0]],list) or isinstance(var[command[0]],tuple):
                if "," in com_arg[0]:
                    try:
                        com_argli = com_arg[0].split(",")
                        if com_argli[0] in var:
                            outer = var[com_argli[0]]
                        else:
                            outer = int(com_argli[0].strip())
                        if com_argli[1] in var:
                            inner = var[com_argli[1]]
                        else:
                            inner = int(com_argli[1].strip())
                        if com_arg[1]=="type":
                            if com_arg[2]=='int':
                                try:
                                    var[command[0]][outer][inner]=int(var[command[0]])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='string':
                                try:
                                    var[command[0]][outer][inner]=str(var[command[0]][outer][inner])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='float':
                                try:
                                    var[command[0]][outer][inner]=float(var[command[0]][outer][inner])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='list':
                                try:
                                    var[command[0]][outer][inner]=list(var[command[0]][outer][inner])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='tuple':
                                try:
                                    var[command[0]][outer][inner]=tuple(var[command[0]][outer][inner])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                        elif com_arg[1]=="to":
                            try:
                                var[com_arg[2]] = var[command[0]][outer][inner]
                            except:
                                print("rf5>>Invalid input.")
                                continue
                            else:
                                pass
                        elif com_arg[1]=="int":
                            try:
                                var[command[0]][outer][inner] = int(com_arg[2])
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="float":
                            try:
                                var[command[0]][outer][inner] = float(com_arg[2])
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="string":
                            try:
                                var[command[0]][outer][inner] = str(com_arg[2])
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="list":
                            try:
                                typeliarg=[]
                                if isinstance(com_arg[2],list) or isinstance(com_arg[2],tuple):
                                    var[command[0]][outer][inner] = list(com_arg[2])
                                    continue
                                typeli = com_arg[2].split(",")
                                fl=0
                                for i in typeli:
                                    if fl==1:
                                        typeliarg[-1] = typeliarg[-1]+i
                                        fl=0
                                        continue
                                    i = i.strip()
                                    if i[-1]=="\\":
                                        i = list(i)
                                        ele = ""
                                        for n in range(len(i)):
                                            if i[n]=="\\":
                                                i[n] = ","
                                            ele = ele+i[n]
                                        i = ele
                                        fl = 1
                                    if i.isnumeric()==True:
                                        i = eval(i)
                                    else:
                                        pass
                                    typeliarg.append(i)
                                var[command[0]][outer][inner] = typeliarg
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="tuple":
                            try:
                                typeliarg=[]
                                if isinstance(com_arg[2],list) or isinstance(com_arg[2],tuple):
                                    var[command[0]][outer][inner] = tuple(com_arg[2])
                                    continue
                                typeli = com_arg[2].split(",")
                                fl=0
                                for i in typeli:
                                    if fl==1:
                                        typeliarg[-1] = typeliarg[-1]+i
                                        fl=0
                                        continue
                                    i = i.strip()
                                    if i[-1]=="\\":
                                        i = list(i)
                                        ele = ""
                                        for n in range(len(i)):
                                            if i[n]=="\\":
                                                i[n] = ","
                                            ele = ele+i[n]
                                        i = ele
                                        fl = 1
                                    if i.isnumeric()==True:
                                        i = eval(i)
                                    else:
                                        pass
                                    typeliarg.append(i)
                                var[command[0]][outer][inner] = tuple(typeliarg)
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                    except:
                        print("rf5>>List index out of range.")
                        continue
                    else:
                        pass
                else:
                    try:
                        if com_arg[0] in var:
                            ind = var[com_arg[0]]
                        else:
                            ind = int(com_arg[0].strip())
                        if com_arg[1]=="type":
                            if com_arg[2]=='int':
                                try:
                                    var[command[0]][ind]=int(var[command[0]][ind])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='string':
                                try:
                                    var[command[0]][ind]=str(var[command[0]][ind])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='float':
                                try:
                                    var[command[0]][ind]=float(var[command[0]][ind])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='list':
                                try:
                                    var[command[0]][ind]=list(var[command[0]][ind])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                            elif com_arg[2]=='tuple':
                                try:
                                    var[command[0]][ind]=tuple(var[command[0]][ind])
                                except:
                                    print("rf5>>Invalid typecasting.")
                                else:
                                    pass
                        elif com_arg[1]=="to":
                            try:
                                var[com_arg[2]] = var[command[0]][ind]
                            except:
                                print("rf5>>Invalid input.")
                                continue
                            else:
                                pass
                        elif com_arg[1]=="int":
                            try:
                                var[command[0]][ind] = int(com_arg[2])
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="float":
                            try:
                                var[command[0]][ind] = float(com_arg[2])
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="string":
                            try:
                                var[command[0]][ind] = str(com_arg[2])
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="list":
                            try:
                                typeliarg=[]
                                if isinstance(com_arg[2],list) or isinstance(com_arg[2],tuple):
                                    var[command[0]][ind] = list(com_arg[2])
                                    continue
                                typeli = com_arg[2].split(",")
                                fl=0
                                for i in typeli:
                                    if fl==1:
                                        typeliarg[-1] = typeliarg[-1]+i
                                        fl=0
                                        continue
                                    i = i.strip()
                                    if i[-1]=="\\":
                                        i = list(i)
                                        ele = ""
                                        for n in range(len(i)):
                                            if i[n]=="\\":
                                                i[n] = ","
                                            ele = ele+i[n]
                                        i = ele
                                        fl = 1
                                    if i.isnumeric()==True:
                                        i = eval(i)
                                    else:
                                        pass
                                    typeliarg.append(i)
                                var[command[0]][ind] = typeliarg
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                        elif com_arg[1]=="tuple":
                            try:
                                typeliarg=[]
                                if isinstance(com_arg[2],list) or isinstance(com_arg[2],tuple):
                                    var[command[0]][ind] = tuple(com_arg[2])
                                    continue
                                typeli = com_arg[2].split(",")
                                fl=0
                                for i in typeli:
                                    if fl==1:
                                        typeliarg[-1] = typeliarg[-1]+i
                                        fl=0
                                        continue
                                    i = i.strip()
                                    if i[-1]=="\\":
                                        i = list(i)
                                        ele = ""
                                        for n in range(len(i)):
                                            if i[n]=="\\":
                                                i[n] = ","
                                            ele = ele+i[n]
                                        i = ele
                                        fl = 1
                                    if i.isnumeric()==True:
                                        i = eval(i)
                                    else:
                                        pass
                                    typeliarg.append(i)
                                var[command[0]][ind] = tuple(typeliarg)
                            except:
                                print("rf5>>Invalid input.")
                            else:
                                pass
                    except:
                        print("rf5>>List index out of range.")
                        continue
                    else:
                        pass
        else:
            print("rf5>>Invalid input.")
        continue

    if command[0] not in commandlist:
        print("rf5>>Command '{}' doesn't exist. Enter 'help' for more info.".format(command[0]))
        continue

    arglen = len(com_arg)
    arglen+=1
    
    if arglen>4:
        print(f"rf5>>Max command length:4  Got:{arglen}")
        continue
    else:
        pass


    if arglen==1:

        if command[0]=="help":
            _help_._help_()
        else:
            path,origin = _arg0_._0_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist)

    elif arglen==2:
        if command[0]=="help":
            if com_arg[0] in historyops:
                _histops_.histops(com_arg[0])
            elif com_arg[0] in pathops:
                _pathops_.pathops(com_arg[0])
            elif com_arg[0] in dispops:
                _dispops_.dispops(com_arg[0])
            else:
                print("rf5>>Command not found.")
        else:
            origin,path = _arg1_._1_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist)

    elif arglen==3:

        _arg2_._2_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist)

    elif arglen==4:
    
        _arg3_._3_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist)
        print()
        
    continue

        

        

