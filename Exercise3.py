####################################################################################
################ program which compute pi from the first 20 ########################
###################      terms of the Madhava series        ########################
####################################################################################
from math import sqrt
#initial value of sum
som=0
for n in range(20):
	som=som+((-1)**n)/((2*n+1)*(3**n))
#value of the sum given by Madhava series 
P=sqrt(12)*som
print("the value of pi compute from the first 20  terms Madhava series is:pi=",P)
