#################################################################################
#### program which,given a list of integers l1 compute a list with ##############
####      the same lenght l2 in which l2[i] is the product of all  ##############
####                 the integers in l1 except l1[i]               ##############
#################################################################################
#################################################################################    

#creation of two empty list
l1=[]
l2=[]
# enter a number of elements of the list l1
n=int(input("how many elements in your list      "))
#condition to make sure that we enter a value greater than 0
while n<=0:
	print("error, enter a number greater than 0")
	n=int(input( ))
t=0
#enter all the element of list l1 and initialize all the element of l2 at 1 
while(t<n):
	number=t+1
	print("enter the element number",number,"of your list")
	b=int(input())
	#add the number in list
	l1.append(b)
	l2.append(1)
	t=t+1
# computing of l2[i] which is the product of all the integers in l1 except l1[i]
for k in range(n):
	for t in range(n):
		if(k==t):
			l2[k]=l2[k]
		else:
			l2[k]=l2[k]*l1[t]
print("the initial list is l1=",l1)
print("the return  list is l2=",l2)
