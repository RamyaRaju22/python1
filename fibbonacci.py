n = 10
a = 0 
b = 1
count = 0
if n<=0:
	print("please enter a positive integer")
elif n==1:
	print("fibbonacci series:",n)
	print(i)
else:
	print("fibbonacci series:",n)
	while count < n:
		print(a)
		sum=a+b
		a=b
		b=sum
		count = count+1
