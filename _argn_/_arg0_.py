import os
import webbrowser
import sys
import interact.display as disp
from googlesearch import *

def _0_(arglen,command,com_arg,path,historydir,origin,func,var,browserPath,arg0,arg1,arg2,arg3,invalidnames,commandlist):
    if arglen==1:
        if command[0] not in arg0:
            if command[0] in arg1:
                print("rf5>>Command '{}' takes 1 argument. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg2:
                print("rf5>>Command '{}' takes 2 arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg3:
                print("rf5>>Command '{}' takes 3 arguments. Enter 'help' for more info.".format(command[0]))
            return path,origin
            

        if command[0]=="error":
            disp.error()
            return path,origin

        if command[0]=="history":
            if os.path.exists(historydir)==False:
                print("rf5>>No history found.")
                return
            filee = open(historydir,'r')
            histdata = filee.read()
            print("\n"+histdata)
            filee.close()
            return path,origin
            

        if command[0]=="clearhistory":
            if os.path.exists(historydir)==False:
                print("rf5>>No history found.")
                return
            filee = open(historydir,'w')
            filee.write("")
            filee.close()
            print("rf5>>History has been cleared.")
            return path,origin
            
        
        if command[0]=='clear' or command[0]=='clr':
            os.system('cls')
            print("RunFile 5.2.2. Enter 'help' for more info.\n")
            print("HomePath:{}".format(path))
            return path,origin
            

        if command[0]=="quit":
            quit()

        if command[0]=='homepath':
            path=origin
            func=""
            print("\nHomePath:{}".format(path))
            return path,origin
            

        if command[0]=='showpath':
            print()
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    print("File:"+os.path.join(root, name))
                for name in dirs:
                    print("Directory:"+os.path.join(root, name))
            print()
            return path,origin

        if command[0]=='delpath':
            if path==origin:
                print("rf5>>Cannot delete from original path.")
                return path,origin
            count=0
            lipath = path.split("\\")
            lipath.pop(-1)
            path=""
            for l in lipath:
                count+=1
                if count==len(lipath):
                    path=path+l
                    break
                path = path+l+"\\"
            fucount=0
            if "." not in func:
                func=""
            else:
                lifu = func.split(".")
                lifu.pop(-1)
                func=""
                for fu in lifu:
                    fucount+=1
                    if fucount==len(lifu):
                        func=func+fu
                        break
                    func=func+fu+"."
            func=func.strip()
            print("\nNewPath:{}".format(path))
            return path,origin
            
        
    
