def ensure_correct_info(*args):
	if "Fernando" in args and "King" in args:
		return "Welcome back Fer!"
	return "Note sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

print(ensure_correct_info(1, True, "King", "Fernando"))

