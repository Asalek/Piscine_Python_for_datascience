
def NULL_not_found(object: any) -> int:
	types = {
		None: "Nothing",
		float('nan'): "Cheese",
		0: "Zero",
		'': "Empty",
		False: "Fake"
	}
	typee = object.__class__
	object_type = types.get(object, "Type not Found")
	if typee is float and object != object:  # NaN is the only value in Python that is not equal to itself
		print("Cheese", ':', object, typee)
	elif typee is int and object == 0:
		print("Zero", ':', object, typee)
	elif typee is str and object != '':
		print(object_type)
	else:
		print(object_type, ':', object , typee)

	if (object_type == "Type not Found"):
		return 1
	else:
		return 0

