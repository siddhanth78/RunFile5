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
import time

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

ct = 0

def for_loop(lvar,loopli,forcode,arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist):

    for itr in loopli:
        for user in forcode:

            var[lvar] = itr
            command,com_arg = ccs.command_args(user,"::")

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
                if isinstance(var[command[0]],list) or isinstance(var[command[0]],tuple):
                    for con in range(len(var[command[0]])):
                        if "|" in str(var[command[0]][con]):
                            conli = var[command[0]][con].split("|")
                            consubli = []
                            consubsubli = []
                            for cl in conli:
                                cl = cl.strip()
                                clli = cl.split(" ")
                                consubli.append(clli)
                            for clx in consubli:
                                clx[0] = clx[0].strip()
                                clx[0] = clx[0].strip("!@#$%^&*()-+=:;><?/\|',.~`1234567890")
                                consubsubli.append(clx[0])
                            for cli in consubsubli:
                                if cli in var:
                                    var[command[0]][con] = var[command[0]][con].replace("|"+cli+"|",str(var[cli]))
                if isinstance(var[command[0]],str):
                    con = str(var[command[0]])
                    if "|" in con:
                        conli = con.split("|")
                        consubli = []
                        consubsubli = []
                        for cl in conli:
                            cl = cl.strip()
                            clli = cl.split(" ")
                            consubli.append(clli)
                        for clx in consubli:
                            clx[0] = clx[0].strip()
                            clx[0] = clx[0].strip("!@#$%^&*()-+=:;><?/\|',.~`1234567890")
                            consubsubli.append(clx[0])
                        for cli in consubsubli:
                            if cli in var:
                                con = con.replace("|"+cli+"|",str(var[cli]))
                                var[command[0]] = con
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

        
            continue
    return path,origin

        

        

