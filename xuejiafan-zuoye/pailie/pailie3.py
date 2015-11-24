q = raw_input("number1:")
w = raw_input("number2:")
e = raw_input("number3:")
r = raw_input("number4:")
t = raw_input("number5:")
y = raw_input("number6:")
u = raw_input("number7:")
t = raw_input("number8:")
o = raw_input("number9:")
a = [q,w,e,r,t,y,u,t,o]
def select_sort(a):
    a_len=len(a)  
    for i in range(a_len):
        min_index = i
        for j in range(i+1, a_len):
            if(a[j]<a[min_index]):  
                min_index=j  
        if min_index != i:
            a[i],a[min_index] = a[min_index],a[i]  
print 'Before sort:',a   
select_sort(a)    
print 'After sort:',a