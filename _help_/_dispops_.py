def dispops(command):
    print()
    if command=="msg":
        print("msg : Display a message.\nSyntax: msg::<message>::optional[<flush(0/1)>]::optional[<endwith(newline/nonewline/any other character or symbol)>]")
    elif command=="star":
        print("star : Display a starred message.\nSyntax: star::<message>::optional[<flush(0/1)>]::optional[<endwith(newline/nonewline/any other character or symbol)>]")
    elif command=="box":
        print("box : Display a boxed message.\nSyntax: box::optional[<title>]::<message>")
    elif command=="error":
        print("error : Display a boxed error message.\nSyntax: error::optional[<message>]")
    elif command=="warn":
        print("warn : Display a boxed warning.\nSyntax: warn::<message>")
    elif command=="info":
        print("info : Display a info box.\nSyntax: info::<message>")
    elif command=="tip":
        print("tip : Display a tip box.\nSyntax: tip::<message>")
    print()
