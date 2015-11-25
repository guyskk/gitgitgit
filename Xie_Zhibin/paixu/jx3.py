while True:
    a = input("Enter a standard list, Please:")
    i = 0
    d = len(a)

    while (i < (d - 1)):
        b = a[i:d]
        c = max(b)
        if (b[0] != c):
            j = 0
            while (b[j] != c):
                j = j + 1
            b[0],b[j] = b[j],b[0]
        a[i:d] = b
        i = i + 1
        
    print "The list which sorted by Mr.Xie was become:",a