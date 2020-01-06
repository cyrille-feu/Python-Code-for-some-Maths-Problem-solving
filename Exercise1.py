##############################################################################################
##############################################################################################
###################                  question 1                         ######################
##############################################################################################
##############################################################################################
#function which take as input an integer p,a numeral n made up k digits and compute the sum of 
#digit of digit of n power p
#our function is called f_p_n
def f_p_n(n,p):
	#conversion of numeral n in list
	n1=list(str(n))
	#initial value of sum
	f=0
	# computing successively the sum
	for i in range(len(n1)):
		f=f+int(n1[i])**p
	#return the final result
	return f

##############################################################################################
##############################################################################################
###################                  question 2                         ######################
##############################################################################################
##############################################################################################
#function which takes as input p and return a list of p+5 element computed by i/(10**(i-1))
# where i is index
def g_p(p):
	#creation of empty list
	l=[]
	for i in range(1,p+6):
		#computing of value with index i
		val=i/(10**(i-1))
		# add a value in list
		l.append(val)
	return l

##############################################################################################
##############################################################################################
###################                  question 3                         ######################
##############################################################################################
##############################################################################################
#function which takes as input an integer p, a list l1 and return a list of bolean. 
#if l1[i])<1/(9**p) the result is 1 and 0 else
def h_p_l(p,l1):
	l2=[]
	for i in range (len(l1)):
		if(l1[i]<(1/9)**p):
			l2.append(1)
		else:
			l2.append(0)
	return l2
##############################################################################################
#observation: after computation for somes values of p we observe that for any values of p,
# l1[i]<(1/9)**p) is true if i>=p+2.       
##############################################################################################


##############################################################################################
##############################################################################################
###################                  question 4                         ######################
##############################################################################################
##############################################################################################
# program which create a list of 0 elements using i*(9**3) at index i
l=[]
for i in range(20):
	val=i*(9**3)
	l.append(val) 

##############################################################################################
##############################################################################################
###################                  question 5                         ######################
##############################################################################################
##############################################################################################
# function loop which return the list of numeral forming the loop obtained while computing 
#successive images by function f_p_n(n,p)
def loop_p_n(p,n):
	#creation of empty list
	l3=[]
	#add initial number in list
	l3.append(n)
	#compute the firsT image
	n=f_p_n(n,p)
	#add the first image in list
	l3.append(n)
	a=0
	while (a==0):
		#compute the next image and compare with all number in list
		#stop when we have the first repetition
		n=f_p_n(n,p)
		t=0
		while (t<len(l3)):
			if(l3[t]==n):
				a=1
				t=len(l3)
			else: 
				a=0
				t=t+1
		#add image in list
		l3.append(n)
	return l3
##############################################################################################
##############################################################################################
###################             test of our differents function         ######################
##############################################################################################
##############################################################################################
n=int(input("Enter a value of n      "))
while n<=0:
	print("enter a number greater than 0")
	n=int(input( ))
p=int(input("Enter a value of p     "))
while n<=1:
	print("enter a number greater than 1")
	n=int(input( ))
A=f_p_n(n,p)
print("the sum of digit of",n,"power",p,"is sum=",A)
B=g_p(p)
print("the list of p+5 elements is:",B)
C=h_p_l(p,B)
print("the list of bolean is:",C)
D=loop_p_n(p,n)
v=D.index(D[-1])
print("the loop is given by:",D,"and it start at f(p,n)=",D[v],"and end at",D[-2])
