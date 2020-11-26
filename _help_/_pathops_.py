def pathops(command):
    print()
    if command=="newhomepath":
        print("newhomepath : Use a new root path.\nSyntax: newhomepath::<path>")
    elif command=="homepath":
        print("homepath : Display root path.")
    elif command=="delpath":
        print("delpath : Remove last added directory from current path.")
    elif command=="showpath":
        print("showpath : Display all paths from current path.")
    elif command=="addpath":
        print("addpath : Add a directory to current path.\nSyntax: addpath::<path>")
    elif command=="findpath":
        print("findpath : Search and display all paths that match the search.\nSyntax: findpath::<keyword>")
    print()
