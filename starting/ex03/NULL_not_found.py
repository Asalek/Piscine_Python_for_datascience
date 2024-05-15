import math

def NULL_not_found(object: any) -> int:
	types = {
		None: "Nothing",
		math.nan: "Cheese",
		0: "Zero",
		'': "Empty",
		False: "Fake"
	}
	object_type = types.get(object, "Type not Found")
	if type(object) is float and math.isnan(object):
		print("Cheese", ':', object, type(object))
	elif type(object) is int and object == 0:
		print("Zero", ':', object, type(object))
	elif type(object) is str and object != '':
		print(object_type)
	else:
		print(object_type, ':', object , type(object))

	if (object_type == "Type not Found"):
		return 1
	else:
		return 0

