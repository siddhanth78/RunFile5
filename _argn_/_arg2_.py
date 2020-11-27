import os
import webbrowser
import sys
import interact.display as disp
from googlesearch import *

def _2_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist):
        if command[0] not in arg2:
            if command[0] in arg0:
                print("rf5>>Command '{}' doesn't take arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg1:
                print("rf5>>Command '{}' takes 1 argument. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg3:
                print("rf5>>Command '{}' takes 3 arguments. Enter 'help' for more info.".format(command[0]))

        types = ['int','string','float','list','tuple']
            
        if com_arg[0] in var and command[0] not in types:
            com_arg[0] = var[com_arg[0]]

        if com_arg[1] in var:
            com_arg[1] = var[com_arg[1]]

        if command[0]=="box":
            disp.box(title=com_arg[0],m=com_arg[1])
            return

        if command[0]=='storelines':
            filee = open(path+"\\"+com_arg[0],'r')
            data = filee.readlines()
            filee.close()
            var[com_arg[1]] = data
            return

        if command[0]=='store':
            filee = open(path+"\\"+com_arg[0],'r')
            data = filee.read()
            filee.close()
            var[com_arg[1]] = data
            return

        if command[0]=='addcontent':
            sub=0
            print("\nFile:{}\n".format(com_arg[0]))
            for con in com_arg[1]:
                try:
                    file = open(path+"\\"+com_arg[0],'a')
                    if con=='[sub]':
                        sub+=4
                        continue
                    if con=='[RunFile]':
                        con = "#RunFile"
                    if con=='[endsub]':
                        sub=sub-4
                        if sub<=0:
                            sub=0
                        continue
                    if "$$" in con:
                        conli = con.split("$$")
                        consubli = []
                        consubsubli = []
                        for cl in conli:
                            cl = cl.strip()
                            clli = cl.split(" ")
                            consubli.append(clli)
                        for clx in consubli:
                            consubsubli.append(clx[0])
                        for cli in consubsubli:
                            if cli in var:
                                con = con.replace("$$"+cli,var[cli])
                    file.write(" "*sub+con+"\n")
                except:
                    print("\nrf5>>An unexpected error occured. File will be closed.")
                    file.close()
                    break
                else:
                    pass
            file.close()
            print("\nrf5>>New content has been added.")
            return

        if command[0]=='int':
            if com_arg[0] in commandlist:
                print("rf5>>Invalid variable name.")
            else:
                flagname=1
                for i in invalidnames:
                    if i in com_arg[0]:
                        print("rf5>>Invalid variable name.")
                        flagname=0
                        break
                    else:
                        flagname=1
                        pass
                if flagname==0:
                    return
                try:
                    var[com_arg[0]] = int(com_arg[1])
                except:
                    print("rf5>>Invalid variable value.")
                else:
                    pass
            return
            

        if command[0]=='string':
            if com_arg[0] in commandlist:
                print("rf5>>Invalid variable name.")
            else:
                flagname=1
                for i in invalidnames:
                    if i in com_arg[0]:
                        print("rf5>>Invalid variable name.")
                        flagname=0
                        break
                    else:
                        flagname=1
                        pass
                if flagname==0:
                    return
                try:
                    var[com_arg[0]] = str(com_arg[1])
                except:
                    print("rf5>>Invalid variable value.")
                else:
                    pass
            return
            

        if command[0]=='float':
            if com_arg[0] in commandlist:
                print("rf5>>Invalid variable name.")
            else:
                flagname=1
                for i in invalidnames:
                    if i in com_arg[0]:
                        print("rf5>>Invalid variable name.")
                        flagname=0
                        break
                    else:
                        flagname=1
                        pass
                if flagname==0:
                    return
                try:
                    var[com_arg[0]] = float(com_arg[1])
                except:
                    print("rf5>>Invalid variable value.")
                else:
                    pass
            return
            

        if command[0]=='list':
            if com_arg[0] in commandlist:
                print("rf5>>Invalid variable name.")
            else:
                flagname=1
                for i in invalidnames:
                    if i in com_arg[0]:
                        print("rf5>>Invalid variable name.")
                        flagname=0
                        break
                    else:
                        flagname=1
                        pass
                if flagname==0:
                    return
                fl=0
                try:
                    typeliarg=[]
                    typeli = com_arg[1].split(",")
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
                        elif i.isnumeric()==True:
                            i = eval(i)
                        else:
                            pass
                        typeliarg.append(i)
                    var[com_arg[0]] = typeliarg
                except:
                    print("rf5>>Invalid variable value.")
                else:
                    pass
            return
            

        if command[0]=='tuple':
            if com_arg[0] in commandlist:
                print("rf5>>Invalid variable name.")
            else:
                flagname=1
                for i in invalidnames:
                    if i in com_arg[0]:
                        print("rf5>>Invalid variable name.")
                        flagname=0
                        break
                    else:
                        flagname=1
                        pass
                if flagname==0:
                    return
                fl=0
                try:
                    typeliarg=[]
                    typeli = com_arg[1].split(",")
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
                        elif i.isnumeric()==True:
                            i = eval(i)
                        else:
                            pass
                        typeliarg.append(i)
                    var[com_arg[0]] = tuple(typeliarg)
                except:
                    print("rf5>>Invalid variable value.")
                else:
                    pass
            return
            

        if command[0] in ['runfunc','findfunc']:
            try:
                lif = com_arg[0].split('.')
                file = lif[0]
                file = file.strip()
                ext = lif[1]
                ext = ext.strip()
                file = file.replace("/",".")
                file = file.replace("\\",".")
            except:
                print("rf5>>An error occured. Check your input and try again.")
            else:
                pass
        
            if ext!="py":
                print("rf5>>Command '{}' works with '.py' files only.".format(command[0]))
            else:
                pass

        if command[0]=='runfunc':
            filee = open(path+"\\"+com_arg[0],'r')
            datar = filee.read()
            filee.close()
            arg = com_arg[1]
            arg = arg.strip()
            if arg=='':
                pass
            elif '(' not in arg or ')' not in arg:
                print("rf5>>Function not completely defined.")
                return
            else:
                if func.strip()=="":
                    runfunc = file+'.'+arg
                else:
                    runfunc = func+'.'+file+'.'+arg
            print("\nStart:{}".format(com_arg[0]))

            try:
                print("Execute:{}".format(runfunc))
                if func=="":
                    exec("import {}".format(file))
                else:
                    exec("import {}".format(func+'.'+file))
                exec(runfunc)
            except:
                print("rf5>>An error occured. Check your input and try again.")
                return
            else:
                pass
            print("Stop:{}\n".format(com_arg[0]))
        elif command[0]=='findfunc':
                funct = com_arg[1]
                filee = open(path+"\\"+com_arg[0],'r')
                data = filee.readlines()
                filee.close()
                print()
                for lines in data:
                    funcname=""
                    lines = lines.strip()
                    if 'def ' in lines or 'class ' in lines:
                        lines = lines.strip(":")
                        lifunc = lines.split(" ")
                        lifunc[0]=""
                        for x in lifunc:
                            if funct in x:
                                flag=1
                                break
                            else:
                                flag=0
                            
                        if flag==1:
                            for x in lifunc:
                                funcname = funcname+x
                            
                            if 'def ' in lines:
                                print("Function:"+funcname)
                            elif 'class ' in lines:
                                print("Class:"+funcname)
                print()
        
            
        
    
