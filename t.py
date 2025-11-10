def assertEquals(expected, actual, message = "Test"):
	if expected == actual:
		quick_print("Pass")
	else:
		quick_print("Fail")