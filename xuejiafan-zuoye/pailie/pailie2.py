i=0
q = raw_input("number1:")
w = raw_input("number2:")
e = raw_input("number3:")
r = raw_input("number4:")
t = raw_input("number5:")
y = raw_input("number6:")
u = raw_input("number7:")
t = raw_input("number8:")
o = raw_input("number9:")
number = [q,w,e,r,t,y,u,t,o]
def R():
	j=7
	while j>=0:
		if (number[j+1]<number[j]):
			number[j],number[j+1]=number[j+1],number[j]
		j-=1
while i<1:
	for t in range(9):
		R()
	i+=1
print number