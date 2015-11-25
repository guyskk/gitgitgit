while True:
    a = raw_input("Enter something to calculate\n(You must use space between numbers and operator to dividethem,\nor the programming may report errors!):")
    b = a.split(" ")
    c = float(b[0])
    d = b[1]
    e = float(b[2])
    if d == "+":
        print "The sum is:",c + e
    elif d == "-":
        print "The difference is:",c - e
    elif d == "*":
        print "The product is:",c * e
    elif d == "/":
        print "The quotient is:",c / e
    elif d =="**":
        print "The exponential is:",c ** e
    else:
        print "Check your input, Please!"