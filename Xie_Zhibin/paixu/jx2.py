while True:
    a = input("Enter a standard list, Please:")
    i = 0
    d = len(a)

    while i < (d - 1):
        j = 0
        while j < (d - 1):
            if (a[j] < a[j + 1]):
                a[j],a[j + 1] = a[j + 1],a[j]
            j = j + 1
        i = i + 1

    print "The list which sorted by Mr.Xie was become:",a