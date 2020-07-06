# def min():
# 	print("min")

# m = min([5, 4, 3])
# print(m)

x = "global x"

def outer():
	# global x
	# x = "outer x"

	def inner():
		# nonlocal x
		# global x
		# x = "inner x"
		print(x)

	inner()
	print(x)

outer()
print(x)