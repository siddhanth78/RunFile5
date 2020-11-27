import os
import webbrowser
import sys
import interact.display as disp

def _3_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist):
        if command[0] not in arg3:
            if command[0] in arg1:
                print("rf5>>Command '{}' takes 1 argument. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg2:
                print("rf5>>Command '{}' takes 2 arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg0:
                print("rf5>>Command '{}' doesn't take arguments. Enter 'help' for more info.".format(command[0]))
            return

        types = ['int','string','float','list','tuple','menu']

        if com_arg[0] in commandlist and command[0] in types:
            print("rf5>>Invalid variable name.")
            return

        if com_arg[1]=='prompt':
            if command[0]=='int':
                try:
                    var[com_arg[0]] = int(disp.prompt(com_arg[2]))
                except:
                    print("rf5>>Invalid value.")
                else:
                    pass
            elif command[0]=='float':
                try:
                    var[com_arg[0]] = float(disp.prompt(com_arg[2]))
                except:
                    print("rf5>>Invalid value.")
                else:
                    pass
            elif command[0]=='string':
                try:
                    var[com_arg[0]] = str(disp.prompt(com_arg[2]))
                except:
                    print("rf5>>Invalid value.")
                else:
                    pass
            elif command[0]=='list':
                try:
                    var[com_arg[0]] = str(disp.prompt(com_arg[2]))
                    typeliarg=[]
                    typeli = var[com_arg[0]].split(",")
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
                    var[com_arg[0]] = typeliarg
                except:
                    print("rf5>>Invalid value.")
                else:
                    pass
            elif command[0]=='tuple':
                try:
                    var[com_arg[0]] = str(disp.prompt(com_arg[2]))
                    typeliarg=[]
                    typeli = var[com_arg[0]].split(",")
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
                    var[com_arg[0]] = tuple(typeliarg)
                except:
                    print("rf5>>Invalid value.")
                else:
                    pass
        elif command[0]=='msg':
            if com_arg[0] in var:
                com_arg[0] = var[com_arg[0]]
            if com_arg[2] in var:
                com_arg[2] = var[com_arg[2]]
                
            if com_arg[2] == 'newline':
                com_arg[2] = "\n"
            elif com_arg[2] == 'nonewline':
                com_arg[2] = ""
            else:
                pass
            disp.msg(m=com_arg[0],f=int(com_arg[1]),e=com_arg[2])
        elif command[0]=='star':
            if com_arg[0] in var:
                com_arg[0] = var[com_arg[0]]
            if com_arg[2] in var:
                com_arg[2] = var[com_arg[2]]
                
            if com_arg[2] == 'newline':
                com_arg[2] = "\n"
            elif com_arg[2] == 'nonewline':
                com_arg[2] = ""
            else:
                pass
            disp.star(m=com_arg[0],f=int(com_arg[1]),e=com_arg[2])
        elif command[0]=='menu':
            if com_arg[2] in var:
                com_arg[2] = var[com_arg[2]]
            if type(com_arg[2])!=list:
                typeliarg=[]
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
                com_arg[2] = typeliarg
            var[com_arg[0]]=disp.menu(title=com_arg[1],items=com_arg[2],reuse=1)
        else:
            print("rf5>>Invalid input.")
        
            
        
    
