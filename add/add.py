def add(*args) -> list:

	if len(args) == 0:
		return []

	# ensure that each list of lists (the inputs in args) are the same length
	list_of_list_length = len(args[0])
	for i, lst in enumerate(args):
		if len(lst) != list_of_list_length:
			raise ValueError("Given matrices are not the same size")

		# ensure each list within the list of list is the same length
		# assumes the list of list is not [], ie that lst[0] exists
		list_length = len(lst[0])
		for j, pair in enumerate(lst):
			if len(pair) != list_length:
				raise ValueError("Given matrices are not the same size")
	
	# step 1: use zip to get the lists lined up 
	# eg if input1 is [[1,-2], [-3,4]] and input2 is [[2,-1],[0,-1]]
	# this will line up the [1,-2] with the [2,-1]
	t1 = [x for x in zip(*args)]
	# print(f"t1: {t1}")

	# step 2: zip the [1,-2] and [2,-1] together and sum them, so sum(1,2) and sum(-2,-1)
	t2 = [[sum(x) for x in zip(*y)] for y in t1]
	# print(f"t2: {t2}")

	return t2

if __name__ == "__main__":
	lol1 = [[1, -2], [-3, 4]]
	lol2 = [[2, -1], [0, -1]]
	print(add(lol1,lol2))

