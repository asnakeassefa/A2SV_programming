TotalTshirt = int(input())

size = {"S":1,"M":2,"L":3}

for i in range(TotalTshirt):
	val = input().split(" ")
	if size[val[0][-1]] > size[val[1][-1]]:
		print(">")
	elif size[val[0][-1]] < size[val[1][-1]]:
		print("<")
	else:
		if val[0][-1] == "S":
			if len(val[0]) > len(val[1]):
				print("<")
			elif len(val[0]) == len(val[1]):
				print('=')
			else:
				print(">")
		elif val[0][-1] == "M":
			print("=")
		else:
			if len(val[0]) < len(val[1]):
				print("<")
			elif len(val[0]) == len(val[1]):
				print('=')
			else:
				print(">")
