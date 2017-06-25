def report_card():
	a=int(input(' Enter the number of classes you took: '))
	nameslist=[]
	scoreslist=[]
	total=0
	for i in range(a):
		name=raw_input("Enter the name of your class? ")
		score=int(input('What was your grade: '))
		nameslist.append(name)
		scoreslist.append(score)
	print(" Report Card ")
	for i in range(a):
		print(nameslist[i],"---->", scoreslist[i])
		total=total+scoreslist[i]
	print("Overall GPA is: ", total/float(a))

report_card()	
	
	
      



