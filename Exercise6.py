##################################################################################
##################################################################################
#####                                                                    #########
##### program which compute the fibonacci sequence's of an input number  #########
#####                                                                    #########
##################################################################################
##################################################################################
#base values 
F_0=0
F_1=1
#creation of list containing the base values
l=[F_0,F_1]
n=int(input("enter a number greater than 2    "))
# condition to make sure that the value of n is greater than 2
while (n<2):
	print("error enter a number greater than 2  ")
	n=int(input( ))
# computation of sequences and add to list containing the base values
for  t in range(2,n+1):
	val=l[t-1]+l[t-2]
	l.append(val)
#print the finite list
print("the values of Fn for n=",0,"to",n,"are respectively in the folowing list ",l)
