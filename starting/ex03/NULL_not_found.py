import math

def NULL_not_found(object: any) -> int:
	types = {
		None: "Nothing",
		math.nan: "Cheese",
		0: "Zero",
		'': "Empty",
		False: "Fake"
	}
	typee = object.__class__
	object_type = types.get(object, "Type not Found")
	if typee is float and math.isnan(object):
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

