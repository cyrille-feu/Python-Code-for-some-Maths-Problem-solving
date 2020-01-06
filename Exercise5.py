#####################################################################################3#
######### program which compute the square root of a number S with HERO'S method,######
##########compare with the "exact" value provided by the math.sqrt method #############
########## and givethe value of n which the two results becomme the same ##############
#######################################################################################

from math import sqrt
s=2117519.73
err=1
N=0
#initial value of x
x=2000
# computing x until err=0
while(err!=0):
	x=0.5*(x+(s/x))
	N=N+1
	err=sqrt(s)-x
	print(" iteration number ",N)
	print("the value of square root computed by HERO'S method is val1= ",x)
	print("the value of square root computed by math.sqrt is val2=",sqrt(s))
	print(" the error at this step is err=",err)
print("the value of n such that the both results are the same is n=",N-1)
