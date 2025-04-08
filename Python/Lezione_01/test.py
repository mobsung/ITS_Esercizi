def is_float(value) -> bool:
    try:
        float(value)  # Try to convert the string to a float
        return True   # If successful, it's a float
    except ValueError:
        return False  # If conversion fails, it's not a float
    

a = "1.22"
is_float(a)

print(type(a))