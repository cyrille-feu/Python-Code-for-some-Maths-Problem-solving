##################################################################################
######### program which Given the list of test scores, produce a list#############
######### associating each score with a rank (starting with 1 for the ############ 
######### highest score). Note that equal scores have the same rank.  ############
##################################################################################
##################################################################################
#creation of 3 empty list                                                        
l1=[]
l2=[]
l3=[]
# enter a number of elements of the list l1
n=int(input("how many elements in your list      "))
# condition to make sure that we enter a positive number
while n<=0:
	print("enter a number greater than 0")
	n=int(input( ))
t=0
#enter all the element of list l1 and initialize all the element of l2 at 0
# l3 is just to save our initial list 
while(t<n):
	number=t+1
	print("enter the element number",number,"of your list")
	b=int(input())
	#add the number in list
	l1.append(b)
	l2.append(0)
	l3.append(b)
	t=t+1
# f is the testing value in condition if
f=0
i=1
# r is variable which permit to compute the list of index
r=1
#condition to make sure that we take all the numbers in list 1
while (i<len(l1)+1):
	t=max(l1)
	k=l1.index(t)
	if(t==f):
		r=r-1
		l2[k]=r
	else:
		l2[k]=r
	f=max(l1)
	l1[k]=min(l1)-1
	r=r+1
	i=i+1
print("the  input  list is l1=",l3)
print("the list of rank is l2=",l2)
