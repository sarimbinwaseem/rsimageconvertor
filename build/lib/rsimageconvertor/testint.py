from convertor import Convertor

con = Convertor()

mini = 100
while True:
	e = con.adjWidth(6014, 4014, mini)
	if type(e) is int or mini >= 6014:
		print(mini)
		break
	else:
		mini += 1

