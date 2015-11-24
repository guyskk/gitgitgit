i=0
q = raw_input("number1:")
w = raw_input("number2:")
e = raw_input("number3:")
r = raw_input("number4:")
t = raw_input("number5:")
y = raw_input("number6:")
u = raw_input("number7:")
v = raw_input("number8:")
o = raw_input("number9:")
number = [q,w,e,r,t,y,u,v,o]
def X():
	j=7
	while j>=0:
		if number[j+1]<number[j]:
			number.insert(j,number[j+1])
			number.pop(j-8)
		j-=1
while i>=0:
	for t in range(8):
		X()
	i-=1
print number