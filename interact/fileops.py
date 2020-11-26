try:
    import sys
except:
    print("os-sys (installation reqd. - yes")
    time.sleep(3)
    quit()
else:
    pass

try:
    import os
except:
    print("os (installation reqd. - yes")
    time.sleep(3)
    quit()
else:
    import os.path

try:
    import shutil
except:
    print("shutil (installation reqd. - yes")
    time.sleep(3)
    quit()
else:
    pass


def help():
    print("\nLink : https://github.com/siddhanth78/interact_module/blob/master/fileops.txt\n")


def readfile(filepath="",return_="whole",amt=0):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        file = open(filepath,'r')
        if return_ == "whole":
            if amt==0:
                data=file.read()
                file.close()
                return data
            else:
                data=file.read(amt)
                file.close()
                return data
        elif return_ == "lines":
            if amt==0:
                data=file.readlines()
                file.close()
                return data
            else:
                data=[]
                for x in range(amt):
                    data.append(file.readline())
                file.close()
                return data
        else:
            data=file.read()
            file.close()
            return data


def bin_readfile(filepath="",return_="whole",amt=0,dec=""):
    try:
        file = open(filepath,'rb')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        file = open(filepath,'rb')
        if return_ == "whole":
            if amt==0:
                data=file.read()
                file.close()
                if dec!="":
                    data = data.decode(dec)
                return data
            else:
                data=file.read(amt)
                file.close()
                if dec!="":
                    data = data.decode(dec)
                return data
        elif return_ == "lines":
            if amt==0:
                data=[]
                datas = file.readlines()
                for x in datas:
                    dat = x
                    if dec!="":
                        data = data.decode(dec)
                    data.append(dat)
                file.close()
                return data
            else:
                data=[]
                for x in range(amt):
                    dat = file.readline()
                    if dec!="":
                        data = data.decode(dec)
                    data.append(dat)
                file.close()
                return data
        else:
            data=file.read()
            file.close()
            if dec!="":
                data = data.decode(dec)
            return data



def writefile(filepath="",newdata="",mode="append"):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        if mode == "append":
            file = open(filepath,'a')
            file.write(newdata)
            file.close()
        elif mode == "overwrite":
            file = open(filepath,'w')
            file.write(newdata)
            file.close()
        else:
            file = open(filepath,'a')
            file.write(newdata)
            file.close()



def bin_writefile(filepath="",newdata="",mode="append",enc="utf-8"):
    newdata=bytearray(newdata,enc)
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        if mode == "append":
            file = open(filepath,'ab')
            file.write(newdata)
            file.close()
        elif mode == "overwrite":
            file = open(filepath,'wb')
            file.write(newdata)
            file.close()
        else:
            file = open(filepath,'ab')
            file.write(newdata)
            file.close()



def createfile(filepath=""):
    if os.path.exists(filepath)==True:
        print("\nFile already exists.\n")
    elif os.path.exists(filepath)==False:
        file = open(filepath,'x')
        file.close()



def deletefile(filepath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.remove(filepath)



def runfile(filepath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.system(filepath)



def rename(filepath="",newpath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.rename(filepath,newpath)



def movefile(filepath="",newpath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.replace(filepath,newpath)



def copyfile(filepath="",copypath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        shutil.copyfile(filepath,copypath)
