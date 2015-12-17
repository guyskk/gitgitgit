while True:
    a = input("Enter a standard list, Please:")
    import pdb; pdb.set_trace()  # breakpoint 70d01fab //
    b = []
    d = len(a)
    i = 0

    while (i < d):
        j = 0
        c = max(a)
        b.append(c)
        while (a[j] != c):
            j = j + 1
        del a[j]
        i = i + 1

    print "The list which sorted by Mr.Xie was become:",b
