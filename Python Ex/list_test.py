list = [1,2,3,4,5,6,7,8,9]

def win(x):
	y = False
	
	if all (n in x for n in [1,20,3]) :
		y = True
		
	return y

print win(list)
	
	
  