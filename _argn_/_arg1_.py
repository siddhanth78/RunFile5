import os
import webbrowser
import sys
import interact.display as disp
from googlesearch import *

def _1_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist):
        if command[0] not in arg1:
            if command[0] in arg0:
                print("rf5>>Command '{}' doesn't take arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg2:
                print("rf5>>Command '{}' takes 2 arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg3:
                print("rf5>>Command '{}' takes 3 arguments. Enter 'help' for more info.".format(command[0]))
            return origin,path

        types = ['int','string','float','list','tuple']

        if com_arg[0] in var and command[0] not in types:
            com_arg[0] = var[com_arg[0]]

        if command[0]=='type':
            try:
                print(type(com_arg[0]))
            except:
                print("rf5>>Invalid value")
            else:
                pass
            return origin,path

        if command[0]=="error":
            disp.error(com_arg[0])
            return origin,path

        if command[0]=="box":
            disp.box(m=com_arg[0])
            return origin,path

        if command[0]=="info":
            disp.info(com_arg[0])
            return origin,path

        if command[0]=="warn":
            disp.warn(com_arg[0])
            return origin,path

        if command[0]=="tip":
            disp.tip(com_arg[0])
            return origin,path

        if command[0]=='msg':
            disp.msg(m=com_arg[0])
            print()
            return origin,path

        if command[0]=='star':
            disp.star(m=com_arg[0])
            print()
            return origin,path

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
                if flagname==1:
                    var[com_arg[0]] = 0
                else:
                    pass
            return origin,path

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
                if flagname==1:
                    var[com_arg[0]] = ""
                else:
                    pass
            return origin,path

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
                if flagname==1:
                    var[com_arg[0]] = 0.0
                else:
                    pass
            return origin,path

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
                if flagname==1:
                    var[com_arg[0]] = []
                else:
                    pass
            return origin,path

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
                if flagname==1:
                    var[com_arg[0]] = ()
                else:
                    pass
            return origin,path

        if command[0]=="searchhistory":
            if os.path.exists(historydir)==False:
                print("rf5>>No history found.")
                return origin,path
            filee = open(historydir,'r')
            histdata = filee.readlines()
            filee.close()
            if histdata==[]:
                print("rf5>>No history found.")
                return origin,path
            print()
            for x in histdata:
                x = x.strip()
                x = x.strip("\n")
                if com_arg[0] in x:
                    print(x)
            print()
            return origin,path

        if command[0]=='browse':
            print("\nSearch:{}\n".format(com_arg[0]))
            browse_path = browserPath
            for url in search(com_arg[0], tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % com_arg[0])
            return origin,path

        try:
            lif = com_arg[0].split('.')
            ext=""
            file = lif[0]
            file = file.strip()
            if len(lif)>=2:
                ext = lif[1]
                ext = ext.strip()
            file = file.replace("/",".")
            file = file.replace("\\",".")
        except:
            print("rf5>>An error occured. Check your input and try again.")
        else:
            pass
        
        if ext!="py" and command[0]=='funclist':
            print("rf5>>Command '{}' works with '.py' files only.".format(command[0]))
        else:
            pass

        if command[0]=='addpath':
            if "." in com_arg[0]:
                print("rf5>>Cannot add file to path.")
                return origin,path
            if os.path.exists(pt:=(path+"\\"+com_arg[0]))==False:
                print(f"rf5>>Path '{pt}' doesn't exist.")
                return origin,path
            path = path+"\\"+com_arg[0]
            com_arg[0] = com_arg[0].replace("/",".")
            com_arg[0] = com_arg[0].replace("\\",".")
            if func.strip()=="":
                func=com_arg[0]
            else:
                func = func+"."+com_arg[0]
            func=func.strip()
            if "-" in func:
                print("rf5>>Invalid character '-' found. Files may or may not open and 'runfunc' will not work.")
            print("\nNewPath:{}".format(path))
            if com_arg[0][0]=='.' or com_arg[0][0]=='.':
                print("rf5>>Dir/subdir request beginning with '/' or '\\' may result in wrong path.")
            return origin,path

        if command[0]=='createfile':
            if os.path.exists(path+"\\"+com_arg[0])==True:
                print("rf5>>File '{}' already exists.".format(com_arg[0]))
            else:
                try:
                    filee = open(path+"\\"+com_arg[0],'x')
                    filee.close()
                except:
                    print("rf5>>An error occured. Check your input and try again.")
                else:
                    print("rf5>>File '{}' has been created.".format(com_arg[0]))
            return origin,path

        if command[0]=='delfile':
            try:
                os.remove(path+"\\"+com_arg[0])
            except:
                print("rf5>>File '{}' doesn't exist.".format(com_arg[0]))
            else:
                print("rf5>>File '{}' has been deleted.".format(com_arg[0]))
            return origin,path

        
        if command[0]=='findpath':
            print()
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    if com_arg[0].lower() in name.lower():
                        print(os.path.join(root, name))
                for name in dirs:
                    if com_arg[0].lower() in name.lower():
                        print(os.path.join(root, name))
            print()
            return origin,path

        if command[0]=='newhomepath':
            origin=com_arg[0].replace("/","\\")
            if os.path.exists(pt:=origin)==False:
                print(f"rf5>>Path '{pt}' doesn't exist.")
                origin = os.getcwd()
                path=origin
                func=""
                print("\nHomePath:{}".format(origin))
            else:
                path=origin
                func=""
                print("\nNewHomePath:{}".format(origin))
            return origin,path

        if os.path.exists(path+"\\"+com_arg[0])==False:
            print("rf5>>File '{}' doesn't exist.".format(com_arg[0]))
            return origin,path
        else:
            pass

        if command[0]=='RunFile':
            filee = open(path+"\\"+com_arg[0],'a')
            filee.write("#RunFile\n")
            filee.close()
            if ext=="py":
                print("rf5>>The output of this file will now be displayed on the terminal.")
            return origin,path

        if command[0]=='content':
            try:
                filee = open(path+"\\"+com_arg[0],'r')
                data = filee.read()
                print("\n{}\n".format(data.strip("\n")))
            except:
                print("rf5>>Couldn't read file.")
            finally:
                filee.close()
            return origin,path
        
        if command[0]=='clearcontent':
            filee = open(path+"\\"+com_arg[0],'w')
            filee.write("")
            filee.close()
            print("rf5>>File content has been deleted.")
            return origin,path

        if command[0]=='addcontent':
            sub=0
            print("\nFile:{}\n".format(com_arg[0]))
            while True:
                try:
                    file = open(path+"\\"+com_arg[0],'a')
                    con = input(" "*sub+">")
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
                    if con=='[endfile]':
                        file.close()
                        print("\nrf5>>New content has been added.")
                        break
                    file.write(" "*sub+con+"\n")
                except:
                    print("\nrf5>>An unexpected error occured. File will be closed.")
                    file.close()
                    break
                else:
                    pass
            file.close()
            return origin,path

        if ext=='py':
            filee = open(path+"\\"+com_arg[0],'r')
            datar = filee.read()
            filee.close()
            if command[0]=='runfile':
                print("\nStart:{}".format(com_arg[0]))
                if "#RunFile" in datar:
                    os.system(r'{}'.format(path+"\\"+com_arg[0]))
                else:
                    webbrowser.open(r'{}'.format(path+"\\"+com_arg[0]))
                print("Stop:{}\n".format(com_arg[0]))
            elif command[0]=='funclist':
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
                            funcname = funcname+x
                        
                        if 'def ' in lines:
                            print("Function:"+funcname)
                        elif 'class ' in lines:
                            print("Class:"+funcname)
                print()
            return origin,path
        else:
            if command[0] == 'runfile':
                print("\nStart:{}".format(com_arg[0]))
                webbrowser.open(r"{}".format(path+"\\"+com_arg[0]))
                print("Stop:{}\n".format(com_arg[0]))
            return origin,path
            
        
    
