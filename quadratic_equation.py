def quad():
	from math import sqrt
	print(" This solves a quadratic equation ax^2+bx+c ")
	a=int(input(" What is the integer value of a ? "))
	b=int(input(" What is the integer value of b ? "))
	c=int(input(" What is the integer value of c ? "))
	discriminant=(b**2)-(4*a*c)
	
	if discriminant <0:
		print(" Sorry this calculator does not calculate Imaginary roots" )
		 
	elif discriminant==0:
		value=0
		print("The root is: "+ int(value))
	else:
		 discriminant1=float(sqrt(discriminant))
		 positive_value=(-b+discriminant1) / (2*a)
		 negative_value=(-b-discriminant1) / (2*a)
		 print("The positive value is: "+ str(positive_value))
		 print("The negative value is: "+ str(negative_value))
quad()	
	
