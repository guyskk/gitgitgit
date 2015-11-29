# -*- coding:UTF-8 -*-

def quick_sort(ary):
	return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
	if left >= right : 
		return ary
	key = ary[left]
	lp = left
	rp = right
	while lp < rp :
		while ary[rp] >= key and lp < rp :
			rp -= 1
		while ary[lp] <= key and lp < rp :
			lp += 1
		ary[lp],ary[rp] = ary[rp],ary[lp]
	ary[left],ary[lp] = ary[lp],ary[left]
	qsort(ary,left,lp-1)
	qsort(ary,rp+1,right)
	return ary

numbers = raw_input("input your unsorted numbers split by comma:")
ary = numbers.split(",")
print "the number list sorted:%s" % quick_sort(ary)