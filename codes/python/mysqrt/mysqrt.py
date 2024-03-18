"""
my module of sqrt

"""
def sqrt2(x, debug = False):
	"""
	msqrt.sqrt2
	"""
	from numpy import nan
	if x==0:
		return 0
	elif x<0:
		return nan
	s = 1.0
	kmax = 10
	tol = 0.001
	for k in range(kmax):
		if debug:
			print(f"At iteration {k} the value of s = {s}")
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s - s0
		if(abs(delta_s)/x < tol):
			break
		if debug:
			print(f"actual s = {s}")
			print(f"Finally, the value of s = {s:1.4f}")
	return s

if __name__ == "__main__":
	from test_case import test_1
	print("in main")
	test_1()
	
