#without parameters
def func1():
	print("hiiiiiii")
	print("hellloooo")
func1()

#with parameters
def func2(a):
	print("hi \t",a)
func2("abs")

#with 2/3 parameters
def func3(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func3(1,2,3)

def func4(university="CMR"):
	print("I am in"+"\t "+university)
func4("IIM")
func4("IIT")
func4()

#return statement
def func5(a,b,c):
	d=a+b+c
	return d
e=func5(1,2,3)
print(e)

#calling onefunction from other return function
def func6(a,b):
	print("hey other function") 
	c=a+b
	return c
def func7():
	print("hello,I am goona call other function")
	s=func6(5,6)
	print("addition is",s)
func7()