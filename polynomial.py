# Moaz Nabeel

x=input('Input or type x: ')

coef_list=map(int,raw_input(' Enter the 4 values of coefficients in a descending order : ').split())
n=len(coef_list)
for i in range(n):
	y_x=coef_list[0]*(x**n) + coef_list[1]*(x**(n-1)) + coef_list[2]*(x**(n-2)) + coef_list[3]*(x**(n-3))
	
print y_x



